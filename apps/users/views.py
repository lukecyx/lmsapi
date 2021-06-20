from http import HTTPStatus
from typing import Dict, Union

from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse, HttpRequest

from django.views.generic.base import View

from apps.lib.utils import validate_data


class CreateUser(View):
    http_method_names = ["post"]

    def get_queryset(self):
        return get_user_model().objects.all()

    def post(
        self, request: HttpRequest, data: Dict
    ) -> Union[JsonResponse, HttpResponse]:
        """Create a user.

        :param request: HttpRequest.
        :param data: Data from request body.
        """

        required_args = ["email", "email2", "password", "password2"]
        optional_args = ["username", "first_name", "last_name", "role"]
        validated_data = validate_data(data, required_args, optional_args)

        # Pull out the necessary fields e.g. email, password, see if they match
        # if so, create the user, else return a response.
        email = validated_data.pop("email")
        email2 = validated_data.pop("email2")

        if email != email2:
            return JsonResponse(
                status=HTTPStatus.BAD_REQUEST.value,
                data={"error": "emails provided do not match"},
            )

        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")

        if password != password2:
            return JsonResponse(
                status=HTTPStatus.BAD_REQUEST.value,
                data={"error": "passwords provided do not match"},
            )

        role = validated_data.pop("role", None)

        # Mypy and Django don't like each other... Below is valid.
        create_user = get_user_model().objects.create_user_factory(role)  # type: ignore

        create_user(email=email, password=password, **validated_data)

        return JsonResponse(
            status=HTTPStatus.CREATED.value, data={"response": "user created"}
        )
