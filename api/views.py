from .serializers import CreateTravelReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import TravelReview
import jwt

class TokenView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        secret = 'secret'
        encoded_jwt = jwt.encode({'user': 'drosaslin', 'role': 'admin'}, secret, algorithm='HS256')

        return Response(encoded_jwt)

class TravelReviewView(generics.ListCreateAPIView):
    queryset = TravelReview.objects.all()
    serializer_class = CreateTravelReviewSerializer
