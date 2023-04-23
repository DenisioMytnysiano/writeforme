from dataclasses import dataclass


@dataclass
class AuthTokenPair:
    access_token: str
    refresh_token: str
