from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexView, name='index'),
    ]
