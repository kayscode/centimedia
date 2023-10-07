from django.shortcuts import render, redirect

from media_manager.models import SourceMediaFile

from media_manager.repositories.source_media import SourceMediaRepository
from media_manager.forms.source import CreateSourceMediaForm, UpdateSourceMediaForm, DeleteSourceMediaForm

source_media_file_repository = SourceMediaRepository()


def get_list_of_sources_media(request):
    """
        render all the source media available
    """
    if request.method == "GET":
        source_media_files = source_media_file_repository.find_all()
        # fetch all sources media

        context = {
            "sources_media_file": source_media_files
        }

        return render(request, "", context)


def create_source_media_file(request):
    """
        render the create source form and store new source file
    """
    if request.method == "GET":
        # render the interface
        create_source_media_form = CreateSourceMediaForm()
        context = {
            "form": create_source_media_form
        }
        return render(request, "", context)
    elif request.method == "POST":

        create_source_media_form = CreateSourceMediaForm(request.POST)
        if create_source_media_form.is_valid():
            source_media_file_repository.create(create_source_media_form.cleaned_data)
            # identify the user type , if it's super admin, create the new source directly
            # if it's an admin create the new source but send a notification for validation to super admin
            # for validation purpose

            # show the details about the newly created source media file
            return redirect("")

        context = {
            "form": create_source_media_form
        }
        return render(request, "", context)


def show_source_media(request):
    pass


def edit_and_update_source_media(request, source_media_id):
    """
        render source media editing form
    """
    source_media = None
    try:
        source_media = source_media_file_repository.find_one(source_media_id)
    except SourceMediaFile.DoesNotExist:
        # render error page with customize message
        context = {
            "error_message": ""
        }
        return render(request, "", context)

    if request.method == "GET":

        if source_media is None:
            context = {
                "error_message": ""
            }
            return render(request, "", context)

        source_media_form = UpdateSourceMediaForm(source_media)

        # fetch source media by ID
        # fill the edit Source form with the source media data and render it

        context = {
            "form": source_media_form
        }

        return render(request, "", context)

    elif request.method == "POST":
        source_media_form = UpdateSourceMediaForm(request.POST)

        if source_media_form.is_valid():
            source_media_file_repository.update(source_media_form.cleaned_data.get("id"),
                                                source_media_form.cleaned_data)

        context = {
            "form": source_media_form
        }
        return render(request, "", context)


def get_filtered_source_media(request):
    """
        get filtered option and fetch all data that match the filter criteria
    """

    if request.method == "GET":
        # fetch source media by applying filter option

        context = {

        }
        return render(request, "", context)
