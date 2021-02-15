from django.urls import path
from .views import TokenView, TravelReviewCreateView, TravelReviewRetrieveView
urlpatterns = [
    path('tk', TokenView.as_view()),
    path('travel/', TravelReviewCreateView.as_view()),
    path('travel/<str:username_id>/', TravelReviewRetrieveView.as_view()),
]