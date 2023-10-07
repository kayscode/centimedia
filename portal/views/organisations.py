from django.shortcuts import render
from ogranisations.repository import OrganisationRepository

organisation_repository = OrganisationRepository()


def organisation_list(request):
    """
        get a list of all organisations
    """

    # retrieve all the registered organisations that has already upload media resources
    organisations = organisation_repository.find_all()
    context = {
        "organisations": organisations,
        "media": {}
    }

    return render(request, "", context)


def organisation_media_list(request):
    """
        get details about an organisation with all the ressource media
    """

    # retrieve all media files (video and audio) uploaded

    # use source media that belongs to the organisation, and retrieve all media files
    # from all the source media available.

    context = {
        "media_files": {},
        "web_scraped_media_files": {}
    }
    pass


def organisation_filtered_media(request):
    """
        return the list of media file base on filters options
    """
    pass
