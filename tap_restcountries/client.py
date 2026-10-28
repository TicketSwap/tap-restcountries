"""REST client handling, including RestCountriesStream base class."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any

from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.pagination import BaseOffsetPaginator
from singer_sdk.streams import RESTStream

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

if TYPE_CHECKING:
    import requests
    from singer_sdk.helpers.types import Context


PAGE_SIZE = 100


class RestCountriesPaginator(BaseOffsetPaginator):
    """Offset paginator that stops when the response reports no more records."""

    @override
    def has_more(self, response: requests.Response) -> bool:
        """Return whether the API reports records past this page.

        Args:
            response: API response object.

        Returns:
            True if another page is available.
        """
        return response.json()["data"]["meta"].get("more", False)


class RestCountriesStream(RESTStream):
    """RestCountries stream class."""

    url_base = "https://api.restcountries.com/countries/v5"
    records_jsonpath = "$.data.objects[*]"

    @property
    @override
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a bearer token authenticator for the configured API key.

        Returns:
            An authenticator instance.
        """
        return BearerTokenAuthenticator(token=self.config["api_key"])

    @override
    def get_new_paginator(self) -> RestCountriesPaginator:
        """Return a paginator that walks the list endpoint by offset.

        Returns:
            A paginator instance.
        """
        return RestCountriesPaginator(start_value=0, page_size=PAGE_SIZE)

    @override
    def get_url_params(
        self,
        context: Context | None,
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The offset of the next page.

        Returns:
            A dictionary of URL query parameters.
        """
        return {"limit": PAGE_SIZE, "offset": next_page_token}
