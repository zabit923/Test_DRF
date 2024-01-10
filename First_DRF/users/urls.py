from django.urls import path, include, re_path
from .views import IndexView, NewsAPIList, NewsAPIUpdate, NewsAPIDestroy, CategoryAPIList, \
                   CategoryAPIUpdate, CategoryAPIDestroy



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/v1/news/', NewsAPIList.as_view()),
    path('api/v1/news/<int:pk>', NewsAPIUpdate.as_view()),
    path('api/v1/news_delete/<int:pk>', NewsAPIDestroy.as_view()),

    path('api/v1/category/', CategoryAPIList.as_view()),
    path('api/v1/category/<int:pk>', CategoryAPIUpdate.as_view()),
    path('api/v1/category_delete/<int:pk>', CategoryAPIDestroy.as_view()),

    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]


