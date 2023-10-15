from django.db import models
from django_softdelete.models import SoftDeleteModel
from organisations.models import Organisations, User


# Create your models here.
class SourceMediaFile(SoftDeleteModel):
    url = models.URLField(blank=False, null=False)
    is_approved = models.BooleanField(default=False)
    source_type = models.CharField(
        choices=[
            ("api", "api"),
            ("web-scrapping", "web-scrapping")
        ],
        null=False,
        blank=False
    )
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def to_json(self):
        return {
            "organisation": self.organisation,
            "source_type": self.source_type,
            "url": self.url,
            "is_approved": self.is_approved
        }


class MediaFile(SoftDeleteModel):
    title = models.CharField(max_length=200, null=False, blank=False)
    file_cover = models.ImageField(null=False, blank=False, upload_to="uploads/media_covers")
    file = models.FileField(null=False, blank=False, upload_to="uploads/media_files")
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_date = models.DateField(auto_created=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "en attente"),
            ("rejected", "rejecter"),
            ("accepted", "accepter"),
        ],
        default="pending"
    )
    media_type = models.CharField(
        choices=[
            ("video", "video"),
            ("audio", "audio")
        ],
        null=False,
        blank=False
    )

    @property
    def to_json(self):
        return {
            "title": self.title,
            "file_cover": self.file_cover,
            "file": self.file,
            "organisation": self.organisation.id,
            "uploaded_date": self.uploaded_date,
            "status": self.status,
            "media_type": self.media_type
        }


class AbstractNotifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING),
    description = models.TextField(null=False, blank=False)
    validation_date = models.DateField(null=True, blank=True),
    is_validated = models.BooleanField(default=False, null=True)
    sent_date = models.DateField(auto_created=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "en attente"),
            ("rejected", "rejecter"),
            ("accepted", "accepter"),
        ],
        default="pending"
    )

    @property
    def to_json(self):
        return {
            "id" : self.id,
            "user_id" : self.user_id,
            "description" : self.description,
            "validation_date" : self.validation_date,
            "is_validated" : self.is_validated,
            "sent_date" : self.sent_date,
            "status" : self.status
        }

    class Meta:
        abstract = True


class Notifications(SoftDeleteModel, AbstractNotifications):
    media = models.ForeignKey(MediaFile, on_delete=models.DO_NOTHING)

    @property
    def to_json(self):
        notification = super().to_json
        notification["media_id"] = self.media_id
        return notification


class NotificationsSourceMedia(SoftDeleteModel, AbstractNotifications):
    source= models.ForeignKey(SourceMediaFile, on_delete=models.DO_NOTHING)

    @property
    def to_json(self):
        notification = super().to_json
        notification["source_id"] = self.source_id
        return notification
