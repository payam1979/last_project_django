from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your models here.

class UserCreationForm(UserCreationForm):
    email = models.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class AuthenticationForm(AuthenticationForm):
    email = models.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']