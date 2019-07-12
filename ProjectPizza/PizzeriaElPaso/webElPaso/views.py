from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product, SizeProduct, Bill, Detail
from .Cart import Cart
from .forms import CartAddProductForm, OrderCreateForm
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db import IntegrityError, transaction

# Create your views here.
def index(request):
    listProduct = Product.objects.all()
    size = SizeProduct.objects.all()
    cart_Form= CartAddProductForm()
    context = {
        'listProduct' : listProduct,
        'sizeProduct' : size,
        'form': cart_Form,
    }
    return render(request, 'webElPaso/index.html', context)

def contact(request):
    return render(request, 'webElPaso/contact.html')

def nosotros(request):
    return render(request, 'webElPaso/nosotros.html')

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        prueba = request.POST['selectTam']
        sizes = SizeProduct.objects.get(product=product_id, size=int(request.POST['selectTam']))
        cd = form.cleaned_data
        s = float(sizes.price) * int(cd['quantity'])
        print(s)
        cart.add(prod=product, size=sizes, quantity=int(cd['quantity']), price=float(s))
    return redirect('index')

def carShop(request):
    cart = Cart(request)
    context = {
        'listProduct' : cart,
        'message': '',
        'x': 0,
    }
    return render(request, 'webElPaso/cart.html', context)

def createBill(request):
    try:
        cart = Cart(request)
        b = Bill.objects.create(client=None, BillDate=timezone.now())
        b.save()
        for item in cart:
            p = Product.objects.get(id=int(item['product'].id))
            d = Detail.objects.create(bill=b, Product=p, price=item['price'], size=item['sizes'], quantity=item['quantity'])
            d.save()
        cart.clear()
        context = {
            'message': 'Ha realizado correctamente su compra',
        }   
        return render(request, 'webElPaso/create.html', context)
    except:
        cart = Cart(request)
        print('asd')
        context = {
            'listProduct' : cart,
            'message': 'Ha ocurrido un error correctamente su compra',
        }
        return redirect('cart')

        