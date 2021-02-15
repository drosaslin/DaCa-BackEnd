from .serializers import TravelReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import TravelReview
import jwt

class TokenView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response(request.user.username)

class TravelReviewCreateView(generics.ListCreateAPIView):
    queryset = TravelReview.objects.all()
    serializer_class = TravelReviewSerializer

class TravelReviewRetrieveView(generics.ListAPIView):
    serializer_class = TravelReviewSerializer
    lookup_field = 'username_id'

    def get_queryset(self):
        return TravelReview.objects.filter(username_id=self.kwargs[self.lookup_field])