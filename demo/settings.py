import random
import string
from collections import namedtuple
from os import environ


def get_token_secret():
    # If this wasn't a demo app, I'd pull the secret from some
    # secret manager. But it is a demo, so...
    corpus = string.ascii_letters + string.punctuation + string.digits
    secret = "".join(random.choice(corpus) for _ in range(20))
    return secret


DEFINED = {
    "DB_PASSWORD": environ.get("DB_PASSWORD", ""),
    "DB_USERNAME": environ.get("DB_USERNAME", ""),
    "DB_HOSTNAME": environ.get("DB_HOSTNAME", ""),
    "DB_PORT": environ.get("DB_PORT", "5432"),
    "DB_DATABASE": environ.get("DB_DATABASE", ""),
    "DB_MIN_CONN": int(environ.get("DB_MIN_CONN", 1000)),
    "DB_MAX_CONN": int(environ.get("DB_MAX_CONN", 3000)),
    "JWT_ALGORITHM": "HS256",
    "SESSION_LENGHT": 28800,  # 8 hours
    "JWT_SECRET": get_token_secret(),
}

Settings = namedtuple("Settings", list(DEFINED.keys()))

settings = Settings(*list(DEFINED.values()))
