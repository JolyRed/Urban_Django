from django.contrib import admin
from django.urls import path
from task5.views import sign_up_by_django, sign_up_by_html
from task4.views import main_page, cart_page, shop_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('html_sign_up/', sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up/', sign_up_by_django, name='sign_up_by_django'),
    path('main_page/', main_page, name='main_page'),
    path('cart_page/', cart_page, name='card_page'),
    path('shop_page/', shop_page, name='shop_page')

]