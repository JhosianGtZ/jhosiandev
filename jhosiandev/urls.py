
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from portfolio import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path("portfolio/", include('portfolio.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
