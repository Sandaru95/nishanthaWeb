from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('add_to_newsletters/', views.AddToNewslettersView.as_view(), name="add_to_newsletter"),
]