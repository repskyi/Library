from django import forms
from django.forms import ModelForm

from .models import Author
from book.models import Book

class AddAuthorInfo(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        labels = {
            'name': 'First name:',
            'surname': 'Last name:',
            'patronymic': 'Patronymic:',
        }        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'surname': forms.TextInput(attrs={'class':'form-control'}),
            'patronymic': forms.TextInput(attrs={'class':'form-control'}),
        }  
        
