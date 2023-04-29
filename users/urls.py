from django.urls import path, include


app_name = "users"
urlpatterns = [
    # Default Authorization URL
    path("", include("django.contrib.auth.urls"))
]
