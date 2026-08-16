import json
import logging
import requests

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import CarMake, CarModel
from .populate import initiate

logger = logging.getLogger(__name__)

NODE_URL = getattr(settings, 'NODE_BACKEND_URL', 'http://localhost:3030')
SENTIMENT_URL = getattr(settings, 'SENTIMENT_ANALYZER_URL', 'http://localhost:5050')


# ──────────────────────────────────────────
# Auth Views
# ──────────────────────────────────────────

@csrf_exempt
def login_user(request):
    """POST /djangoapp/login  body: {userName, password}"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({'userName': username, 'status': 'Authenticated'})
    return JsonResponse({'userName': username, 'error': 'Invalid credentials'}, status=401)


@csrf_exempt
def logout_user(request):
    """GET /djangoapp/logout"""
    username = request.user.username if request.user.is_authenticated else 'anonymous'
    logout(request)
    return JsonResponse({'userName': username, 'status': 'Logged out'})


@csrf_exempt
def registration(request):
    """POST /djangoapp/register  body: {userName, firstName, lastName, email, password}"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')
    first_name = data.get('firstName', '')
    last_name = data.get('lastName', '')
    email = data.get('email', '')

    if User.objects.filter(username=username).exists():
        return JsonResponse({'userName': username, 'error': 'Already registered'}, status=400)

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )
    login(request, user)
    return JsonResponse({'userName': username, 'status': 'Registered'})


# ──────────────────────────────────────────
# Dealer Views  (proxy to Node.js service)
# ──────────────────────────────────────────

def get_cars(request):
    """GET /djangoapp/get_cars"""
    count = CarMake.objects.count()
    if count == 0:
        initiate()

    makes = CarMake.objects.prefetch_related('car_models').all()
    cars = []
    for make in makes:
        for model in make.car_models.all():
            cars.append({
                'CarMake': make.name,
                'CarModel': model.name,
                'CarType': model.car_type,
                'Year': model.year,
            })
    return JsonResponse({'CarMakes': [{'name': m.name, 'description': m.description} for m in makes],
                         'Cars': cars})


def get_dealerships(request, state='All'):
    """GET /djangoapp/get_dealers/[<state>/]"""
    if state == 'All':
        url = f"{NODE_URL}/fetchDealers"
    else:
        url = f"{NODE_URL}/fetchDealers/{state}"

    try:
        resp = requests.get(url, timeout=10)
        dealers = resp.json()
        return JsonResponse({'status': 200, 'dealers': dealers})
    except Exception as e:
        logger.error(f"Error fetching dealers: {e}")
        return JsonResponse({'status': 500, 'error': str(e)}, status=500)


def get_dealer_details(request, dealer_id):
    """GET /djangoapp/dealer/<dealer_id>/"""
    url = f"{NODE_URL}/fetchDealer/{dealer_id}"
    try:
        resp = requests.get(url, timeout=10)
        dealer = resp.json()
        return JsonResponse({'status': 200, 'dealer': dealer})
    except Exception as e:
        logger.error(f"Error fetching dealer {dealer_id}: {e}")
        return JsonResponse({'status': 500, 'error': str(e)}, status=500)


def get_dealer_reviews(request, dealer_id):
    """GET /djangoapp/reviews/dealer/<dealer_id>/"""
    url = f"{NODE_URL}/fetchReviews/dealer/{dealer_id}"
    try:
        resp = requests.get(url, timeout=10)
        reviews_raw = resp.json()

        # Enrich each review with sentiment
        reviews = []
        for review in reviews_raw:
            sentiment = _get_sentiment(review.get('review', ''))
            review['sentiment'] = sentiment
            reviews.append(review)

        return JsonResponse({'status': 200, 'reviews': reviews})
    except Exception as e:
        logger.error(f"Error fetching reviews for dealer {dealer_id}: {e}")
        return JsonResponse({'status': 500, 'error': str(e)}, status=500)


@csrf_exempt
def add_review(request):
    """POST /djangoapp/add_review  body: {review object}"""
    if not request.user.is_authenticated:
        return JsonResponse({'status': 401, 'error': 'Unauthorized'}, status=401)

    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    data = json.loads(request.body)
    review = data.get('review', {})

    url = f"{NODE_URL}/insertReview"
    try:
        resp = requests.post(url, json=review, timeout=10)
        return JsonResponse({'status': 200, 'result': resp.json()})
    except Exception as e:
        logger.error(f"Error adding review: {e}")
        return JsonResponse({'status': 500, 'error': str(e)}, status=500)


# ──────────────────────────────────────────
# Sentiment helper
# ──────────────────────────────────────────

def _get_sentiment(text):
    url = f"{SENTIMENT_URL}/analyze/{requests.utils.quote(text)}"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        return data.get('sentiment', 'neutral')
    except Exception:
        return 'neutral'


def analyze_review_sentiment(request, text):
    """GET /djangoapp/analyze_review/<text>/"""
    sentiment = _get_sentiment(text)
    return JsonResponse({'sentiment': sentiment, 'text': text})
