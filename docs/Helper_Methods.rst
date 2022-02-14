Authorization
==============

As authorization is not a very simple task with this REST API,
and happened to be a problem for me when I was using API for the first time,
wrapper is equipped with two functions that can be used to simplify this task as much as possible:

.. py:currentmodule:: malclient

.. autofunction:: generate_token

.. automethod:: Client.refresh_bearer_token