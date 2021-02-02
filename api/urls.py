from django.urls import path
from .views import TokenView, TravelReviewView

urlpatterns = [
    path('tk', TokenView.as_view()),
    path('travel', TravelReviewView.as_view()),
]