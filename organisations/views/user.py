from django.shortcuts import render, redirect, reverse
from organisations.forms import DeleteUserForm, UpdateUserForm, AdminCreateUserForm, AdminUpdateUserForm
from organisations.repositories.user import UserRepository

from organisations.models import User

from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url

user_repository = UserRepository()


# @login_required(login_url=resolve_url("login"))
def user_list(request):
    if request.method == "GET":
        context = {
            "users": user_repository.find_all()
        }

        return render(request, "organisations/users/list_users.html", context)


# @login_required(login_url=resolve_url("login"))
def show_user(request, user_id):
    if request.method == "GET":
        user = user_repository.find_one(user_id)

        context = {
            "user": user
        }

        return render(request, "organisations/users/user_detail.html", user)


# @login_required(login_url=resolve_url("login"))
def update_user(request, user_id):
    if request.user is not None and request.user.is_authenticated:
        if request.method == "GET":
            try:
                user = UserRepository.find_one(user_id)

                if request.user.is_super_admin is True:
                    user_form = AdminUpdateUserForm(user.to_json)
                else:
                    user_form = UpdateUserForm(user.to_json)

                context = {
                    "form": user_form
                }
                return render(request, "organisations/users/edit_user.html", context)
            except User.DoesNotExist:

                return render(request, "errors/404.html")
        if request.method == "POST":
            is_admin = False

            if request.user.is_super_admin is True:
                user_form = AdminUpdateUserForm(request.POST)
                is_admin = True
            else:
                user_form = UpdateUserForm(request.POST)

            if user_form.is_valid():

                try:
                    if is_admin:
                        UserRepository.update_as_admin(
                            user_form.cleaned_data.get("id"),
                            user_form.cleaned_data
                        )
                    else:
                        UserRepository.update_as_manager(
                            user_form.cleaned_data.get("id"),
                            user_form.cleaned_data
                        )

                except User.DoesNotExist:
                    return render(request, "errors/404.html")

                return redirect(reverse("show_user", kwargs={"user_id": user_id}))

                # return render(request, "")

            context = {
                "form": user_form
            }

            return render(request, "organisations/users/edit_user.html", context)
    else:
        return redirect(reverse("auth_login"))


# @login_required(login_url=resolve_url("login"))
def create_user(request):
    if request.user is not None and request.user.is_authenticated:
        if request.user.is_super_admin is True:
            user_form = AdminCreateUserForm()
            context = {
                "user_form": user_form
            }
            return render(request, "organisations/users/create_user.html", context)
    else:
        return redirect(reverse("auth_login"))


# @login_required(login_url=resolve_url("login"))
def store_user(request):
    if request.user is not None and request.user.is_authenticated:
        if request.user.is_super_admin is True:
            if request.method == "GET":
                user_form = AdminCreateUserForm()
                context = {
                    "user_form": user_form
                }
                return render(request, "organisations/users/create_user.html", context)
            if request.method == "POST":

                user_form = AdminCreateUserForm(request.POST)

                if user_form.is_valid():
                    user = user_repository.create(user_form.cleaned_data)

                    return redirect(reverse("show_user", kwargs={"user_id": user.id}))
                context = {
                    "user_form": user_form
                }
                return render(request, "organisations/users/create_user.html", context)
    else:
        return redirect(reverse("auth_login"))


# @login_required(login_url=resolve_url("login"))
def delete_user(request):
    if request.method == "POST":
        user_deletion_form = DeleteUserForm(request.POST)

        if user_deletion_form.is_valid():
            user = user_deletion_form.cleaned_data
            user_repository.delete(user.id)

            return redirect("")
