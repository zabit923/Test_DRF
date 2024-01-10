from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer

from .models import News, Category, User

class NewsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')
        ref_name = 'UserCreateSerializer'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'is_superuser', 'email', 'is_staff', 'date_joined',
            'image'
        )
        ref_name = 'UserSerializer'
