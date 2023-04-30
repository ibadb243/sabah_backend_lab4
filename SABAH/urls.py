from django.urls import path, re_path, include

from .views import controller, article

urlpatterns = [
    path('', controller),
    path('article-<int:id>/', article),
]
