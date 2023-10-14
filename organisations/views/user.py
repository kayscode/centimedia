from django.shortcuts import render, redirect
from organisations.forms import CreateUserForm, DeleteUserForm, UpdateUserForm
from organisations.repositories.user import UserRepository

from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url

user_repository = UserRepository()


# @login_required(login_url=resolve_url("login"))
def user_list(request):
    if request.method == "GET":
        context = {
            "users": user_repository.find_all()
        }

        return render(request, "", context)


# @login_required(login_url=resolve_url("login"))
def show_user(request, user_id):
    if request.method == "GET":
        user = user_repository.find_one(user_id)

        context = {
            "user": user
        }

        return render(request, "", user)


# @login_required(login_url=resolve_url("login"))
def update_user(request, user_id):
    if request.method == "GET":
        pass
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST)

        if user_form.is_valid():
            update_user_data = user_form.clean()
            user = user_repository.find_one(user_id)

            if user:
                user_repository.update(user_id, user)
                # redirect to the show user
                return redirect("")

            return render(request, "")

        # if form is not valid
        return render(request, "")


# @login_required(login_url=resolve_url("login"))
def create_user(request):
    user_form = CreateUserForm()
    context = {
        "user_form": user_form
    }
    return render(request, "", context)


# @login_required(login_url=resolve_url("login"))
def store_user(request):
    if request.method == "POST":

        user_form = CreateUserForm(request.POST)

        if user_form.is_valid():
            user = user_form.clean()
            user_repository.create(user)

            return render(request, "")


# @login_required(login_url=resolve_url("login"))
def delete_user(request):
    if request.method == "POST":
        user_deletion_form = DeleteUserForm(request.POST)

        if user_deletion_form.is_valid():
            user = user_deletion_form.cleaned_data
            user_repository.delete(user.id)

            return redirect("")
