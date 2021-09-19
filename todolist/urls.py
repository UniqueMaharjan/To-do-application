from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus/", views.Aboutus, name="aboutus"),
    path("task/", views.createForm, name="tasks"),
    path("edit/<str:pk>/", views.editForm, name="edit"),
    path("delete/<str:pk>/", views.deleteForm, name="delete"),
]
