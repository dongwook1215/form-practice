from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Your ID",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "register-control"}),
    )
    password1 = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "register-control"}),
    )
    password2 = forms.CharField(
        label="Password confirm",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "register-control"}),
        help_text="Write the same password",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "register-control"})
    )
    profile = forms.ImageField(widget=forms.FileInput())


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Your ID",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "login-control"}),
    )
    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "login-control"}),
    )

