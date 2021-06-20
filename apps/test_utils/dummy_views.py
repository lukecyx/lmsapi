from http import HTTPStatus
from typing import Dict

from django.http import HttpRequest, JsonResponse
from django.views.generic import View


class DummyView(View):
    """DummyView to test base api calls on."""

    def get(
        self, request: HttpRequest
    ) -> JsonResponse:
        """GET request with dummy response."""

        return JsonResponse(status=HTTPStatus.OK.value, data={"Dummy": "GET OK"})

    def post(
        self, request: HttpRequest, data: Dict = None
    ) -> JsonResponse:
        """POST request with dummy response."""

        return JsonResponse(status=HTTPStatus.OK.value, data=data)
