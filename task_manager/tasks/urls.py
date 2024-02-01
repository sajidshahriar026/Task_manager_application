from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("details", views.details, name="details"),
    path("signin", views.signin, name="signin")
]
