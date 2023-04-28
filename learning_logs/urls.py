"""Определяет схемы URL для learning_logs"""

from django.urls import path

from . import views


app_name = "learning_logs"
urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    # Topics Page
    path("topics/", views.topics, name="topics"),
    # Concrete Topic Page
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # New Topic Page
    path("new_topic/", views.new_topic, name="new_topic"),
    # New Entry Page
    path("new_entry<int:topic_id>/", views.new_entry, name="new_entry"),
]
