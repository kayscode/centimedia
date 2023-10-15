from django.core.exceptions import ObjectDoesNotExist
import datetime

from media_manager.models import Notifications, NotificationsSourceMedia
# from media_manager.repositories import MediaFileRepository, SourceMediaRepository
from .media_file import MediaFileRepository
from .source_media import SourceMediaRepository


class NotificationsRepository:
    repository_model = Notifications

    @classmethod
    def create(cls, notification_data):
        return cls.repository_model.objects.create(
            user=notification_data.get("user_id"),
            media=notification_data.get("media_id"),
            description=notification_data.get("description"),
        )

    @classmethod
    def find_all(cls):
        return cls.repository_model.objects.all()

    @classmethod
    def find_one(cls, notification_id):
        notification = cls.repository_model.objects.get(id=notification_id)
        if notification is None:
            raise Notifications.DoesNotExist

        return notification

    @classmethod
    def approve_notification(cls, notification_id):
        notification = cls.find_one(notification_id)
        notification.is_validated = True
        notification.validation_date = datetime.date.today()
        notification.save()
        MediaFileRepository.approve_uploaded_file(notification.media_id)

        return notification

    @classmethod
    def reject_notification(cls, notification_id):
        notification = cls.find_one(notification_id)
        notification.is_validated = False
        notification.validation_date = datetime.date.today()
        notification.save()

        # reject uploaded file
        MediaFileRepository.reject_uploaded_file(notification.media_id)
        return notification

    @classmethod
    def delete(cls, notification_id):
        notification = cls.find_one(notification_id)
        return notification.delete()


class SourceMediaNotificationsRepository:
    repository_model = NotificationsSourceMedia

    @classmethod
    def create(cls, notification_data):
        return cls.repository_model.objects.create(
            user=notification_data.get("user_id"),
            source=notification_data.get("media_id"),
            description=notification_data.get("description"),
        )

    @classmethod
    def find_all(cls):
        return cls.repository_model.objects.all()

    @classmethod
    def find_one(cls, notification_id):
        notification = cls.repository_model.objects.get(id=notification_id)
        if notification is None:
            raise Notifications.DoesNotExist

        return notification

    @classmethod
    def approve_notification(cls, notification_id):
        notification = cls.find_one(notification_id)
        notification.is_validated = True
        notification.validation_date = datetime.date.today()
        notification.status = "accepter"
        notification.save()

        SourceMediaRepository.approve_uploaded_source(notification.source.id)

        return notification

    @classmethod
    def reject_notification(cls, notification_id):
        notification = cls.find_one(notification_id)
        notification.is_validated = False
        notification.validation_date = datetime.date.today()
        notification.status = "rejecter"
        notification.save()

        # reject uploaded file
        SourceMediaRepository.reject_uploaded_source(notification.source.id)
        return notification

    @classmethod
    def delete(cls, notification_id):
        notification = cls.find_one(notification_id)
        return notification.delete()
