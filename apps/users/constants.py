from enum import IntEnum, unique
from typing import List


@unique
class Roles(IntEnum):
    """Constants for user roles."""

    STANDARD = 1
    STAFF = 2
    SUPERUSER = 3

    @staticmethod
    def as_list() -> List[int]:
        """Return roles in a list, useful when checking if a supplied role id
        is supported.

        :returns: List of all role values
        """

        return list(map(lambda role: role.value, Roles))
