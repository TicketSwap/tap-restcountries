"""RestCountries entry point."""

from __future__ import annotations

from tap_restcountries.tap import TapRestCountries

TapRestCountries.cli()
