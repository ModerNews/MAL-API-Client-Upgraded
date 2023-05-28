from __future__ import annotations
from typing import Optional, Literal, Union

from .Datamodels import Fields, Person, PersonFields
from .exceptions import MainAuthRequiredError

__all__ = ["Industry"]


class Industry:
    def __init__(self):
        return

    def get_person_details(self, person_id, *, fields: PersonFields = PersonFields()):
        """
        Get full info about person with provided id

        :param int person_id: id on https://myanimelist.net
        :param Fields fields: Fields returned alongside results

        :returns: PersonObject for requested id
        :rtype: PersonObject
        """
        uri = f'people/{str(person_id)}'
        params = {'fields': fields.to_payload()}
        data = self._api_handler.call(uri, params=params)
        return Person(**data)
