==============
API Reference
==============

.. _Client:

Base Class
==========

.. py:currentmodule:: malclient

.. autoclass:: Client
    :members:

Anime-related functions
=======================

.. note::
    Currently `related_manga` field doesn't contain any  data - it is known bug, for more info refer to `Inconsistencies <Inconsistencies.html>`_ page

.. py:currentmodule:: malclient

.. automethod:: Client.get_anime_details

.. automethod:: Client.get_anime_fields

.. automethod:: Client.search_anime

.. note::
    Search query `q` must be string at least 3 and not longer than 64 characters

.. automethod:: Client.get_anime_ranking

.. automethod:: Client.get_seasonal_anime

.. automethod:: Client.get_suggested_anime


Manga-related functions
=======================

.. note::
    Currently `related_anime` field doesn't contain any  data - it is known bug, for more info refer to `Inconsistencies <Inconsistencies.html>`_ page

.. warning::
    Requesting `alternative_titles` field for some mangas may return `400 Bad Request` Error.
    Apparently this is caused by invalid unicode formatting and nothing can be done wrapper-side.

.. py:currentmodule:: malclient

.. automethod:: Client.get_manga_details

.. automethod:: Client.get_manga_fields

.. automethod:: Client.search_manga

.. note::
    Search query `q` must be string at least 3 and not longer than 64 characters

.. automethod:: Client.get_manga_ranking


Forum Boards
============

Forum boards stay pretty much untouch, either by me or previous developer, so there is nothing available at the moment
I will be working on bringing it back though.


User List
==========

.. py:currentmodule:: malclient

.. automethod:: Client.update_my_anime_list_status

.. automethod:: Client.delete_my_anime_list_status

.. automethod:: Client.get_user_anime_list

.. automethod:: Client.update_my_manga_list_status

.. automethod:: Client.delete_my_manga_list_status

.. automethod:: Client.get_user_manga_list


Utility
=======

.. py:currentmodule:: malclient

.. autoclass:: PagedResult
    :members:


Exceptions
==========

.. py:currentmodule:: malclient

.. autoexception:: APIException

.. autoexception:: BadRequest

.. autoexception:: Unauthorized

.. autoexception:: Forbidden

.. autoexception:: NotFound
