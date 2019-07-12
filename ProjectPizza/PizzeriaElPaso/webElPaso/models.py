from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=250)
    photo = models.ImageField(upload_to = 'webElPaso', blank = True)

class SizeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    PIZZA_SIZES = (
        ('4','Personal'),
        ('6', 'Pequeño'),
        ('8', 'Mediano'),
        ('12', 'Grande'),
        ('16', 'Familiar'),
    )
    size = models.CharField(max_length=2, choices=PIZZA_SIZES)
    price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)

class Client(models.Model):
    name = models.CharField(max_length = 15)
    lastName = models.CharField(max_length = 8)
    phoneNumber = models.CharField(max_length=8)
    direction = models.CharField(max_length = 250)

class Bill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True)
    BillDate =models.DateTimeField()

class Detail(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    Product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    size = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField()