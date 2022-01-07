from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.loginUser,name = "login"),
    path("signup/",views.registerUser,name = "signup"),
    path("logout/",views.logoutUser,name = "logout"),
    path("create/", views.createTask, name="create"),
    path("edit/<int:pk>/", views.editTask, name="edit"),
    path("delete/<int:pk>/", views.deleteTask, name="delete"),
    path("editprofile/", views.editUser, name="editprofile"),
]
