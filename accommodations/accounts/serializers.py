from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """User Model serializer class."""

    class Meta:
        model = User
        fields = ('id', 'username', 'appuser_picture')
