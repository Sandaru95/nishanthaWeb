from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create_message/', views.CreateMessageView.as_view(), name="create_message"),
]