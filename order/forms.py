from django import forms
from django.forms import ModelForm

from .models import Order

class OrderUpdate(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('end_at', 'plated_end_at')       
        widgets = {
            'end_at': forms.DateTimeInput(attrs={'class':'form-control'}),
            'plated_end_at': forms.DateTimeInput(attrs={'class':'form-control'}),
        }  
        

