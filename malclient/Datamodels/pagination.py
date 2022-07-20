from malclient import exceptions


class PagedResult(list):
    """

    List of objects with paging support

    """
    def __init__(self, seq, page_link: dict):
        self._payload = page_link
        self._base_class = type(seq[0])
        self._next = page_link.get("next", None)
        self._previous = page_link.get("previous", None)
        super().__init__(seq)

    def fetch_next_page(self, client):
        try:
            assert self._next is not None
            result = client._api_handler.call(uri=self._next.replace(client._base_url, ''))
        except AssertionError:
            raise exceptions.NotFound("There is no next page for this query")
        return PagedResult([self._base_class(**temp_object) for temp_object in result["data"]], result["paging"])

    def fetch_previous_page(self, client):
        try:
            assert self._previous is not None
            result = client._api_handler.call(uri=self._previous.replace(client._base_url, ''))
        except AssertionError:
            raise exceptions.NotFound("There is no previous page for this query")
        return PagedResult([self._base_class(**temp_object) for temp_object in result["data"]], result["paging"])
