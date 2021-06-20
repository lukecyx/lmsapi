from http import HTTPStatus
from typing import Callable, Union

from django.http import HttpResponse, HttpRequest, JsonResponse


class ContentTypeMiddleware:
    """Returns HTTP 415 for any request that does not have the correct
    Content-Type header.

    The only Content-Type being accepted for each request is:
    'Content-Type: application/json'
    """

    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> Union[HttpResponse, JsonResponse]:
        request_method = request.META.get("REQUEST_METHOD")
        if request_method == "GET":
            return self.get_response(request)

        content_type = request.META.get("CONTENT_TYPE")

        if content_type != "application/json":
            return HttpResponse(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE.value)

        response = self.get_response(request)

        return response
