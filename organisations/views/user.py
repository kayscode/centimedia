from django.shortcuts import render, redirect
from ..forms import UserForm, UserDeletionForm
from ogranisations.repositories.user import UserRepository

user_repository = UserRepository()


def user_list(request):
    if request.method == "GET":
        context = {
            "users": user_repository.find_all()
        }

        return render(request, "", context)


def show_user(request, user_id):
    if request.method == "GET":
        user = user_repository.find_one(user_id)

        context = {
            "user": user
        }

        return render(request, "", user)


def update_user(request, user_id):
    if request.method == "PUT":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            update_user_data = user_form.clean()
            user = user_repository.find_one(user_id)

            if user:
                user_repository.update(user_id, user)
                # redirect to the show user
                return redirect("")

            return render(request, "")

        # if form is not valid
        return render(request,"")


def create_user(request):
    user_form = UserForm()
    context = {
        "user_form": user_form
    }
    return render(request, "", context)


def store_user(request):
    if request.method == "POST":

        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.clean()
            user_repository.create(user)

            return render(request, "")


def delete_user(request):
    if request.method == "POST":
        user_deletion_form = UserDeletionForm(request.POST)

        if user_deletion_form.is_valid():
            user = user_deletion_form.clean()
            user_repository.delete(user.user_id)

            return redirect("")
