from django.shortcuts import render, redirect
from organisations.forms import CreateOrganisationForm, DeleteOrganisationForm, UpdateOrganisationForm
from organisations.repositories.organisation import OrganisationRepository

organisation_repository = OrganisationRepository()


def organisation_list(request):
    context = {
        "organisations": organisation_repository.find_all()
    }
    return render(request, "", context)


def show_organisation(request, organisation_id):
    context = {
        "organisation": organisation_repository.find_one(organisation_id)
    }

    return render(request, "", context)


def create_organisation(request):
    if request.method == "GET":
        organisation_form = CreateOrganisationForm()
        context = {
            "organisation_form": organisation_form
        }
        return render(request, "", context)


def store_organisation(request):
    if request.method == "POST":
        organisation_form = CreateOrganisationForm(request.POST)
        if organisation_form.is_valid():
            organisation = organisation_form.cleaned_data
            organisation_repository.create(organisation)
            return redirect("")

        context = {
            "organisation_form": organisation_form
        }
        return render(request, "", context)


def edit_and_update_organisation(request, organisation_id):
    if request.method == "GET":
        organisation = None
        try:
            organisation = organisation_repository.find_one(organisation_id)

            if organisation is None:
                raise Exception("error occurred impossible to find an organisation  with that id")
            form = UpdateOrganisationForm(organisation.to_form())

            context = {
                "form": form
            }
            return render(request, "", context)
        except:
            context = {
                "error": "organisation doesn't exist"
            }
            return render(request, "", context)

    elif request.method == "POST":
        organisation_form = UpdateOrganisationForm(request.POST)

        if organisation_form.is_valid():

            organisation_data = organisation_form.clean()
            organisation = organisation_repository.find_one(organisation_id)

            if organisation:
                organisation_repository.update(organisation_id, organisation_data)
                return redirect("")

            return render(request, "")

        context = {
            "organisation_form": organisation_form
        }

        return render(request, "", context)


def delete_organisation(request):
    if request.method == "POST":
        form = DeleteOrganisationForm(request.POST)

        if form.is_valid():
            # delete and redirect to list
            pass
        context = {
            "form": form
        }

        return render(request, "", context)
