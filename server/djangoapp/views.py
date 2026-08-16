import json
import logging

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CarMake, CarModel, Dealer, Review
from .populate import initiate, seed_dealers

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────
# Sentiment (local — no Flask service needed)
# ─────────────────────────────────────────────────────────────

POSITIVE_WORDS = [
    'great', 'excellent', 'fantastic', 'amazing', 'wonderful', 'awesome',
    'outstanding', 'superb', 'perfect', 'best', 'love', 'happy', 'satisfied',
    'recommend', 'helpful', 'friendly', 'professional', 'efficient', 'smooth',
    'quick', 'honest', 'fair', 'nice', 'good', 'pleased', 'delighted',
    'impressive', 'top', 'exceptional', 'incredible', 'brilliant', 'terrific',
]
NEGATIVE_WORDS = [
    'bad', 'terrible', 'awful', 'horrible', 'worst', 'poor', 'disappointed',
    'disappointing', 'unhappy', 'upset', 'rude', 'unprofessional', 'slow',
    'overpriced', 'expensive', 'waste', 'avoid', 'never', 'problem', 'issue',
    'wrong', 'broken', 'defective', 'frustrating', 'annoying', 'dishonest',
    'scam', 'fraud', 'lied', 'deceived', 'regret', 'mistake',
]


def _sentiment(text):
    t = (text or '').lower()
    pos = sum(1 for w in POSITIVE_WORDS if w in t)
    neg = sum(1 for w in NEGATIVE_WORDS if w in t)
    if pos > neg:
        return 'positive'
    if neg > pos:
        return 'negative'
    return 'neutral'


# ─────────────────────────────────────────────────────────────
# Auth
# ─────────────────────────────────────────────────────────────

@csrf_exempt
def login_user(request):
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
    username = request.user.username if request.user.is_authenticated else 'anonymous'
    logout(request)
    return JsonResponse({'userName': username, 'status': 'Logged out'})


@csrf_exempt
def registration(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body)
    username   = data.get('userName')
    password   = data.get('password')
    first_name = data.get('firstName', '')
    last_name  = data.get('lastName', '')
    email      = data.get('email', '')

    if User.objects.filter(username=username).exists():
        return JsonResponse({'userName': username, 'error': 'Already registered'}, status=400)

    user = User.objects.create_user(
        username=username, first_name=first_name,
        last_name=last_name, email=email, password=password,
    )
    login(request, user)
    return JsonResponse({'userName': username, 'status': 'Registered'})


# ─────────────────────────────────────────────────────────────
# Cars
# ─────────────────────────────────────────────────────────────

def get_cars(request):
    if CarMake.objects.count() == 0:
        initiate()
    makes = CarMake.objects.prefetch_related('car_models').all()
    cars  = []
    for make in makes:
        for model in make.car_models.all():
            cars.append({'CarMake': make.name, 'CarModel': model.name,
                         'CarType': model.car_type, 'Year': model.year})
    return JsonResponse({
        'CarMakes': [{'name': m.name, 'description': m.description} for m in makes],
        'Cars': cars,
    })


# ─────────────────────────────────────────────────────────────
# Dealers  (served directly from SQLite)
# ─────────────────────────────────────────────────────────────

def _ensure_dealers():
    """Seed dealers on first request if table is empty."""
    if Dealer.objects.count() == 0:
        seed_dealers()


def get_dealerships(request, state='All'):
    """GET /djangoapp/get_dealers          → all dealers
       GET /djangoapp/get_dealers/<state>  → filtered by state"""
    _ensure_dealers()
    qs = Dealer.objects.all()
    if state and state != 'All':
        qs = qs.filter(state__iexact=state)
    dealers = [d.to_dict() for d in qs.order_by('state', 'city')]
    return JsonResponse({'status': 200, 'dealers': dealers})


def get_dealer_details(request, dealer_id):
    """GET /djangoapp/dealer/<id>"""
    _ensure_dealers()
    try:
        dealer = Dealer.objects.get(pk=dealer_id)
        return JsonResponse({'status': 200, 'dealer': dealer.to_dict()})
    except Dealer.DoesNotExist:
        return JsonResponse({'status': 404, 'error': 'Dealer not found'}, status=404)


# ─────────────────────────────────────────────────────────────
# Reviews  (served directly from SQLite)
# ─────────────────────────────────────────────────────────────

def get_dealer_reviews(request, dealer_id):
    """GET /djangoapp/reviews/dealer/<id>"""
    _ensure_dealers()
    reviews = Review.objects.filter(dealer_id=dealer_id)
    result  = []
    for r in reviews:
        d = r.to_dict()
        d['sentiment'] = _sentiment(r.review)
        result.append(d)
    return JsonResponse({'status': 200, 'reviews': result})


@csrf_exempt
def add_review(request):
    """POST /djangoapp/add_review"""
    if not request.user.is_authenticated:
        return JsonResponse({'status': 401, 'error': 'Unauthorized'}, status=401)
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    data   = json.loads(request.body)
    rev    = data.get('review', {})
    dealer_id = rev.get('dealership')

    try:
        dealer = Dealer.objects.get(pk=dealer_id)
    except Dealer.DoesNotExist:
        return JsonResponse({'status': 404, 'error': 'Dealer not found'}, status=404)

    review = Review.objects.create(
        dealer        = dealer,
        name          = rev.get('name', request.user.username),
        review        = rev.get('review', ''),
        purchase      = rev.get('purchase', False),
        purchase_date = rev.get('purchase_date', ''),
        car_make      = rev.get('car_make', ''),
        car_model     = rev.get('car_model', ''),
        car_year      = rev.get('car_year', 2023),
    )
    d = review.to_dict()
    d['sentiment'] = _sentiment(review.review)
    return JsonResponse({'status': 200, 'result': d})


# ─────────────────────────────────────────────────────────────
# Sentiment endpoint
# ─────────────────────────────────────────────────────────────

def analyze_review_sentiment(request, text):
    """GET /djangoapp/analyze_review/<text>"""
    return JsonResponse({'sentiment': _sentiment(text), 'text': text, 'status': 200})
