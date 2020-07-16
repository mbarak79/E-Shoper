from django.urls import path
from .views import index, shop, cart, checkout

app_name = 'store'

urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]
