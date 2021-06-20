from typing import NoReturn, Union

import json
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def get_secret(setting: str) -> Union[str, NoReturn]:
    """Get secret setting or raise ImproperlyConfigured.

    :param setting: Required setting.

    :return: Secrets value.
    :raises: ImproperlyConfigured when setting cannot be found.

    """

    with open(BASE_DIR.joinpath("secrets.json")) as secrets_file:
        secrets = json.load(secrets_file)

    try:
        return secrets.get(setting, None)

    except KeyError as settings_not_found:
        raise ImproperlyConfigured(
            f"{setting} not found in file"
        ) from settings_not_found
