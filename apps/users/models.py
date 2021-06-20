# type: ignore

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from .validators import invalid_characters, unique_username


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Simple CustomUser Model, easily extensible to whatever need arises."""

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    username = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        validators=[invalid_characters, unique_username],
    )

    # TODO: Personal Info. Should be encrypted charfield (GDPR).
    email = models.EmailField(_("email address"), unique=True, blank=False, null=False)

    # These are fine to be left unencrypted.
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"CustomUser(email={self.email}, username={self.username})"
