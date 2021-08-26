import json
from http import HTTPStatus

from apps.test_utils.base_api_calls import (
    get,
    post,
)


URL = "http://lms.local/dummy/"


def test_get():
    """Test simple GET request."""

    response = get(URL)

    assert response.status_code == HTTPStatus.OK.value
    assert json.loads(response.content) == {"Dummy": "GET OK"}


def test_post_no_data():
    """Test POST request without any data."""

    response = post(URL)

    assert response.status_code == HTTPStatus.BAD_REQUEST.value


def test_successful_post_with_data():
    """Test a post request with data."""

    data = {"foo": "bar"}

    response = post(
        URL,
        data=data,
    )

    # print(response)
    # print(response.content)
    assert response.status_code == HTTPStatus.OK.value
    assert response.content == {"foo": "bar"}
