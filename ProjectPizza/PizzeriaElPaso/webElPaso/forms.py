from django import forms
from .models import SizeProduct, Bill

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Cantidad ')


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['client', 'BillDate']
