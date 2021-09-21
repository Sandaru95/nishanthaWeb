from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings

from .views import HomeRedirectView

app_name = "nishanthaWeb"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeRedirectView.as_view()),

    path('account/', include('account.urls')),
    path('home/', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('cart/', include('cart.urls')),
    path('books/', include('books.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
