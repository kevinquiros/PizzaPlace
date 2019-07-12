from .models import Product, SizeProduct
from django.conf import settings
from decimal import Decimal

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, prod, size, quantity, price):
        prod_id = str(prod.id)
        if prod_id not in self.cart:
            print('holas')
            self.cart[prod_id] = {'quantity': quantity, 'sizes': str(size.size) , 'price': float(price)}
        else:
            self.cart[prod_id]['quantity'] += quantity 
        self.save() 

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def __str__(self):
        return "id" + str(self.idP) + "quantity: " + str(self.quantity)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
