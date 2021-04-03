from django import forms
from django.forms import ModelForm

from .models import Author
from book.models import Book

class AddBookInfo(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'description', 'count')
        labels = {
            'name': ' Book name:',
            'description': 'Counts:',
            'count': ' Description:',
        }        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
            'count': forms.NumberInput(attrs={'class':'form-control'}),
        }  
        

