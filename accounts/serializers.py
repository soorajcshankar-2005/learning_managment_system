from rest_framework import serializers
from accounts.models import User

class UserSeraializer(serializers.ModelSerializer):
    class Meta:
        model=User

        fields=["username","email","password","phone","role"]


