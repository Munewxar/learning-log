from django.urls import path, include

from . import views


app_name = "users"
urlpatterns = [
    # Default Authorization URL
    path("", include("django.contrib.auth.urls")),
    # Registration Page
    path("register/", views.register, name="register"),
]
