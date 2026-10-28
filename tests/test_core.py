"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from singer_sdk.testing import get_tap_test_class

from tap_restcountries.streams import CountriesStream
from tap_restcountries.tap import TapRestCountries

TestTapRestCountries = get_tap_test_class(
    tap_class=TapRestCountries,
)


def test_demo_record_maps_to_v31_shape() -> None:
    """The v5 demo key returns one real Canada object; map it without spending quota."""
    tap = TapRestCountries(
        config={
            "api_key": "rc_live_demo",
            "fields": ["cca3", "name", "cca2", "latlng", "population"],
        },
    )
    stream = CountriesStream(tap)
    [row] = stream.get_records(None)
    record = stream.post_process(row)

    assert list(record) == ["cca3", "name", "cca2", "latlng", "population"]
    assert record["cca3"] == "CAN"
    assert record["cca2"] == "CA"
    assert record["name"]["common"] == "Canada"
    assert record["latlng"] == [60.0, -95.0]
    assert isinstance(record["population"], int)
