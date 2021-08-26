import json
from typing import Any, Dict, List, NamedTuple, Optional, Union
from http.cookies import SimpleCookie

from django.http import JsonResponse, HttpResponse
from django.test import Client


class PostResponse(NamedTuple):
    status_code: int
    content: Union[List, str, Dict]


CSRF_TOKEN = "XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4"

request_cookies = {"csrftoken": CSRF_TOKEN}
request_headers = {"Content-Type": "application/json"}
csrf_token_header = {"HTTP_X_CSRFTOKEN": CSRF_TOKEN}
post_request_headers = request_headers | csrf_token_header


def get(
    url: str,
    headers: Optional[Dict[str, str]] = request_headers,
    cookies: Optional[Dict[str, str]] = None,
) -> Union[HttpResponse, JsonResponse]:
    """A GET request to an endpoint that should return 200.

    :param url: The url of the endpoint.
    :param headers: Request headers.
    :param request_cookies: Request cookies.
    """

    client = Client()

    if cookies:
        client.cookies = SimpleCookie(cookies)

    return client.get(url, extra=headers)


def post(
    url: str,
    headers: Optional[Dict[str, str]] = post_request_headers,
    cookies: Optional[Dict[str, str]] = request_cookies,
    content_type: str = "application/json",
    data: Optional[Dict[str, Any]] = None,
) -> PostResponse:
    """A POST request to an endpoint

    :param url: The url of the endpoint.
    :param headers: Request headers.
    :param cookies: Request cookies.
    :param content_type: Content-Type HTTP header. Django test client wants it
                         as a parameter not a header. It then adds the
                         Content-Type header itself.
    :param data: Data to send in the request body.
    """

    # The wording in Django docs implies enforcing csrf checks is not worthwhile,
    # however, I want to make sure I'm handling it correctly.
    # TODO: In hindsight this is pretty pointless..
    # There should be 1 test that does this check.
    client = Client(enforce_csrf_checks=True, HTTP_X_CSRFTOKEN=CSRF_TOKEN)

    if cookies:
        client.cookies = SimpleCookie(cookies)

    response = client.post(url, data=data, content_type=content_type, extra=headers)
    response_content_type = response.headers.get("content-type", None)

    if response.content and response_content_type == "application/json":
        content = json.loads(response.content.decode("UTF-8"))
    else:
        content = response.content

    return PostResponse(response.status_code, content)
