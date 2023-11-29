from django.urls import path, include
from .views import IndexView, UsersViewSet, CategoryViewSet
from rest_framework import routers




router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/v1/', include(router.urls), name='users'),
    path('api/v1/', include(router.urls), name='category'),
]
