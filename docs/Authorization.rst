=============
Authorization
=============

.. warning::
    This documentation is currently undergoing maintenance and big changes, if you find any mistakes and/or errors please create PR's or issues on `project's github <https://github.com/ModerNews/MAL-API-Client-Upgraded>`_

.. warning::
    Before starting you need to create app on `web control panel <https://myanimelist.net/apiconfig>`_, if you don't know how, you can learn it on :ref:`quickstart page <Create App>`.

Wrapper-assisted Auth
=====================

Manual Auth
===========


.. note::
    | Please note even though the examples will be shown for :code:`curl` and/or python :code:`requests` library, same requests should be working for :code:`fetch API`, :code:`Axios` and other similar frameworks.
    | If your new to similar projects you may want to use `Postman <https://www.postman.com>`_ to observe API behaviour.

.. _Step 1:

Step 1: Generating code verifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| First you will need code verifier, this is, by simplification, string proofing, that all the requests in OAuth flow are coming from the same source. This is why it should be unique for every access token you want to get. You can read more about `PKCE for OAuth here <https://www.rfc-editor.org/rfc/rfc7636>`_ If you're intrested
| It's length is required to be between 48 to 128 characters. You can generate it like this in python:

.. code-block:: python

    import secrets

    token = secrets.token_urlsafe(100)  # Generates token, containing only url allowed chars
    code_verifier = token[:128]  # Gets first 128 characters from token

.. _Step 2:

Step 2: Generating authorization url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next you will be generating link that users will use to authenticate your app on their profile

.. code-block:: bash

    https://myanimelist.net/v1/oauth2/authorize?response_type=code& \
     client_id=$CLIENT_ID& \
     code_challenge=$CODE_CHALLENGE& \
     redirect_uri=$REDIRECT \

.. list-table::
    :header-rows: 1

    * - Variable
      - Description

    * - CLIENT_ID
      - Your client id fetched from `MAL Config page <https://myanimelist.net/apiconfig>`_.
    * - CODE_CHALLENGE
      - Same as code verifier generated in :ref:`previous step <Step 1>`
    * - REDIRECT
      - If during app configuration you provided more than one redirect links you will need to specify one of them here

Step 3: User authenticates app with their profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now you will need to redirect/provide your user with link we generated in step 2, if you didn't make any mistakes your user were provided with authentication or login page.
For now let's go to this link ourselves and see it ourselves:

.. image:: _static/img/auth_page.png
    :alt: Authorization Page Screenshot

All there is to do here is just pressing :code:`Allow` and we can go to next step

.. _Step 4:

Step 4: Getting code from redirect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If user allowed access to their account in previous step they will now be redirected to url you provided during app configuration, it may look like this:

.. code-block:: bash

    http://127.0.0.1:5000/redirect?code=def502002f4cdfb367bccdc143628a273880a2fcd012570255175a2d37766afe0ea222b2f48a5253b0017fc8ee573ecc9e1d7735733cf8c78969605adf71a58dd69849a4ca7ac0d5d0894754972e92ecd20f7a025c81e42d8bb9b1e25cea439db925e5baa5038d18bab2d7f1c0ec4cc5b4be324806eb9a1807653dc865ec3ad0e8ae9bc1941cac41404c833bb0039443852ec18f1dec2a9df98e174f45721ecab757dbe4264b341d1663d8bd8cb633d99236dc013e4c93b2e37bbc593e23cd4abcedc031095eb5924f5c187a101683af474ec98c4843bbe9256c615b8477003458000975d9a7f3b1d8c68b1ba2239a582ebcd3fa9a0ad3cb71d7f98bb00444c829ae5f67503d39cc5c1e2ed44ec319d521d250d3f6520dd977214cefb8785eef464d6a8d4b1549aa553ce0f5878f1f219b235601b383b41676633b982d1b566b9099d3283cc1527d96383d8afa6dfbc935fcb2c605354896ec2cbf55caf7e4ef1f518884b3b595da01d5e453cd5297016d1e8a0170ec6c1a1854f912a314bb570bd7da4479cdfcfdca87f1ac1ac5b03de407d710a5ceee20b83bfe613901e22deb1f2cfcf1f7da5b5d290417dde1c72b6a73792bf9efcd4df7e562a8b73ac75e9504f1f8cade0dfae324dd4d66ca79ad2edf0fed4ce2953bbe217ccf02100b04be1a253259b5e646c94a0958446ea08d27132d3792252ea1d946cb26fb454f7ca213989239212a8e38&state=RequestID42

| As you can see there are two parameters here, the one that interests us is :code:`code` one. It contains code that will be used to generate access token.
| If you use web framework you will be able to get it as an query parameter.

Step 5: Getting access token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now what we need to do is generate :code:`POST` request which will return the access and refresh tokens, for it we will be using MAL scheme 2.

.. code-block:: bash

    curl POST https://myanimelist.net/v1/oauth2/token \
        -- header 'Content-Type: application/x-www-form-urlencoded'\
        --data-urlencode 'client_id=$CLIENT_ID' \
        --data-urlencode 'client_secret=$CLIENT_SECRET' \
        --data-urlencode 'grant_type=authorization_code' \
        --data-urlencode 'code=$CODE' \
        --data-urlencode 'redirect_uri=$REDIRECT' \
        --data-urlencode 'code_verifier=$CODE_VERIFIER'

.. code-block:: python

    import requests

    data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': redirect,
    'code_verifier': code_verifier
    }

    requests.post('https://myanimelist.net/v1/oauth2/token', params=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})

.. list-table::
    :header-rows: 1

    * - Variable
      - Description

    * - CLIENT_ID
      - Your client id fetched from `MAL Config page <https://myanimelist.net/apiconfig>`_.
    * - CLIENT_SECRET
      - Your client secret fetched from `MAL Config page <https://myanimelist.net/apiconfig>`_.
    * - grant_type
      - This parameter is required, even though as for now it takes only one possible value: :code:`authorization_code`
    * - CODE
      - Code fetched in :ref:`previous step <Step 4>`
    * - REDIRECT
      - Redirect url, must be the same as in :ref:`Step 2 <Step 2>`
    * - CODE_VERIFIER
      - Code verifier generated in :ref:`Step 1 <Step 1>`, must be the same as :code:`CODE_CHALLANGE` in :ref:`Step 2 <Step 2>`

If all of those variables are set correctly you should get response containing access token, using which you will be able to access authenticated user's profile.

.. code-block:: json

    {
        "token_type": "Bearer",
        "expires_in": 2592000,
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImI4M2FjYzRjZTFhODI4MTc0MDYyODBkMTNjNjg2YjZhNDViYzUwMjNjNTEzYWRkMDkyNWFjYTNmYzQ4ZTcwMTUwNmFkMzEwYWE1Y2YzMzg0In0.eyJhdWQiOiI2NDE0YzI1ZmFjZjYxNzA1NWNlMzE5NTVkNTBkNTBlNSIsImp0aSI6ImI4M2FjYzRjZTFhODI4MTc0MDYyODBkMTNjNjg2YjZhNDViYzUwMjNjNTEzYWRkMDkyNWFjYTNmYzQ4ZTcwMTUwNmFkMzEwYWE1Y2YzMzg0IiwiaWF0IjoxNjY4NTEwODcwLCJuYmYiOjE2Njg1MTA4NzAsImV4cCI6MTY3MTEwMjg3MCwic3ViIjoiMTA4MzEzMzAiLCJzY29wZXMiOltdfQ.AcwtKwRscqgt0wI6bnpiiBxAogpG57eeDkeJT71EPh1Gl5Ge_clhzaZ314FXQ1LeeX3_wDn4cBi_Cg_B2MirOlsAEU0OQqiOU8WnCQkWoD_SndFeaqrJ8eDp3XlruQcOUQs51iUfLDma6T08QtS_G0CbfATAKCPPh9dvWTamWma1NrpK8JI1wLGbUDmIXbu-TLS4YODJCK1RFbjpRoU2n9aag1F078s72bbO_gh9jt8VDfigIhGQbFuOYrWJsQ6m4pMgx6mujT8RSid_3oVrtzWIHwuFpH8DSNT036H3zDFsmEY0PVtz42kpb69vePWsiwq7tLHUBci3xEkU4hVT9Q",
        "refresh_token": "def502001feff6f447a22fe078059aad0ab32c4478691e1959731765df523780efddcef88b213007c5ff87cab219448977a265a3ff7b591b6c450070fcb8ea7ab599532ed0a20a4ccbc06035ee539d4e31c47ca128933088dd48fa92588f77d931fadf1f20d65e159b881413d05772286dbf794afdf864178913c7584a6f72e1aebf52191e718c2dea186f442fc9539c1b855644d03c09304707bdfd4399448361c2024b2bc1210472b4e8be2974ae6cab05cd306bfd1c7983fa2d60c2e7b11e50baeee02bc5e15415a480e7e542663462db59aacebeabf75cb02c08146aa257f9023f78b10bce8bf9353024bd05bed33713f0af9ac62f6012af53a80f768aca966c4fbb478ff15613beba7ed616d8a401c3b8adda41a6b17605a3783871f52ea4fe789ef1158f50e7de291cae4ce483e0af356c7bead94d8f74e44de1541198113321d515a64e132353cae8086f59c58bd2e41f97b8fbb25604413c3d0cedbf37a1834d56717891197209faa32d53c00fcb5187dbcb5693b06577b3ff19a28a0c7caaf17e666f1aab"
    }

Value of :code:`expires_in` is equal to 30 days in seconds, there currently is now way of modifying how long token will last.