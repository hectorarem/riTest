import uuid

from django.contrib.auth.models import User
from django.db import models

class UserApp(User):
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    phonePrefix = models.CharField(max_length=5, verbose_name="Prefijo", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="Teléfono", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return str(self.username)
