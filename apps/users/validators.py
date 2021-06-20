from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


def invalid_characters(username: str) -> None:
    """Handle any unwanted characters in the username.

    Raises a ValidationError if '@' is found in the given username.

    :param username: A users/superusers username.
    """

    if "@" in username:
        raise ValidationError(
            _("'@' is not allowed in a username"), params={"username": username}
        )

    return None


def unique_username(username: str) -> None:
    """Username is optional therefore only check if it is unique if a user
    has supplied a username.

    Raises a ValidationError if another user is found with the same username.
    """

    if username:
        user = get_user_model()
        if user.objects.filter(username=username):
            raise ValidationError(
                _("Username must be unique"), params={"username": username}
            )

    return None
