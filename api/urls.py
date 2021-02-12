from django.urls import path
from .views import TokenView, TravelReviewCreateView
urlpatterns = [
    path('tk', TokenView.as_view()),
    path('travel/<str:travel>/', TravelReviewCreateView.as_view(), kwargs={'travel_id': None}),
    # path('travel/<str:travel_id>/', TravelReviewReadView.as_view()),
]