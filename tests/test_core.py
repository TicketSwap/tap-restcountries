"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from singer_sdk.testing import get_tap_test_class

from tap_restcountries.tap import TapRestCountries


# Run standard built-in tap tests from the SDK:
TestTapRestCountries = get_tap_test_class(
    tap_class=TapRestCountries,
    config=SAMPLE_CONFIG,
)