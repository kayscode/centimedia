from media_manager.models import MediaFile


class MediaFileRepository:

    def __int__(self):
        self.media_file_manager = MediaFile.objects

    def find_all(self):
        return self.media_file_manager.all()

    def find_one(self, media_id):
        media = self.media_file_manager.get(id=media_id)
        if media is None:
            raise
        return media

    def create(self, media_data):
        return self.media_file_manager.create(
            title=media_data.get("title"),
            file_cover=media_data.get("file_cover"),
            file_path=media_data.get("file_path"),
            organisation=media_data.get("organisation"),
            uploaded_date=media_data.get("uploaded_date"),
            is_approved=media_data.get("is_approved"),
            media_type=media_data.get("media_type")
        )

    def update(self, media_id, media_data):
        media = self.find_one(media_id)

        media.title = media_data.get("title")
        media.file_cover = media_data.get("file_cover")
        media.file_path = media_data.get("file_path")
        media.organisation = media_data.get("organisation")
        media.uploaded_date = media_data.get("uploaded_date")
        media.is_approved = media_data.get("is_approved")
        media.media_type = media_data.get("media_type")

        return media.save()

    def approve_uploaded_file(self, media_id):
        media = self.find_one(media_id)
        media.is_approved = True
        return media.save()

    def reject_uploaded_file(self, media_id):
        media = self.find_one(media_id)
        media.is_approved = False
        return media.save()

    def delete(self, media_id):
        media = self.find_one(media_id)
        if media:
            return media.delete()
