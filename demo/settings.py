from collections import namedtuple
from os import environ

DEFINED = {
    "DB_PASSWORD": environ.get("DB_PASSWORD", ""),
    "DB_USERNAME": environ.get("DB_USERNAME", ""),
    "DB_HOSTNAME": environ.get("DB_HOSTNAME", ""),
    "DB_PORT": environ.get("DB_PORT", "5432"),
    "DB_DATABASE": environ.get("DB_DATABASE", ""),
    "DB_MIN_CONN": int(environ.get("DB_MIN_CONN", 1)),
    "DB_MAX_CONN": int(environ.get("DB_MAX_CONN", 10)),
}

Settings = namedtuple("Settings", list(DEFINED.keys()))

settings = Settings(*list(DEFINED.values()))
