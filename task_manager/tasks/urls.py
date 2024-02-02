from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("details", views.details, name="details"),
    path("update", views.update, name="update"),
    path("create", views.create, name="create"),
    path("signin", views.signin, name="signin")
]
