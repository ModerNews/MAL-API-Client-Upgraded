API Reference
==============

.. _Client:

Base Class
~~~~~~~~~~

.. autoclass:: malclient.Client


Anime-related functions
~~~~~~~~~~~~~~~~~~~~~~~

Already finished:

.. py:currentmodule:: malclient

.. automethod:: Client.get_anime_details


.. automethod:: Client.search_anime

Still waiting to finish them off:

.. py:currentmodule:: malclient

.. automethod:: Client.get_anime_ranking


.. automethod:: Client.get_seasonal_anime


.. automethod:: Client.get_suggested_anime


Manga-related functions
~~~~~~~~~~~~~~~~~~~~~~~

Already finished:

.. py:currentmodule:: malclient

.. automethod:: Client.get_manga_details


.. automethod:: Client.search_manga

Still waiting to finish them off:

.. py:currentmodule:: malclient

.. automethod:: Client.get_manga_ranking


Forum Boards
~~~~~~~~~~~~

Forum boards stay pretty much untouch, either by me or previous developer, so there is nothing available at the moment
I will be working on bringing it back though.


User Anime List Update
~~~~~~~~~~~~~~~~~~~~~~

Those still need some polishing, but are pretty much functional as far as I know

.. py:currentmodule:: malclient

.. automethod:: Client.update_my_anime_list_status
    
.. automethod:: Client.delete_my_anime_list_status

.. automethod:: Client.get_user_anime_list


User Manga List Update
~~~~~~~~~~~~~~~~~~~~~~

Those still need some polishing, but are pretty much functional as far as I know

.. py:currentmodule:: malclient

.. automethod:: Client.update_my_manga_list_status
    
.. automethod:: Client.delete_my_manga_list_status

.. automethod:: Client.get_user_manga_list


Utility
~~~~~~~

.. py:currentmodule:: malclient

.. automethod:: Client.get_user_info


Exceptions
~~~~~~~~~~

.. py:currentmodule:: malclient

.. autoexception:: APIException

.. autoexception:: BadRequest

.. autoexception:: Unauthorized

.. autoexception:: Forbidden

.. autoexception:: NotFound
