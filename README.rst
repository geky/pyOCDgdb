pyOCDgdb
========

pyOCDgdb is a complete GDB server implemented with the 
`pyOCD <https://github.com/mbedmicro/pyOCD>`__ library. With the 
appropriate GDB client, pyOCDgdb provides a remote target that 
can be used for debugging any embedded system supported by pyOCD 
at the source-code level.

Installation
------------

To install the latest development version (master branch), you can do
the following:

.. code:: shell

    $ pip install --pre -U https://github.com/<user>/pyOCDgdb/archive/master.zip

| Note that you may run into permissions issues running these commands.
| You have a few options here:

#. Run with ``sudo -H`` to install pyOCDgdb and dependencies globally
#. Specify the ``--user`` option to install local to your user
#. Run the command in a `virtualenv <https://virtualenv.pypa.io/en/latest/>`__ 
   local to a specific project working set.

You can also install from source by cloning the git repository and running

.. code:: shell

    $ python setup.py install

Standalone GDB Server
---------------------

Once you have installed pyOCDgdb, you should be able to simply execute 
the following in order to start a GDB server:

.. code:: shell

    $ pyocd-gdbserver

For additional help and options run ``pyocd-gdbserver --help``.

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

Although running ``pyocd-gdbserver`` is the suggested method for creating a 
GDB server, pyOCDgdb can be integrated into a Python project as a Python library.

Simple GDB server in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python:

.. code:: python

    from pyOCDgdb import GDBServer
    from pyOCD.board import MbedBoard

    # Find a connected mbed device
    board = MbedBoard.chooseBoard()

    # Start a GDB server
    gdb = GDBServer(board, 3333)

GDB client:

.. code:: shell

    $ arm-none-eabi-gdb basic.elf

    (gdb) target remote localhost:3333
    (gdb) load
    (gdb) info registers
    (gdb) monitor reset
    (gdb) continue

