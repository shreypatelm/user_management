from builtins import dict, str
from app.services.email_service import EmailService
from app.models.user_model import User

class NotificationService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    async def send_professional_status_upgrade_notification(self, user: User):
        """
        Notify a user when their account is upgraded to professional status.

        Args:
            user (User): The user who has been upgraded.
        """
        notification_data = {
            "name": user.first_name,
            "nickname": user.nickname,
            "email": user.email,
            "message": f"Congratulations {user.first_name}! Your account has been upgraded to professional status."
        }
        await self.email_service.send_user_email(notification_data, email_type="professional_status_upgrade")

    async def send_generic_notification(self, user: User, subject: str, message: str):
        """
        Send a generic notification email to a user.

        Args:
            user (User): The recipient of the notification.
            subject (str): The subject of the notification email.
            message (str): The body content of the notification.
        """
        notification_data = {
            "name": user.first_name,
            "email": user.email,
            "message": message
        }
        await self.email_service.send_user_email(notification_data, email_type="generic_notification")

