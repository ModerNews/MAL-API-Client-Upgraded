=======
Logging
=======

Introduced in version 1.2.5 was logging module.
Log file registers all requests sent by your client to Myanimelist API,
there are currently two ways of setting it up

First way is using library's function `malclient.setup_logging()`,
this function works as is or can be provided with additional parameters resembling python builtin logging package

.. code-block:: py

    import malclient
    import logging

    # with no parameters
    malclient.setup_logging()

    # or using custom parameters
    malclient.setup_logging(log_level=logging.WARNING, format="%(levelname)s | %(asctime)s | %(message)s", filename="malclient-log.log")

Another way is using python logging module directly, it let's you tweak it some more to match your needs

.. code-block:: py

    import logging

    logging.basic_config(level=logging.INFO, format="%(levelname)s | %(asctime)s | %(message)s", filename="malclient-log.log")

Default logging level is `INFO` this is level on which requests are registered.