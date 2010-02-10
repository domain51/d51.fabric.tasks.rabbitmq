d51.fabric.tasks.rabbitmq
=========================
Fabric tasks for handling basic management tasks on RabbitMQ


Requirements
------------
This has been built to be used with the 1.0a version of the `Fabric
fork <http://github.com/tswicegood/fabric>`_ maintained by `Travis
Swicegood <http://www.travisswicegood.com>`_.  It might be usable with other
versions of Fabric, but your mileage may vary.


Usage
-----
You can import the individual tasks into your current fabfile:

::

    from d51.fabric.tasks.rabbitmq import *

Or, you can import the module and execute the tasks that way:

::

    from d51.fabric.tasks import rabbitmq


Full Documentation
------------------
Full documentation is available in the `docs/` directory and is buildable
using `Sphinx <http://sphinx.pocoo.org/>`_.


