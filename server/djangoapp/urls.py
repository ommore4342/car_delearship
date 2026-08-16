from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Auth
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='register'),

    # Cars
    path('get_cars', views.get_cars, name='get_cars'),

    # Dealers
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),

    # Reviews
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review', views.add_review, name='add_review'),

    # Sentiment
    path('analyze_review/<str:text>', views.analyze_review_sentiment, name='analyze_review'),
]
