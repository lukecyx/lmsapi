
from http import HTTPStatus
import json
from typing import Tuple, Union

from django.views.generic import View

from apps.lib.base_views.base_types import JSON


# Deprecated.
class APIBase(View):
    """APIBase view, to be used subclassed for all API views.

    Each method transforms request.body into JSON.

    When overriding methods, you must first call super() to have request params
    as a dict.
    """

    # Override these in a subclass as needed.
    http_method_names = ["get", "post"]

    # This is now done through Middleware.
    def process_post_request_body(
        self, request_body: bytes
    ) -> Union[Tuple[bool, int], Tuple[JSON, int]]:
        """Transform the request body from bytes into JSON format.

        :param request_body: The body of the incoming request.
        :return: Status code and JSON of success/problem.
        """

        # Do not allow post requests to not have a request body, even as a empty dict.
        if not request_body:
            return False, HTTPStatus.BAD_REQUEST.value

        try:
            data = json.loads(request_body)
        except json.JSONDecodeError:
            return False, HTTPStatus.BAD_REQUEST.value

        if not isinstance(data, dict):
            return False, HTTPStatus.BAD_REQUEST.value

        return data, HTTPStatus.OK.value
