from django.shortcuts import render

from media_manager.repositories import MediaFileRepository,SourceMediaRepository


def home(request):
    """
        rendering the home page with all the media resources regrouped by uploaded
        and web scraped.
    """
    # retrieve a limited list of media file

    # use web scraping to get all the media file available on the different source media
    context = {
        "audio_media_files": {},
        "video_media_files": {}
    }

    return render(request, "", context)


def media_file_audio_details(request):
    """
        get media file details
    """

    if request.media == "GET":
        # retrieve audio file information base on the id if the audia was uploaded manually

        # if the audio file is a web scraped resource, passed the argument(url) that point to
        # the audio source
        context = {
            "audio_details": {}
        }
        return render(request, "", context)

    return render(request, "")


def media_file_video_details(request):
    """
        render the details about the video and the possibility to play it
    """

    if request.method == "GET":
        # if the video media is an uploaded file
        # retrieve video media from the database and render all details

        # if the requested video is a web scraped video, pass the url.
        context = {}

        return render(request, "", context)

    return render(request, "")


def media_filtered_option(request):
    """
        return the list of filtered media file based on filter options

    """
    if request.method == "GET":
        #  get filter options
        #  get media file from the database
        #  apply webscraping and filter result based on requested resources

        filtered_media = {}

        return render(request, "", filtered_media)

    return render(request, "")
