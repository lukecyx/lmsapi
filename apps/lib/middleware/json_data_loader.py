from http import HTTPStatus
import json
from typing import Any, Callable, Dict, List, Optional, Union

from django.http import HttpResponse, HttpRequest, JsonResponse


class JsonDataLoaderMiddleware:
    """Loads the body of each request into a data kwarg to passed into
    each view.

    Disallows any post request that doesn't not contain a body in the request.

    The data kwarg can be omitted from the func/method signature if uneeded,
    i.e. in a GET request.
    """

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> Union[HttpResponse, JsonResponse]:
        return self.get_response(request)

    def process_view(
        self,
        request: HttpRequest,
        view_func: Callable,
        view_args: List,
        view_kwargs: Dict[str, Any],
    ) -> Optional[HttpResponse]:
        """Process the calling of view.

        Adds the request body into the kwargs for each view i.e.
        (data: request.body).

        Rejects any POST request that does not have a body.

        :param request: Incoming request.
        :param view_func: The actual view function/class.
        :param view_args: List of posistional arguments to pass to the view.
        :param view_kwargs: Dict of keyword arguments to pass to the view.

        :return: Compulsory returns for Django Middleware; None or HttpResponse.
        """

        request_method = request.META.get("REQUEST_METHOD", None)

        # TODO: Consider GET parameters.
        if request_method == "GET":
            return None

        if request_method == "POST":
            try:
                request_body = json.loads(request.body)
            except json.JSONDecodeError:
                return HttpResponse(status=HTTPStatus.BAD_REQUEST.value)

            # b'{}' is not considered falsey, so check for this and return 400
            # as we do not want any post requests with empty data.
            if not request_body:
                return HttpResponse(status=HTTPStatus.BAD_REQUEST.value)

            if not isinstance(request_body, dict):
                return HttpResponse(status=HTTPStatus.BAD_REQUEST.value)

            view_kwargs["data"] = request_body

        return None
