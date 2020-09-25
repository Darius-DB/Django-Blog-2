from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Password'}),
            'password2': forms.Textarea(attrs={'placeholder': 'Enter password again'}),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['image']
