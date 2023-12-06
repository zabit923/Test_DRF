from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import News, Category, User
from .serializers import NewsSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly




class IndexView(TemplateView):
    template_name = 'index.html'

# __________________________________________________________________________________________

class NewsAPIList(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class NewsAPIUpdate(RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class NewsAPIDestroy(RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# __________________________________________________________________________________________

class CategoryAPIList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryAPIUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CategoryAPIDestroy(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)

# __________________________________________________________________________________________


