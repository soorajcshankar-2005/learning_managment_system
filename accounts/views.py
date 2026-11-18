from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from accounts.serializers import UserSeraializer

# Create your views here.
class UserCreateView(CreateAPIView):
    serializer_class=UserSeraializer
