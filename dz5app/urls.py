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

app_name = 'dz5app'

urlpatterns = [
    path('clients/', views.client_list, name='clients'),
    path('products/', views.product_list, name='products'),
    path('orders/', views.orders_list, name='orders'),
]