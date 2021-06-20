from typing import Dict, List, Optional


def validate_data(
    data: Dict, required_args: List[str], optional_args: Optional[List[str]] = None
) -> Dict:
    """Validates data in the request.body to in the incoming view.

    :param data: Data coming into the view from the request.body.
    :param required_args: A list of requried args, that must always be sent
                          in the request.
    :param optional_args: A list of optional args to the view. These are
                          treated as expected arguments.

    :returns: Data dictionary.
    :raises: [TypeError, ValueError] depending on missing/incorrect types of
    params.
    """

    if not data:
        raise ValueError("no data provided")

    if not required_args:
        raise ValueError("required args not specified")

    if not isinstance(data, dict):
        raise TypeError("data must be a dict")

    if not isinstance(required_args, list):
        raise TypeError("required_args must be a list of strings")

    data_keys = set(data.keys())
    difference = list(set(required_args).difference(data_keys))

    # Specified optional args are not considered unexpected and thus removed from
    # the difference.
    if optional_args:
        difference = [arg for arg in difference if arg not in optional_args]

    if difference:
        raise ValueError(f"expected arg(s) missing :: {difference}")

    return data
