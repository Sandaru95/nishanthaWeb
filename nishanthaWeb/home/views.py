from django.views.generic.base import TemplateView, View
from django.shortcuts import render, HttpResponse
from django.forms.models import model_to_dict
import json

from .models import NewsletterEmail
from authors.models import Author
from publishers.models import Publisher

class IndexView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # Author List
        author_list = []
        for author in Author.objects.all():
            author_list.append({ 'name': author.name, 'name_sinhala': author.name_sinhala, 'address': author.address, 'tel': author.tel })
        context['author_list'] = json.dumps(author_list)
        # Publisher List
        publisher_list = []
        for publisher in Publisher.objects.all():
            publisher_list.append({ 'title': publisher.title, 'title_sinhala': publisher.title_sinhala, 'logo': publisher.logo.url})
        context['publisher_list'] = json.dumps(publisher_list)
        return context

class AddToNewslettersView(View):
    def post(self, request):
        nl_email = NewsletterEmail()
        nl_email.email = request.POST['email']
        nl_email.save()
        return HttpResponse("success")