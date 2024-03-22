from datetime import timezone, timedelta
from django.shortcuts import render, redirect
from dz5app.forms import ProductForm
from .models import Product, Order, Client
from datetime import timedelta
from django.utils import timezone

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('save-success')  # Перенаправление после сохранения
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def view_name(request):
    return render(request, 'success.html')

def save_success(request):
    return render(request, 'success.html')

def unique_products_from_orders(orders):
    unique_products = set()
    for order in orders:
        for item in order.orderitem_set.all():
            unique_products.add(item.product)
    return unique_products

def client_orders(request, client_id):
    now = timezone.now()
    client_orders_last_7_days = Order.objects.filter(client_id=client_id, date_ordered__gte=now - timedelta(days=7))
    client_orders_last_month = Order.objects.filter(client_id=client_id, date_ordered__gte=now - timedelta(days=30))
    client_orders_last_year = Order.objects.filter(client_id=client_id, date_ordered__gte=now - timedelta(days=365))

    products_last_7_days = unique_products_from_orders(client_orders_last_7_days)
    products_last_month = unique_products_from_orders(client_orders_last_month)
    products_last_year = unique_products_from_orders(client_orders_last_year)

    context = {
        'products_last_7_days': products_last_7_days,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year,
    }

    return render(request, 'client_products.html', context)

def my_page(request):

    return render(request, 'my_page.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def orders_list(request):
    orders = Order.objects.select_related('client').prefetch_related('products').all()
    return render(request, 'orders.html', {'orders': orders})