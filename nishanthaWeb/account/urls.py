from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login_register/", views.LoginRegisterView.as_view(), name="login_register"),
]