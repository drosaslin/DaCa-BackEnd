from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)
    gender = serializers.CharField(max_length=6, required=True)
    birthday = serializers.DateField(required=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.gender = self.validated_data.get('gender', '')
        user.birthday = self.validated_data.get('birthday', '')
        user.save(update_fields=['first_name', 'last_name', 'gender', 'birthday'])