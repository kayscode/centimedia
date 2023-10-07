from django.shortcuts import render
from media_manager.forms.media import CreateMediaFileForm, UpdateMediaFileForm, DeleteMediaFileForm
from media_manager.repositories.media_file import MediaFileRepository
from media_manager.repositories.source_media import SourceMediaRepository

from media_manager.service.webscraping import SourceMediaFileWebScrapper
from media_manager.service.apis.media import SourceMediaFileService

media_file_repository = MediaFileRepository()
source_media_repository = SourceMediaRepository()


def get_media_file_list(request):
    """
        get list of all media file
    """

    api_resources_links = source_media_repository.find_by_media_type("api")
    web_scrapped_links = source_media_repository.find_by_media_type("web-scrapping")

    web_scrapped_media_file = SourceMediaFileWebScrapper.get_media_files(web_scrapped_links)
    api_media_file = SourceMediaFileService.get_media_files(api_resources_links)

    uploaded_media_file = media_file_repository.find_all()

    context = {
        "web_scrapped_media_file": web_scrapped_media_file,
        "api_media_file": api_media_file,
        "uploaded_media_file": uploaded_media_file
    }

    return render(request,"",context)


def delete_media_file(request,media_file_id):
    pass


def edit_and_update_media_file(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
