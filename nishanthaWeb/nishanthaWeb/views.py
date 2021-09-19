from django.views.generic.base import RedirectView

class HomeRedirectView(RedirectView):
    pattern_name = "home:index"