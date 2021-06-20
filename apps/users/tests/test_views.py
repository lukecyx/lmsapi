from http import HTTPStatus
import pytest
from typing import Dict, Tuple

from django.contrib.auth import get_user_model

from apps.test_utils.base_api_calls import post


@pytest.fixture
def data():
    get_user_model().objects.create(
        email="someuser@user.com",
        password="Secretpassword1",
        username="Yoda",
    )


# Role enum value, is_staff, is_supersuser.
USER_ROLES = [
    (1, False, False),
    (2, True, False),
    (3, True, True),
]


TEST_ARGS: Tuple[Dict[str, str], Dict[str, str]] = [
    (
        {
            "email": "testuser@user.com",
            "email2": "testuser@user.com",
            "password2": "SecretPassword1",
        },
        {"error": "expected arg(s) missing :: ['password']"},
    ),
    (
        {
            "email": "testuser@user.com",
            "email2": "testuser@user.com",
            "password": "SecretPassword1",
        },
        {"error": "expected arg(s) missing :: ['password2']"},
    ),
    (
        {
            "email": "testuser@user.com",
            "password": "SecretPassword1",
            "password2": "SecretPassword1",
        },
        {"error": "expected arg(s) missing :: ['email2']"},
    ),
    (
        {
            "email2": "testuser@user.com",
            "password": "SecretPassword1",
            "password2": "SecretPassword1",
        },
        {"error": "expected arg(s) missing :: ['email']"},
    ),
]


class TestCreateUser:
    """Test cases for creating a user."""

    URL = "/users/create/"

    @pytest.mark.django_db
    def test_create_user_success(self):
        response = post(
            self.URL,
            data={
                "email": "testuser@user.com",
                "email2": "testuser@user.com",
                "password": "SecretPassword1",
                "password2": "SecretPassword1",
                "username": "Ob1K2n0bi",
                "first_name": "Obiwan",
                "last_name": "Kenobi",
            },
        )

        assert response.status_code == HTTPStatus.CREATED.value
        assert response.content == {"response": "user created"}
        assert get_user_model().objects.all().count() == 1
        assert get_user_model().objects.get(pk=1).is_active is False
        assert get_user_model().objects.get(pk=1).is_staff is False
        assert get_user_model().objects.get(pk=1).is_superuser is False

    @pytest.mark.django_db
    @pytest.mark.parametrize("test_args, expected_exception", TEST_ARGS)
    def test_correct_errors_without_required_args(self, test_args, expected_exception):
        response = post(self.URL, data=test_args)

        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == expected_exception

    @pytest.mark.django_db
    def test_password_is_validated_by_django(self):
        response = post(
            self.URL,
            data={
                "email": "testuser1@user.com",
                "email2": "testuser1@user.com",
                "password": "asdf",
                "password2": "asdf",
                "username": "d4rth",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {'error': ['This password is too short. It must contain at least 8 characters.', 'This password is too common.']}

    @pytest.mark.django_db
    def test_password_error_diff_environment(self, data):
        response = post(
            self.URL,
            data={
                "email": "testuser1@user.com",
                "email2": "testuser1@user.com",
                "password": "asdf",
                "password2": "asdf",
                "username": "d4rth",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {
            "error": [
                "This password is too short. It must contain at least 8 characters.",
                "This password is too common.",
            ]
        }

    @pytest.mark.django_db
    def test_create_user_fails_without_number_in_password(self):
        response = post(
            self.URL,
            data={
                "email": "testuser1@user.com",
                "email2": "testuser1@user.com",
                "password": "0000",
                "password2": "0000",
                "username": "d4rth",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {
            "error": [
                "This password is too short. It must contain at least 8 characters.",
                "This password is too common.",
                "This password is entirely numeric.",
            ]
        }

    @pytest.mark.django_db
    def test_passwords_must_match(self):
        response = post(
            self.URL,
            data={
                "email": "testuser1@user.com",
                "email2": "testuser1@user.com",
                "password": "d4rthvader",
                "password2": "d4rthvader123",
                "username": "d4rthvader",
            },
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {"error": "passwords provided do not match"}

    @pytest.mark.django_db
    def test_emails_must_match(self):
        response = post(
            self.URL,
            data={
                "email": "testuser1@user.com",
                "email2": "testuser12@user.com",
                "password": "d4rthvader",
                "password2": "d4rthvader",
                "username": "d4rthvader",
            },
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {"error": "emails provided do not match"}

    @pytest.mark.django_db
    def test_user_already_exists(self, data):
        response = post(
            self.URL,
            data={
                "email": "someuser@user.com",
                "email2": "someuser@user.com",
                "password": "SecretPassword1",
                "password2": "SecretPassword1",
                "username": "foobar",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {"error": "Email already in use"}

    @pytest.mark.django_db
    @pytest.mark.parametrize("role, is_staff, is_superuser", USER_ROLES)
    def test_user_gets_correct_role(self, role, is_staff, is_superuser):
        response = post(
            self.URL,
            data={
                "email": "someuser@user.com",
                "email2": "someuser@user.com",
                "password": "SecretPassword1",
                "password2": "SecretPassword1",
                "username": "foobar",
                "role": role,
            },
        )

        assert response.status_code == HTTPStatus.CREATED.value
        # There will only be 1 user, the one we've just created.
        # The user data fixture isn't used.
        user = next(iter(get_user_model().objects.all()))
        assert user.is_staff == is_staff
        assert user.is_superuser == is_superuser
        assert response.content == {"response": "user created"}

    @pytest.mark.django_db
    def test_user_must_have_unique_username(self, data):
        response = post(
            self.URL,
            data={
                "email": "someuser42@user.com",
                "email2": "someuser42@user.com",
                "password": "SecretPassword1",
                "password2": "SecretPassword1",
                "username": "Yoda",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {"error": ["Username must be unique"]}

    @pytest.mark.django_db
    def test_username_cannot_have_at_symbol_in(self):
        response = post(
            self.URL,
            data={
                "email": "someuser42@user.com",
                "email2": "someuser42@user.com",
                "password": "SecretPassword1",
                "password2": "SecretPassword1",
                "username": "Qui@gon",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {"error": ["'@' is not allowed in a username"]}

    @pytest.mark.django_db
    def def_username_can_have_any_other_special_chars(self):
        response = post(
            self.URL,
            data={
                "email": "someuser42@user.com",
                "email2": "someuser42@user.com",
                "password": "SecretPassword1",
                "password2": "SecretPassword1",
                "username": "Qui!gon\"'£$%^&*()+-",
            },
        )

        assert response.status_code == HTTPStatus.CREATED.value
        assert response.content == {"response": "user created"}
