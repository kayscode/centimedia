from django.shortcuts import render, redirect
from django.urls import reverse
from authentication.forms import LoginForm, LogoutForm
from organisations.repositories.user import UserRepository

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

user_repository = UserRepository()


def authentication(request):
    if request.method == "GET":
        login_form = LoginForm()
        context = {
            "form": login_form
        }
        return render(request, "auth/login.html", context)

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            try:
                user_data = login_form.cleaned_data.get("username")
                user = authenticate(username = user_data.get("username"),password=user_data.get("password"))
                login(request, user)
                return redirect(reverse("admin-dashboard"))
            except Exception as err:
                # redirect to error page
                context = {
                    "error": "user doesn't exist"
                }
                return render(request, "", context)
        context = {
            "form": login_form
        }
        return render(request, "",context)


@login_required()
def sign_out(request):
    logout(request)
    return redirect(reverse("login"))
