from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserDetail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['id','username','password','mobile_number']

