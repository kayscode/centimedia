from media_manager.models import SourceMediaFile
from django.db import models


class SourceMediaRepository:
    def __int__(self):
        self.source_media_file_manager = SourceMediaFile.objects

    def create(self, source_media_file_data):
        return self.source_media_file_manager.create(
            url=source_media_file_data.get("url"),
            media_type=source_media_file_data.get("media_type"),
            organisation=source_media_file_data.get("organisation")
        )

    def find_one(self, source_media_file_id):
        source_media = self.source_media_file_manager.get(id=source_media_file_id)

        if source_media:
            return source_media
        else:
            raise models.ObjectDoesNotExist

    def find_all(self):
        return self.source_media_file_manager.all()

    def find_by_media_type(self, media_type: str):
        return self.source_media_file_manager.filter(media_type=media_type)

    def delete(self, source_media_file_id):
        source_media = self.find_one(source_media_file_id)
        source_media.delete()

    def update(self, source_media_file_id, source_media_data):

        fetched_source_media = self.find_one(source_media_file_id)

        fetched_source_media["url"] = source_media_data.get("url")
        fetched_source_media["organisation"] = source_media_data.get("organisation")
        fetched_source_media["media_type"] = source_media_data.get("media_type")

        return fetched_source_media.save()
