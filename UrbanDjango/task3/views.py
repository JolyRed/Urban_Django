# task3/views.py
from django.shortcuts import render

def main_page(request):
    return render(request, 'third_task/main_page.html')

def shop_page(request):
    items = {
        'item1': 'Игровая приставка',
        'item2': 'Игровая мышь',
        'item3': 'Игровая клавиатура',
    }
    return render(request, 'third_task/shop_page.html', {'items': items})

def cart_page(request):
    return render(request, 'third_task/cart_page.html')
