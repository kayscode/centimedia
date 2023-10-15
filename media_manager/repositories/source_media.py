from media_manager.models import SourceMediaFile
from django.db import models


class SourceMediaRepository:

    @classmethod
    def create(cls, source_media_file_data):
        return SourceMediaFile.objects.create(
            url=source_media_file_data.get("url"),
            media_type=source_media_file_data.get("media_type"),
            organisation=source_media_file_data.get("organisation")
        )

    @classmethod
    def find_one(cls, source_media_file_id):
        source_media = SourceMediaFile.objects.get(id=source_media_file_id)

        if source_media:
            return source_media
        else:
            raise models.ObjectDoesNotExist

    @classmethod
    def find_all(cls):
        return SourceMediaFile.objects.all()

    @classmethod
    def find_by_media_type(cls, media_type: str):
        return SourceMediaFile.objects.all().filter(media_type=media_type)

    @classmethod
    def delete(cls, source_media_file_id):
        source_media = cls.find_one(source_media_file_id)
        return source_media.delete()

    @classmethod
    def update(cls, source_media_file_id, source_media_data):

        fetched_source_media = cls.find_one(source_media_file_id)

        fetched_source_media.url = source_media_data.get("url")
        fetched_source_media.organisation = source_media_data.get("organisation")
        fetched_source_media.media_type = source_media_data.get("media_type")
        fetched_source_media.is_approved = False

        return fetched_source_media.save()

    @classmethod
    def find_by_organisation_id(cls, organisation_id):
        return cls.find_all().filter(organisation=organisation_id)

    @classmethod
    def approve_uploaded_source(cls, source_id):
        source_media = cls.find_one(source_id)
        source_media.is_approved = True
        return source_media.save()

    @classmethod
    def reject_uploaded_source(cls, source_id):
        source_media = cls.find_one(source_id)
        source_media.is_approved = False
        return source_media.save()
