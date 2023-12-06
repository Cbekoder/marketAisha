import random
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .models import Profil
from eskiz.client import SMSClient
from django.contrib.auth import login, logout, authenticate

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        profil = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        if profil is  None:
            return redirect("/user/login")
        return redirect('/main/home/')



class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        profil = Profil.objects.create_user(
            username = request.POST.get('tel'),
            password = request.POST.get('psw'),
            tel = request.POST.get('tel'),
            first_name = request.POST.get('ism'),
            last_name = request.POST.get('familya'),
            davlat = request.POST.get('davlat'),
            shahar = request.POST.get('shahar'),
            jins = request.POST.get('gender'),
            tasdiqlash_kodi = str(random.randrange(100000, 999999))
        )
        mijoz = SMSClient(
            api_url = "https://notify.eskiz.uz/api/",
            email = settings.ESKIZ_GMAIL,
            password = settings.ESKIZ_PAROL,
        )
        mijoz._send_sms(
            phone_number=profil.tel,
            message=f"""Aisha loyihasi uchun taqsdiqlash kodingiz:
{profil.tasdiqlash_kodi}
            """
        )
        login(request, profil)
        return redirect('/user/confirm')

class ConfirmView(View):
    def get(self, request):
        return render(request, 'confirm.html')
    def post(self, request):
        profil = Profil.objects.get(id = request.user.id)
        print(profil)
        if profil.tasdiqlash_kodi == request.POST.get('confirm'):
            profil.tasdiqlangan = True
            profil.save()
            return redirect('/user/login/')
        return redirect("/user/confirm")