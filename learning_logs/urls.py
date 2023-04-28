"""Определяет схемы URL для learning_logs"""

from django.urls import path

from . import views


app_name = "learnign_logs"
urlpatterns = [path("", views.index, name="index")]
