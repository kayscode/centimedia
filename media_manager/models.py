from django.db import models
from django_softdelete.models import SoftDeleteModel
from organisations.models import Organisations, User


# Create your models here.
class SourceMediaFile(SoftDeleteModel):
    id = models.BigAutoField()
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


class MediaFile(SoftDeleteModel):
    id = models.BigAutoField()
    title = models.CharField(max_length=200, null=False, blank=False)
    file_cover = models.ImageField(null=False, blank=False, upload_to="uploads/media_covers")
    file = models.FileField(null=False, blank=False, upload_to="uploads/media_files")
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_date = models.DateField(auto_created=True)
    is_approved = models.BooleanField(default=False)
    media_type = models.CharField(
        choices=[
            ("video", "video"),
            ("audio", "audio")
        ],
        null=False,
        blank=False
    )


class Notifications(SoftDeleteModel):
    id = models.BigAutoField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING),
    media_id = models.ForeignKey(MediaFile, on_delete=models.DO_NOTHING)
    description = models.TextField(null=False, blank=False)
    validation_date = models.DateField(),
    is_validated = models.BooleanField(default=None, null=True)
    sent_date = models.DateField(auto_created=True)
