from django.shortcuts import redirect, render, HttpResponse
from django.views.generic.base import View, TemplateView

import requests
import json
from random import randint

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm
 
from .functions.emaill_function import py_mail, py_mail_verifycode

class IndexView(TemplateView):
    template_name = "account/index.html"

class LoginView(View):
    template_name = "account/login.html"

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Hello World This is me!")
            login(request, user)
            return redirect('home:index')
        else:
            return render(request, self.template_name, {})

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('home:index')   
        else:
            return redirect('home:index')

class RegisterView(View):
    template_name = "account/register.html"

    def get(self, request):
        form = CreateUserForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = CreateUserForm(request.POST)

        # Getting Recaptcha Response
        recaptcha_post_data = request.POST['g-recaptcha-response']
        recaptcha_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {'secret':'6LftNnkcAAAAAHH-aD1in1OwXrLzvdpvOD2QekGu', 'response': recaptcha_post_data})
        print(f"RECAPTCHA STATUS: {json.loads(recaptcha_response.text)}")

        if form.is_valid():
            form.save()
            messages.success(request, "Account was created. Please login to proceed.")
            # Sending an Email
            username = form.cleaned_data['username']
            py_mail(request.POST['email'], username)

            return redirect("account:login")
        else:
            form = CreateUserForm()
            return render(request, self.template_name, {'form': form})

class RegisterVerificationView(View):
    magic_number = randint(0, 15000)

    def post(self, request):
        py_mail_verifycode(request.POST['email'], request.POST['username'], self.magic_number)
        return HttpResponse(str(self.magic_number))