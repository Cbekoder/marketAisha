from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import JustHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userapp.urls')),
    path('main/', include('asosiy.urls')),
    path('order/', include('buyurtma.urls')),
    path('', JustHome.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
