from http import HTTPStatus
from typing import Callable, NoReturn, Union

from django.conf import settings
from django.http import HttpRequest, JsonResponse


class APIErrorMiddleware:
    """Any error that occurs/gets raised will return a helpful JSONResponse,
    with the exceptions provided message.

    I.e. ValueError("Wrong Value").
    """

    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        return response

    def process_exception(
        self, request: HttpRequest, exception: Exception
    ) -> Union[JsonResponse, None, NoReturn]:
        """Return an error that happened within a view inside JsonResponse.

        If running locally, or in debug mode, raise the exception.

        :param request: Incoming request.
        :param: exception: Exception that occured in a view.

        :returns: JsonResponse if not running local or debug settings.
                  None on no exception.
        :raises: Exception is raised if using local debug settings.
        """

        if exception:
            # TODO: Find out if sentry is free for personal use.
            # Generally, this should happen for all things that go wrong
            # except for pre-defined accepted errors.
            if settings.IS_LOCAL or settings.DEBUG:
                raise exception

            else:
                error_message = (
                    exception.messages
                    if hasattr(exception, "messages")
                    else str(exception)
                )

                return JsonResponse(
                    status=HTTPStatus.BAD_REQUEST.value, data={"error": error_message}
                )

        return None
