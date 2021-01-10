from django.urls import path
from .views import TokenView

urlpatterns = [
    path('tk', TokenView.as_view())
]