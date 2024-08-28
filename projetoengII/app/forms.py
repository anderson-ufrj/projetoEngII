from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['cliente', 'pratos', 'status', 'data_entrega']
        widgets = {
            'data_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
