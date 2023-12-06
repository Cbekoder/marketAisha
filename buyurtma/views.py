from django.shortcuts import render, redirect
from django.views import View
from .models import *
class TanlanganView(View):
    def get(self, request):
        content = {
            'tanlanganlar' : Tanlangan.objects.filter(profil = request.user)
        }
        return render(request, 'page-profile-wishlist.html', content)

class BuyurtmalarVeiw(View):
    def get(self, request):
        return render(request, 'page-profile.order.html')

class SavatView(View):
    def get(self, request):
        savati = Savat.objects.filter(profil=request.user)
        if savati.exists():
            savati = savati.first()
        else:
            savati = Savat.objects.create(profil = request.user)
        itemlar = SavatItem.objects.filter(savat=savati)
        chegirma = 0
        for item in itemlar:
            chegirma += (item.mahsulot.narx + item.mahsulot.chegirma)//100
        content = {
            'savat' : savati,
            'itemlar' : itemlar,
            'chg' : chegirma,
            'sum' : savati.total_sum +chegirma,
            'yakumiy' : savati.total_sum
        }
        return render(request, 'page-shopping-cart.html', content)


class MiqdorQosh(View):
    def get(self, request):
        item = SavatItem.objects.get(id=pk)
        item.miqdor += 1
        item.save()
        return redirect('order/savat/')