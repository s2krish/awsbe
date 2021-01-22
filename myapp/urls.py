# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<str:room_name>/', views.room, name='room'),
]