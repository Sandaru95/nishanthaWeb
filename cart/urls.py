from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('order_complete/', views.OrderCompleteView.as_view(), name="order_complete"),
    path('wishlist/', views.WishlistView.as_view(), name="wishlist"),
    path('checkout/', views.CheckoutView.as_view(), name="checkout"),
]