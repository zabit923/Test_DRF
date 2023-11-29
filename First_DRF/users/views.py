from django.views.generic import TemplateView
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Users, Category
from .serializers import UsersSerializer, CategorySerializer




class IndexView(TemplateView):
    template_name = 'index.html'


class UsersViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    # def get_queryset(self):



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



