import contact
from django.views.generic.base import TemplateView, View
from django.shortcuts import HttpResponse, render

from .models import ContactMessage

class IndexView(TemplateView):
    template_name = "contact/index.html"

class CreateMessageView(View):
    def post(self, request):
        contact_message = ContactMessage()
        contact_message.sender_name = request.POST['sender_name']
        contact_message.sender_tel = request.POST['sender_tel']
        contact_message.sender_message = request.POST['sender_message']
        contact_message.save()
        return HttpResponse("success")
