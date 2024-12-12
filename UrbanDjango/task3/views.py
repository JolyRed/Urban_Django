# task3/views.py
from django.shortcuts import render

def main_page(request):
    return render(request, 'third_task/main_page.html')

def shop_page(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077']}

    return render(request, 'third_task/shop_page.html', {'context': context})

def cart_page(request):
    return render(request, 'third_task/cart_page.html')
