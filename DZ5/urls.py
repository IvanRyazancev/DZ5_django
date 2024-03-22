"""
URL configuration for DZ5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from itertools import product

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from DZ5 import settings
from dz5app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_product/', views.add_product, name='add_product'),
    path('success/', views.save_success, name='save-success'),
    path('client/<int:client_id>/orders/', views.client_orders, name='client_orders'),
    path('dz5app/', include('dz5app.urls')),
    path('', views.my_page, name='my_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
