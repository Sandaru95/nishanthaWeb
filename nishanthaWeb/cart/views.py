from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "cart/index.html"

class OrderCompleteView(TemplateView):
    template_name = "cart/order_complete.html"

class WishlistView(TemplateView):
    template_name = "cart/wishlist.html"