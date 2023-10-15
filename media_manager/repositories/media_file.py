from media_manager.models import MediaFile


class MediaFileRepository:

    @classmethod
    def find_all(cls):
        return MediaFile.objects.all()

    @classmethod
    def find_one(cls, media_id):
        media = MediaFile.objects.get(id=media_id)

        if media is None:
            raise MediaFile.DoesNotExist

        return media

    @classmethod
    def create(cls, media_data):
        return MediaFile.objects.create(
            title=media_data.get("title"),
            file_cover=media_data.get("file_cover"),
            file_path=media_data.get("file_path"),
            organisation=media_data.get("organisation"),
            media_type=media_data.get("media_type")
        )

    @classmethod
    def update(cls, media_id, media_data):
        media = cls.find_one(media_id)

        media.title = media_data.get("title")
        media.file_cover = media_data.get("file_cover")
        media.file_path = media_data.get("file_path")
        media.organisation = media_data.get("organisation")
        media.status = media_data.get("status")
        media.media_type = media_data.get("media_type")

        return media.save()

    @classmethod
    def approve_uploaded_file(cls, media_id):
        media = cls.find_one(media_id)
        media.source_type= "accepter"
        return media.save()

    @classmethod
    def reject_uploaded_file(cls, media_id):
        media = cls.find_one(media_id)
        media.source_type = "accepter"
        return media.save()

    @classmethod
    def delete(cls, media_id):
        media = cls.find_one(media_id)
        if media is not None:
            return media.delete()

    @classmethod
    def find_by_organisation_id(cls, organisation_id):
        return cls.find_all().filter(organisation = organisation_id)
