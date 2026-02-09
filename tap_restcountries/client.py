"""REST client handling, including RestCountriesStream base class."""

from __future__ import annotations

import decimal
import sys
from typing import TYPE_CHECKING, Any, ClassVar

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import SinglePagePaginator
from singer_sdk.streams import RESTStream

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

if TYPE_CHECKING:
    from collections.abc import Iterable

    import requests
    from singer_sdk.helpers.types import Context


class RestCountriesStream(RESTStream):
    """RestCountries stream class."""

    # The API returns a top-level JSON array.
    records_jsonpath = "$[*]"

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings.

        Returns:
            The base URL for the REST Countries API.
        """
        return "https://restcountries.com/v3.1"

    @override
    def get_url_params(
        self,
        context: Context | None,
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """ 
        if len(self.config["fields"]) > 10:
            raise ValueError("The API has a maximum of 10 fields per request.")
        return {"fields": ",".join(self.config["fields"])}