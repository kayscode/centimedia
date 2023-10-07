from django.core.exceptions import ObjectDoesNotExist
import datetime

from media_manager.models import Notifications
from media_manager.repositories.media_file import MediaFileRepository


class NotificationsRepository:

    def __int__(self):
        self.notifications_manager = Notifications.objects

    def create(self, notification_data):
        return self.notifications_manager.create(
            user_id=notification_data.get("user_id"),
            media_id=notification_data.get("user_id"),
            description=notification_data.get("description"),
            status=notification_data.get("status"),
            validation_date=notification_data.get("validation_date"),
            is_validated=notification_data.get("is_validated"),
            sent_date=notification_data.get("sent_date")
        )

    def find_all(self):
        return self.notifications_manager.all()

    def find_one(self, notification_id):
        notification = self.notifications_manager.get(id = notification_id)

        if notification is None:
            raise ObjectDoesNotExist
        return notification

    def approve_notification(self, notification_id):
        media_repository = MediaFileRepository()

        notification = self.find_one(notification_id)
        notification.is_validated = True
        notification.validation_date = datetime.date.today()
        notification.save()
        media_repository.approve_uploaded_file(notification.media_id)

        return notification

    def reject_notification(self, notification_id):
        media_repository = MediaFileRepository()

        notification = self.find_one(notification_id)
        notification.is_validated = False
        notification.validation_date = datetime.date.today()
        notification.save()

        #reject uploaded file
        media_repository.reject_uploaded_file(notification.media_id)
        return notification

    def delete(self,notification_id):
        notification = self.find_one(notification_id)
        return notification.delete()
