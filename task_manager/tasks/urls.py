from django.contrib.auth.decorators import login_required
from django.urls import path, include


from . import views

app_name = "tasks"

urlpatterns = [
    path("", login_required(views.IndexView.as_view()), name="index"),
    path("details/<int:pk>", login_required(views.DetailView.as_view()), name="details"),
    path("update/<int:task_id>", views.update, name="update"),
    path("delete_image/<int:image_id>", views.delete_image, name="delete_image"),
    path("delete/<int:task_id>", views.delete, name='delete'),
    path("search", views.search, name='search'),
    path("filter", views.filter, name='filter'),
    path("create", views.create, name="create"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout, name="logout"),
]
