from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/create/', views.createBill, name='order_create'),
    path('cart/', views.carShop, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('nosotros/', views.nosotros, name='nosotros')
   #path('contact/',  , name='contact')
]

