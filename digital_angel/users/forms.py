from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# form that inherits from UserCreationForm and adds field 'email'
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
