from django.urls import path, re_path, include

from .views import index, article, newest, create

urlpatterns = [
    path('', index, name='home'),
    path('newest/', newest, name='new'),
    path('article-<int:id>/', article, name='article'),
    path('create/', create, name='create'),
]