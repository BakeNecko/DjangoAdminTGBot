from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from bot.models import Subscriber
from bot.bot import send_message_to_subscribers
from django.utils import timezone
from django.contrib.auth.models import User


@receiver(user_logged_in)
def user_logged_admin_in_handler(sender, request, user: 'User', **kwargs):
    if request.path.startswith('/admin/'):
        message = (
            f"Дата входа: {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"User Info (username - email): {user.username} - {user.email}",
        )
        send_message_to_subscribers(message)
