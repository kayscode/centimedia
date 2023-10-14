from django.shortcuts import render, redirect, reverse

from media_manager.models import SourceMediaFile

# repositories
from media_manager.repositories import SourceMediaRepository, MediaFileRepository, NotificationsRepository
from organisations.repositories import OrganisationRepository

from media_manager.forms import ManagerCreateSourceMediaForm, ManagerUpdateSourceMediaForm, DeleteSourceMediaForm, \
    AdminCreateSourceMediaForm, AdminUpdateSourceMediaForm


def create_and_store_source(request):
    if request.user is not None and request.user.is_authenticated:
        if request.method == "GET":

            if request.user.is_super_admin:
                source_media_form = AdminCreateSourceMediaForm()
            else:
                source_media_form = ManagerCreateSourceMediaForm()

            context = {
                "source_media_form": source_media_form
            }

            return render(request, "", context)

        elif request.method == "POST":

            if request.user.is_super_admin:
                source_media_form = AdminCreateSourceMediaForm(request.POST)
            else:
                source_media_form = ManagerCreateSourceMediaForm(request.POST)

            if source_media_form.is_valid():
                if request.user.is_super_admin is False:
                    source_media_form.cleaned_data["organisation"] = request.user.organisation
                SourceMediaRepository.create(source_media_form.cleaned_data)
                return redirect(reverse("list_source"))
            else:
                context = {
                    "source_media": source_media_form
                }

                return render(request, "", context)
    else:
        return redirect(reverse("auth_login"))


def show_source(request, source_id):
    if request.user is not None and request.user.is_authenticated:
        if request.method == "GET":
            try:
                source = SourceMediaRepository.find_one(source_id)

                context = {
                    "source": source
                }
                return render(request, "", context)
            except SourceMediaFile.DoesNotExist:

                return redirect("model_not_found_error")
    else:
        return redirect(reverse("auth_login"))


def edit_and_update_source(request, source_id):
    if request.user is not None and request.user.is_authenticated:
        if request.method == "GET":
            try:
                source_media = SourceMediaRepository.find_one(source_id)
            except SourceMediaFile.DoesNotExist:
                return redirect("model_not_found_error")

            if request.user.is_super_admin:
                source_media_form = AdminUpdateSourceMediaForm(source_media.to_json)
            else:
                source_media_form = ManagerUpdateSourceMediaForm(source_media.to_json)

            context = {
                "source_media": source_media_form
            }

            return render(request, "", context)

        elif request.method == "POST":

            if request.user.is_super_admin:
                source_media_form = AdminUpdateSourceMediaForm(request.POST)
            else:
                source_media_form = ManagerUpdateSourceMediaForm(request.POST)

            if source_media_form.is_valid():
                source_media_id = source_media_form.cleaned_data.get("id")
                SourceMediaRepository.update(source_media_id, source_media_form.cleaned_data)
                return redirect(reverse("list_source"))
            else:

                context = {
                    "source_media": source_media_form
                }

                return render(request, "", context)
    else:
        return redirect(reverse("auth_login"))


def list_source(request):
    if request.method == "GET":

        if request.user is not None and request.user.is_authenticated:
            if request.user.is_super_admin is False:
                authenticated_user = request.user
                organisation = authenticated_user.organisation
                source_media_links = SourceMediaRepository.find_by_organisation_id(organisation_id=organisation.id)
                context = {
                    "source_media": source_media_links
                }
                return render(request, "", context)
            else:
                source_media_links = SourceMediaRepository.find_all()
                context = {
                    "source_media": source_media_links
                }
                return render(request, "", context)
        else:
            return redirect(reverse("auth_login"))
