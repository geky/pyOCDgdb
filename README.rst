pyDAPgdb
========

pyDAPgdb is a complete GDB server implemented on top of the 
`pyOCD <https://github.com/mbedmicro/pyOCD>`__ library.

From a GDB client, you have all the features provided by gdb:

-  load a .elf file
-  read/write memory
-  read/write core register
-  set/remove hardware breakpoints
-  high level stepping
-  reset
-  ...

Installation
------------

To install the latest development version (master branch), you can do
the following:

.. code:: shell

    $ pip install --pre -U https://github.com/mbedmicro/pyDAPgdb/archive/master.zip

Note that you may run into permissions issues running these commands.
You have a few options here:

#. Run with ``sudo -H`` to install pyDAPgdb and dependencies globally
#. Specify the ``--user`` option to install local to your user
#. Run the command in a `virtualenv <https://virtualenv.pypa.io/en/latest/>`__ 
   local to a specific project working set.

You can also install from source by cloning the git repository and running

.. code:: shell

    python setup.py install

Standalone GDB Server
---------------------

When you install pyDAPgdb via pip, you should be able to execute the
following in order to start a GDB server powered by pyOCD:

.. code:: shell

    pydap-gdbserver

You can get additional help by running ``pydap-gdbserver --help``.

Recommended GDB and IDE setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GDB server works well with Eclipse and the GNU ARM Eclipse OpenOCD plug-in.
To view register the Embedded System Register Viewer plugin can be used.
These can be installed from inside eclipse using the following links:
GNU ARM Eclipse: http://gnuarmeclipse.sourceforge.net/updates
Embedded System Register Viewer: http://embsysregview.sourceforge.net/update

The pyOCD gdb server executable will run as a drop in place replacement for
OpenOCD. If a supported mbed development board is being debugged the target
does not need to be specified, as pyOCD will automatically determine this.
If an external processor is being debugged then ``-t [processor]`` must
be added to the command line. For more information on setup see
`this post for OpenOCD <http://gnuarmeclipse.livius.net/blog/openocd-debugging/>`__

Development Setup
-----------------

PyOCD developers are recommended to setup a working environment using
`virtualenv <https://virtualenv.pypa.io/en/latest/>`__. After cloning
the code, you can setup a virtualenv and install the PyOCD
dependencies for the current platform by doing the following:

.. code:: console

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r dev-requirements.txt

On Windows, the virtualenv would be activated by executing
``env\Scripts\activate``.

Examples
--------

Simple GDB server in python
~~~~~~~~~~~~~~~~~~

Python:

.. code:: python

    from pyDAPgdb import GDBServer
    from pyOCD.board import MbedBoard

    import logging
    logging.basicConfig(level=logging.INFO)

    board = MbedBoard.chooseBoard()

    # start gdbserver
    gdb = GDBServer(board, 3333)

gdb server:

::

    arm-none-eabi-gdb basic.elf

    <gdb> target remote localhost:3333
    <gdb> load
    <gdb> continue

