from http import HTTPStatus
import pytest


from apps.lib.base_views.api_base import APIBase


post_request_bodies = [
    (b'{"foo": "bar"}', ({"foo": "bar"}, HTTPStatus.OK.value)),
    (b"", (False, HTTPStatus.BAD_REQUEST.value)),
    (b"123", (False, HTTPStatus.BAD_REQUEST.value)),
    (b"XX-XX", (False, HTTPStatus.BAD_REQUEST.value)),
]


@pytest.mark.parametrize("request_body, expected", post_request_bodies)
# Deprecated.
def test_process_post_request_body(request_body, expected):
    """Test method turning request body into JSON on APIBase view."""

    result = APIBase().process_post_request_body(request_body)

    assert result == expected
