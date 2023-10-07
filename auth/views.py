from django.shortcuts import render, redirect, resolve_url
from auth.forms import LoginForm, LogoutForm
from organisations.repositories.user import UserRepository

from django.contrib.auth import login, logout

# Create your views here.

user_repository = UserRepository()


def authentication(request):
    if request.method == "GET":
        login_form = LoginForm()
        context = {
            "form": login_form
        }
        return render(request, "", context)

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            try:
                user = user_repository.find_by_username(login_form.cleaned_data.get("username"))
                login(request, user)
                return redirect(resolve_url("admin-dashboard"))
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


def sign_out(request):
    logout(request)
    return redirect(resolve_url("login"))
