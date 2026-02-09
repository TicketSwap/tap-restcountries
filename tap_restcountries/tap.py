"""RestCountries tap class."""

from __future__ import annotations

import sys

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_restcountries import streams

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override



class TapRestCountries(Tap):
    """Singer tap for RestCountries."""

    name = "tap-restcountries"

    config_jsonschema = {}

    @override
    def discover_streams(self) -> list[streams.RestCountriesStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.CountriesStream(self),
        ]


if __name__ == "__main__":
    TapRestCountries.cli()
