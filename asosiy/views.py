from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.db.models import Avg
from django.utils import timezone

class JustHome(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class HomeView(View):
    def get(self, request):
        content = {
            'bolimlar' : Bolim.objects.all()[:8]
        }
        return render(request, 'page-index.html', content)

class BolimlarView(View):
    def get(self, request):
        content = {
            "bolimlar" : Bolim.objects.all()
        }
        return render(request, 'page-category.html', content)

class MahsulotlarView(View):
    def get(self, request, pk):
        content = {
            "mahsulotlar" : Mahsulot.objects.filter(bolim = pk)
        }
        return render(request, 'page-listing-grid.html', content)

class MahsulotView(View):
    def get(self, request, pk):
        izohlar = Izoh.objects.filter(mahsulot=pk)
        ortachasi = izohlar.aggregate(Avg("baho")).get("baho__avg")
        if ortachasi:
            ortachasi*=20
        else:
            ortachasi=0
        print(ortachasi)
        content = {
            "mahsulot" : Mahsulot.objects.get(id = pk),
            'ortachasi' : ortachasi,
            'izohlar' : Izoh.objects.filter(mahsulot = Mahsulot.objects.get(id = pk))
        }
        return render(request, 'page-detail-product.html', content)

    def post(self, request, pk):
        Izoh.objects.create(
        profil = request.user,
        mahsulot = Mahsulot.objects.get(id=pk),
        matn = request.POST.get('comment'),
        baho = request.POST.get('rating'),
        sana = timezone.now()
        )
        return redirect(f'/main/mahsulot/{pk}')
