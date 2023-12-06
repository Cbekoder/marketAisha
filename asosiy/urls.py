from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('category/', BolimlarView.as_view(), name="bolimlar"),
    path('bolim/<int:pk>', MahsulotlarView.as_view(), name="mahsulotlar"),
    path('mahsulot/<int:pk>', MahsulotView.as_view(), name="mahsulot"),
]