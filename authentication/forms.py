from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import CustomUser

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
            label='Password:', 
            widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'**********'}))  
    password2 = forms.CharField(
            label='Confirm password:', 
            widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'**********'}))  
    
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'middle_name', 'last_name']
        labels = {
            'email': 'Email:',
            'first_name': 'First name:',
            'middle_name': 'Last name:',
            'last_name': 'Middle name:',
        }        
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'you@example.com'}),
            'first_name': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'middle_name': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'last_name': forms.TextInput(attrs={'class':'form-control mb-2'}),
        }        
    
class UserLoginForm(forms.Form):
        email = forms.EmailField(
            label='User email:', 
            widget=forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'you@example.com'}))
        password = forms.CharField(
            label='Password:', 
            widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'**********'}))

