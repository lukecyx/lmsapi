import pytest

from apps.test_utils.base_api_calls import get, post


URL = "/dummy/"


def test_middleware_does_nothing_with_get_method():
    """Tests JsonDataLoader middleware GET request method."""

    response = get(URL)

    assert response.status_code == 200


BAD_REQ_DATA = [({}), ("1234"), ('{foo":"bar"}')]


@pytest.mark.parametrize("test_data", BAD_REQ_DATA)
def test_returns_bad_request(test_data):
    """Tests that HTTP Bad Request is returned in the following scenarios:

    1. request.body cannot be loaded into JSON.
    2. request.body can be loaded, but is falsey.
    3. request.body can be loaded but is not a dict.
    """

    response = post(URL, data=test_data)

    assert response.status_code == 400
