from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/<int:pk>/", views.blog, name="blog"),
    path("blogs/<int:pk>/edit/", views.editblog, name="editblog"),
    path("blogs/<int:pk>/delete/", views.deleteblog, name="deleteblog"),
]