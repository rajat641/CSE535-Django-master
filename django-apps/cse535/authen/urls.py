from django.urls import path
from . import views

urlpatterns = [
path("login/", views.login.as_view(), name="login"),
path("signup/", views.signup.as_view(), name="signup"),
path("group_save/", views.group_save.as_view(), name="group_save"),## To save all groups in the database
]
