from django.db import models

from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Subscriber(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    chat_id = models.BigIntegerField(unique=True)

    class Meta:
        verbose_name = _("Подписчик")
        verbose_name_plural = _("Подписчики")

    def __str__(self):
        return f"{self.chat_id} - {self.is_active} - {self.subscribed_at}"

    def deactivate(self):
        """Деактивировать подписку."""
        self.is_active = False
        self.save()

    def activate(self):
        """Активировать подписку."""
        self.is_active = True
        self.save()
