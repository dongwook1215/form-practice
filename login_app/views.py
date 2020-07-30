from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import User_Info

from .forms import RegisterForm, LoginForm

# Create your views here.


def start(request):
    return redirect("/login_app/login/")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data["password1"] == form.cleaned_data["password2"]:
                user = User.objects.create_user(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password1"],
                    email=form.cleaned_data["email"],
                )
                user_info = User_Info()
                user_info.user = user
                try:
                    user_info.profile = form.cleaned_data["profile"]
                except:
                    pass
                user_info.save()
                return redirect("/login_app/login/")
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/blog_app/main/")
            else:
                form = LoginForm()
                return render(
                    request,
                    "login.html",
                    {"message": "username or password is incorrect.", "form": form},
                )
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})

