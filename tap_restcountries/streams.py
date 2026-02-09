"""Stream type classes for tap-restcountries."""

from __future__ import annotations

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_restcountries.client import RestCountriesStream

# Translation entry schema (official + common name in a language)
_translation_schema = th.ObjectType(
    th.Property("official", th.StringType),
    th.Property("common", th.StringType),
)


class CountriesStream(RestCountriesStream):
    """Stream of all countries from the REST Countries v3.1 API."""

    name = "countries"
    path = "/all"
    primary_keys = ("cca3",)
    replication_key = None

    schema = th.PropertiesList(
        # ── Codes ──────────────────────────────────────────────
        th.Property(
            "cca2",
            th.StringType,
            description="ISO 3166-1 alpha-2 two-letter country code",
        ),
        th.Property(
            "cca3",
            th.StringType,
            description="ISO 3166-1 alpha-3 three-letter country code",
        ),
        th.Property(
            "ccn3",
            th.StringType,
            description="ISO 3166-1 numeric code (UN M49)",
        ),
        th.Property(
            "cioc",
            th.StringType,
            description="Code of the International Olympic Committee",
        ),
        th.Property(
            "fifa",
            th.StringType,
            description="FIFA country code",
        ),
        # ── Status & membership ────────────────────────────────
        th.Property(
            "independent",
            th.BooleanType,
            description="ISO 3166-1 independence status",
        ),
        th.Property(
            "status",
            th.StringType,
            description="ISO 3166-1 assignment status",
        ),
        th.Property(
            "unMember",
            th.BooleanType,
            description="UN Member status",
        ),
        # ── Name ───────────────────────────────────────────────
        th.Property(
            "name",
            th.ObjectType(
                th.Property("common", th.StringType),
                th.Property("official", th.StringType),
                th.Property(
                    "nativeName",
                    th.ObjectType(
                        additional_properties=th.ObjectType(
                            th.Property("official", th.StringType),
                            th.Property("common", th.StringType),
                        ),
                    ),
                    description="Native country name per language code",
                ),
            ),
            description="Country name (common, official, and native)",
        ),
        th.Property(
            "altSpellings",
            th.ArrayType(th.StringType),
            description="Alternate spellings of the country name",
        ),
        th.Property(
            "translations",
            th.ObjectType(
                additional_properties=_translation_schema,
            ),
            description="Country name translations keyed by language code",
        ),
        # ── Geography ─────────────────────────────────────────
        th.Property(
            "area",
            th.NumberType,
            description="Geographical size in km²",
        ),
        th.Property(
            "borders",
            th.ArrayType(th.StringType),
            description="Border countries (cca3 codes)",
        ),
        th.Property(
            "capital",
            th.ArrayType(th.StringType),
            description="Capital cities",
        ),
        th.Property(
            "capitalInfo",
            th.ObjectType(
                th.Property(
                    "latlng",
                    th.ArrayType(th.NumberType),
                    description="Capital latitude and longitude",
                ),
            ),
            description="Capital city geolocation info",
        ),
        th.Property(
            "continents",
            th.ArrayType(th.StringType),
            description="Continents the country is on",
        ),
        th.Property(
            "landlocked",
            th.BooleanType,
            description="Whether the country is landlocked",
        ),
        th.Property(
            "latlng",
            th.ArrayType(th.NumberType),
            description="Country latitude and longitude",
        ),
        th.Property(
            "maps",
            th.ObjectType(
                th.Property("googleMaps", th.StringType),
                th.Property("openStreetMaps", th.StringType),
            ),
            description="Links to Google Maps and OpenStreetMap",
        ),
        th.Property(
            "region",
            th.StringType,
            description="UN demographic region",
        ),
        th.Property(
            "subregion",
            th.StringType,
            description="UN demographic subregion",
        ),
        th.Property(
            "timezones",
            th.ArrayType(th.StringType),
            description="List of timezones",
        ),
        # ── People & culture ──────────────────────────────────
        th.Property(
            "population",
            th.IntegerType,
            description="Country population",
        ),
        th.Property(
            "languages",
            th.ObjectType(
                additional_properties=th.StringType,
            ),
            description="Official languages keyed by language code",
        ),
        th.Property(
            "demonyms",
            th.ObjectType(
                additional_properties=th.ObjectType(
                    th.Property("f", th.StringType),
                    th.Property("m", th.StringType),
                ),
            ),
            description="Genderized demonyms keyed by language code",
        ),
        # ── Practical info ────────────────────────────────────
        th.Property(
            "currencies",
            th.ObjectType(
                additional_properties=th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("symbol", th.StringType),
                ),
            ),
            description="Currencies keyed by currency code",
        ),
        th.Property(
            "idd",
            th.ObjectType(
                th.Property("root", th.StringType),
                th.Property("suffixes", th.ArrayType(th.StringType)),
            ),
            description="International dialing codes",
        ),
        th.Property(
            "tld",
            th.ArrayType(th.StringType),
            description="Internet top-level domains",
        ),
        th.Property(
            "postalCode",
            th.ObjectType(
                th.Property("format", th.StringType),
                th.Property("regex", th.StringType),
            ),
            description="Postal code format and regex",
        ),
        th.Property(
            "startOfWeek",
            th.StringType,
            description="Day of the start of the week",
        ),
        th.Property(
            "car",
            th.ObjectType(
                th.Property("signs", th.ArrayType(th.StringType)),
                th.Property("side", th.StringType),
            ),
            description="Car signs and driving side",
        ),
        # ── Indices & misc ────────────────────────────────────
        th.Property(
            "gini",
            th.ObjectType(
                additional_properties=th.NumberType,
            ),
            description="Worldbank Gini index keyed by year",
        ),
        # ── Visual assets ─────────────────────────────────────
        th.Property(
            "flag",
            th.StringType,
            description="Flag emoji",
        ),
        th.Property(
            "flags",
            th.ObjectType(
                th.Property("png", th.StringType),
                th.Property("svg", th.StringType),
                th.Property("alt", th.StringType),
            ),
            description="Links to flag images (png and svg)",
        ),
        th.Property(
            "coatOfArms",
            th.ObjectType(
                th.Property("png", th.StringType),
                th.Property("svg", th.StringType),
            ),
            description="Links to coat of arms images",
        ),
    ).to_dict()
