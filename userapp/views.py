from django.shortcuts import render
from django.views import View
from django.conf import settings
from .models import Profil

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        profil = Profil.objects.create(
            username = request.POST.get('tel'),
            password = request.POST.get('psw'),
            username = request.POST.get('tel'),
        )

class ConfirmView(View):
    def get(self, request):
        return render(request, 'confirm.html')