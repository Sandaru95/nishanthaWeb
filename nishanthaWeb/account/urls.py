from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),

    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("register/verification/", views.RegisterVerificationView.as_view(), name="register_verification"),
]