from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "account/index.html"

class LoginRegisterView(TemplateView):
    template_name = "account/login_register.html"