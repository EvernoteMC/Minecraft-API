from ratelimit import Rule
from api.core import config


from typing import Tuple

rate_limit_config = (
    # {
    #     f"^{config.settings.api_prefix}/mojang/check": [
    #         Rule(minute=1),
    #         Rule(group="admin"),
    #     ],
    # },
)


async def rate_auth(scope) -> Tuple[str, str]:
    """
    Resolve the user's unique identifier and the user's group from ASGI SCOPE.

    If there is no user information, it should raise `EmptyInformation`.
    If there is no group information, it should return "default".
    """
    return "USER_UNIQUE_ID", "default"