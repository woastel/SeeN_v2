from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

def about_view(request):
    return render(request, "about.html")

def login_view(request):
    # print(request.user.is_authenticated())
    next_side = request.GET.get('next')
    titel = "User Login"
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        # print(request.user.is_authenticated())
        if next_side:
            return redirect(next_side)
        return redirect("overview:home")
    context = {
        "form": form,
        "titel": titel
    }
    return render(request, "accounts/login_form.html", context)

def register_view(request):
    # print(request.user.is_authenticated())
    next_side = request.GET.get('next')
    titel ="User Registration"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next_side:
            return redirect(next_side)
        return redirect("overview:home")
        # return

    context = {
        "form": form,
        "titel": titel
    }
    return render(request, "accounts/registration_form.html", context)

def logoout_view(request):
    titel = "User Logout"
    template = "accounts/logout.html"
    current_user = request.user
    context = {
        "username": current_user.username,
        "titel" : titel
        }
    logout(request)
    return render(request, template, context)
