from django.contrib import admin
from .models import UserSignal, UserGoogle, UserFacebook, UserTwitter

admin.site.register(UserSignal)
admin.site.register(UserGoogle)
admin.site.register(UserFacebook)
admin.site.register(UserTwitter)