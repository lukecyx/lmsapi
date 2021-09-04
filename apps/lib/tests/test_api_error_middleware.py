from http import HTTPStatus
import pytest

from django.conf import settings

from apps.test_utils.base_api_calls import post
from apps.users.views import CreateUser


class MockException:
    """A mock exception to test APIErrorMiddleware."""

    def __init__(self, *args, **kwargs):
        raise Exception("Mock Exception")


class TestAPIErrorMiddleware:
    """This will occur for every view where an exception gets raised.

    CreateUserView is used.
    """

    URL = "/users/create/"

    @pytest.mark.django_db
    def test_exception_in_json(self, monkeypatch):
        monkeypatch.setattr(CreateUser, "post", MockException)

        response = post(
            self.URL,
            data={
                "email": "testuser1@user.com",
                "email2": "testuser1@user.com",
                "password": "supersecretpassword",
                "password2": "supersecretpassword",
                "username": "Chewbaca",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST.value
        assert response.content == {"error": "Mock Exception"}

    @pytest.mark.django_db
    def test_exception_raised_locally(self, monkeypatch):
        monkeypatch.setattr(CreateUser, "post", MockException)
        monkeypatch.setattr(settings, "IS_LOCAL", True)

        with pytest.raises(Exception):
            post(
                self.URL,
                data={
                    "email": "testuser1@user.com",
                    "email2": "testuser1@user.com",
                    "password": "supersecretpassword",
                    "password2": "supersecretpassword",
                    "username": "Chewbaca",
                },
            )

    @pytest.mark.django_db
    def test_exception_raised_in_debug(self, monkeypatch):
        monkeypatch.setattr(CreateUser, "post", MockException)
        monkeypatch.setattr(settings, "DEBUG", True)

        with pytest.raises(Exception):
            post(
                self.URL,
                data={
                    "email": "testuser1@user.com",
                    "email2": "testuser1@user.com",
                    "password": "supersecretpassword",
                    "password2": "supersecretpassword",
                    "username": "Chewbaca",
                },
            )
