from django.urls import path
from .views import *

urlpatterns = [
    path('tanlanganlar/', TanlanganView.as_view()),
    path('savat/', SavatView.as_view()),
]