import pytest

from django.contrib.auth import get_user_model

from apps.users.constants import Roles


user = get_user_model()


@pytest.mark.django_db
@pytest.mark.skip(
    reason=(
        "To be removed, these tests are now redundant as are tested in the view tests"
    )
)
def test_create_standard_user():
    """Test creating a user."""

    standard_user = user.objects.create_user(email="standard@user.com", password="foo")

    assert user.objects.count() == 1
    assert standard_user.email == "standard@user.com"
    assert standard_user.is_active is False
    assert standard_user.is_staff is False
    assert standard_user.is_superuser is False

    with pytest.raises(TypeError):
        user.objects.create_user()

    with pytest.raises(TypeError):
        user.objects.create_user(email="")

    with pytest.raises(ValueError):
        user.objects.create_user(email="", password="foo")

    with pytest.raises(ValueError):
        user.objects.create_user(email="standard@user.com", password="")


@pytest.mark.django_db
@pytest.mark.skip(
    reason=(
        "To be removed, these tests are now redundant as are tested in the view tests"
    )
)
def test_create_staff_user():
    """Test the creation of a staff user."""

    staff_user = user.objects.create_staff_user(email="staff@user.com", password="foo")

    assert user.objects.count() == 1
    assert staff_user.email == "staff@user.com"
    assert staff_user.is_active is False
    assert staff_user.is_staff is True
    assert staff_user.is_superuser is False

    with pytest.raises(TypeError):
        user.objects.create_staff_user()

    with pytest.raises(TypeError):
        user.objects.create_staff_user(email="")

    with pytest.raises(ValueError):
        user.objects.create_staff_user(email="", password="foo")

    with pytest.raises(ValueError):
        user.objects.create_staff_user(email="staff@user.com", password="")


@pytest.mark.django_db
@pytest.mark.skip(
    reason=(
        "To be removed, these tests are now redundant as are tested in the view tests"
    )
)
def test_create_superuser():
    """Test creating a superuser (administrator)."""

    superuser = user.objects.create_superuser(email="super@user.com", password="foo")

    assert user.objects.count() == 1

    assert superuser.email == "super@user.com"
    assert superuser.is_active is True
    assert superuser.is_staff is True
    assert superuser.is_superuser is True

    with pytest.raises(TypeError):
        user.objects.create_superuser()

    with pytest.raises(TypeError):
        user.objects.create_superuser(email="")

    with pytest.raises(ValueError):
        user.objects.create_superuser(email="", password="foo")

    with pytest.raises(ValueError):
        user.objects.create_superuser(email="super@user.com", password="")


# Since user manager has no __init__ mypy will consider it to not have any members.
user_factory_data = [
    (Roles.STANDARD.value, user.objects.create_user),  # type: ignore
    (Roles.STAFF.value, user.objects.create_staff_user),  # type: ignore
    (Roles.SUPERUSER.value, user.objects.create_superuser),  # type: ignore
]


@pytest.mark.parametrize("role, expected", user_factory_data)
def test_user_factory(role, expected):
    """Test user factory returns correct create user method for a given role."""

    result = user.objects.create_user_factory(role)

    assert result == expected
