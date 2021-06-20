import pytest

from apps.test_utils.base_api_calls import post


URL = "/dummy/"


content_types = [
    ("application/java-archive"),
    ("application/javascript"),
    ("application/pdf"),
    ("application/xhtml+xml"),
    ("application/ld+json"),
    ("application/xml"),
    ("application/zip"),
    ("application/x-www-form-urlencoded"),
]


@pytest.mark.parametrize("content_type", content_types)
def test_middleware_handles_wrong_content_types(content_type):
    """Tests that the middleware denies any Content-Type header that is not

    'Content-Type': 'application/json'

    for a post request.
    """

    response = post(
        URL,
        content_type=content_type,
        data={"foo": "bar"},
    )

    assert response.status_code == 415


def test_middleware_allows_application_json_content_type():
    """Tests that middleware allows the header:

    'Content-Type': application/json
    """

    response = post(URL, data={"foo": "bar"})

    assert response.status_code == 200
    assert response.content == {"foo": "bar"}
