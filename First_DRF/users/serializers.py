from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Users, Category


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'title', 'content', 'is_published', 'cat')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
