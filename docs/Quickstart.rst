================
Quickstart Guide
================

.. warning::
    This documentation is currently undergoing maintenance and big changes, if you find any mistakes and/or errors please create PR's or issues on `project's github <https://github.com/ModerNews/MAL-API-Client-Upgraded>`_


Wrapper Authorization
=====================

MAL API has quite complicated authorization process for a beginner, first you will need to choose type of authentication you want your bot to use

Anonymous Authorization
~~~~~~~~~~~~~~~~~~~~~~~
This one is simple, only thing you need is :code:`client_id` available on `MAL API control panel <https://myanimelist.net/apiconfig>`_, although this form is quite limited, there is no possibility of:

#. Fetching user information
#. Fetching list information
#. Updating list information

[Mal_Client_Info.png here]

After getting :code:`client_id` as shown the only thing you need to do to get your client running is:

.. code-block:: python

    import malclient

    id = '3972103843b1j12' # Your client id fetched from myanimelsit
    client = malclient.Client(client_id=id)

User Authorization
~~~~~~~~~~~~~~~~~~
.. note::
    This way of authorizing only applies if you're going to use one static token (idealy yours), if your app will need multiple users, or needs custom auth flow please refer to :doc:`Authorization <Authorization>` for detailed guide

| This type of authorization available within API is one let's you use all functionalities of an API, you can set it up with help of the wrapper, all you need is :code:`client_id` and :code:`client_secret`
| You will be prompted with webpage (or link to webpage if console can't manage to open it for you) where you will need to allow your app to access data from your account, after that you will be redirected. You need to paste redirect link back into console.

.. code-block:: python

    import malclient

    id = '3972103843b1j12'  # Your client id fetched from myanimelsit
    secret = 'duisadaw892138979qwiudsa0'  # Your client secret fetched from myanimelist
    client = malclient.Client.generate_new_token(client_id, client_secret)  # Everything is handled automatically here

First steps
===========

Now that you're authenticated with API you may start querying MAL for all information you need, two most important endpoints for anime are:

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token, nsfw=True)
    data1 = client.search_anime(keyword='Fate')  # Search for all anime series with `Fate` in name
    data2 = client.get_anime_details(anime_id)  # Get full information about given anime series

And same goes for manga:

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token, nsfw=True)
    data1 = client.search_manga(keyword='Fate')  # Search for all anime series with `Fate` in name
    data2 = client.get_manga_details(anime_id)  # Get full information about given anime series

Common Parameters
=================

NSFW
~~~~
This parameter controls if results with nsfw field :code:`Gray` or :code:`Black` will be shown
it can be set globally either while defining client class or in runtime with nsfw attribute.
It is set to :code:`True` by default.

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token, nsfw=True)
    client.nsfw = True

Functions which make use of this in queries also have nsfw parameter defined, which will overwrite globally defined attribute for this one query

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token, nsfw=False)
    data1 = client.search_anime(keyword='Fate', limit=100)
    data2 = client.search_anime(keyword='Fate', nsfw=True, limit=100)

    print(data1 == data2)  # Those two datasets are different, with nsfw entries present in data2

Limit
~~~~~
This is most common parameter, it exists in almost every query and presents how many entries (at max) will be fetched, so f.e.:

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token)
    data1 = client.get_anime_ranking(ranking_type=malclient.AnimeRankingType.POPULAR, limit=5)  # only 5 entries will be returned

Offset
~~~~~~
This parameter present in most queries, it defines first item that is to be fetched from list queries, f.e.

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token)
    data1 = client.get_anime_ranking(ranking_type=malclient.AnimeRankingType.POPULAR, limit=5, offset=5)

This response will fetch 5 items after 5 item offset, so entries with positions in ranking: 6, 7, 8, 9, 10.

Fields
~~~~~~
Fields are parameter taken by multiple queries used to determine what information in particular will be fetched within query.
For it I designed special object to generate fields parameter for you. There are three ways to prepare it.
First, you can use predesigned field groups:

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token)
    fields = malclient.Fields.anime()  # This represents all anime fields
    client.get_anime_ranking(ranking_type=malclient.AnimeRankingType.POPULAR, limit=5, fields=fields)

| I you ran this snippet you will see that your query now contains full data about each anime available in list.
| Other possibility of determining those values is setting them in constructor

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token)
    fields = malclient.Fields(pictures=True,
                              recommendations=fields.Fields.anime(),
                              related_anime=True)
    client.get_anime_fields(10087, fields=fields)

As you can see in this example two of those fields (:code:`recommendations`, :code:`related_anime`) can containing subfields, in this case those subfields are fields of anime,
but they can be other as well, f.e. :code:`authors` in manga entries, you can define them in two ways:

* One, as shown in :code:`recommendations` you can define it as another fields object
* Second, you can assign :code:`bool` value to it, either :code:`True` to contain every field, or :code:`False` to contain none

Third way uses custom generator to prepare new fields object based of list of fields you want to get, for fields containing subfields, if it is contained in list it's value will be treated as :code:`True`, and all subfields will be returned

.. code-block:: python

    import malclient

    client = malclient.Client(access_token=access_token, refresh_token=refresh_token)
    fields = malclient.Fields(['pictures', 'recommendations', 'related_anime'])
    client.get_anime_fields(10087, fields=fields)

What's next?
============
| That's everything for a quickstart, if you want to know more please refer to :doc:`full documentation <API_Reference>`.
| You may as well want to see :doc:`Authorization <Authorization>` for more details about integrating user auth into your app.