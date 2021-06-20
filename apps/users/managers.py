from typing import Any, Callable, Dict, TypeVar

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from apps.users.constants import Roles

User = TypeVar("User")
StaffUser = TypeVar("StaffUser")
Superuser = TypeVar("Superuser")


class CustomUserManager(BaseUserManager):
    """Custom user model manager using email as the unique identifier for
    authentication."""

    def _create_user(
        self,
        email: str,
        password: str,
        commit: bool = True,
        **extra_fields: Dict[str, Any],
    ) -> User:
        """Create and save a stanard or superuser user using the given email
        and password and any extra fields.

        :param email: Users email address.
        :param password: Users password.
        :param commit: Optional: Whether to commit user creation to the db.
        :extra_fields: Any extra fields to add to the user.

        :return: A new user object Standard, Staff or Superuser.
        """

        if not email:
            raise ValueError(_("Email is required"))

        email_in_use = self.model.objects.filter(email=email).count()

        if email_in_use:
            raise ValueError(_("Email already in use"))

        if not password:
            raise ValueError(_("Password is required"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        # Will raise any validation errors for you.
        validate_password(password)
        # Password is valid at this point, so set it.
        user.set_password(password)
        user.full_clean()

        if commit:
            user.save(using=self._db)

        return user

    def create_user(
        self,
        email: str,
        password: str,
        commit: bool = True,
        **extra_fields: Dict[str, Any],
    ) -> User:
        """Create and save a standard user given the email, password and any
        extra fields.

        :param email: Users email address.
        :param password: Users password.
        :param commit: Optional: Whether to commit user creation to the db.
        :param commit: Optional: Whether to commit user creation to the db.
        :extra_fields: Any extra fields to add to the user.

        :return: Standard User Object.
        """

        # Ensure that a standard user cannot become a superuser during creation.
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, commit, **extra_fields)

    def create_staff_user(
        self,
        email: str,
        password: str,
        commit: bool = True,
        **extra_fields: Dict[str, Any],
    ) -> StaffUser:
        """Create and save a staff user given the email, password and any
        extra fields.

        Don't set is_active = True by default, this should be togglable
        when required.

        :param email: Users email address.
        :param password: Users password.
        :param commit: Optional: Whether to commit user creation to the db.
        :param commit: Optional: Whether to commit user creation to the db.
        :extra_fields: Any extra fields to add to the user.

        :return: Staff User Object.
        """

        # Ensure that a staff user cannot become a superuser during creation.
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, commit, **extra_fields)

    def create_superuser(
        self,
        email: str,
        password: str,
        commit: bool = True,
        **extra_fields: Dict[str, Any],
    ) -> Superuser:
        """Create and save a superuser with given email and password and any
        extra fields.

        is_active = True is required otherwise we can't activate a superuser
        account.

        :param email: Users email address.
        :param password: Users password.
        :param commit: Optional: Whether to commit user creation to the db.
        :extra_fields: Any extra fields to add to the user.

        :return: Superuser User object.
        """

        # Ensure that a creating a superuser will always be a superuser.
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Somehwat redundant but just in case, check extra_fields for requried
        # variables to be True.
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("A superuser must be staff"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must be enabled as a superuser"))

        return self._create_user(email, password, commit, **extra_fields)

    def create_user_factory(
        self,
        role: int,
    ) -> Callable:
        """Factory method for calling the correct user create method based
        on role.

        :param role: Which role to create the user as.
        :param email: Users email.
        :param password: Users password.
        :param commit: Whether to commit to the db, defaults to True.
        :param extra_fields: Any extra fields when creating the user.

        :return: User create method for specific role.
        :raises: NotImplemntedError if there is no user create method for the
                 role provided.
        """

        if not role or role == Roles.STANDARD.value:
            return self.create_user

        if role == Roles.STAFF.value:
            return self.create_staff_user

        if role == Roles.SUPERUSER.value:
            return self.create_superuser

        raise NotImplementedError(f"role={role} not yet implemented")
