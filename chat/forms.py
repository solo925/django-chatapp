from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(label="password",widget=forms.PasswordInput())
    
    
class RoomForm(forms.ModelForm):
    
    class Meta:
        model = ChatRoom
        fields = '__all__'
