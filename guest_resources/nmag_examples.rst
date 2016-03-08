Nmag Examples
-------------

Nmag examples can also be run, and can be found in section 2 (Guided Tour) of
the manual found here:

    http://nmag.soton.ac.uk/nmag/current/manual/html/manual.html

or locally in:

    `~/nmag-0.2.1/doc/html/manual.html </home/virtualmicromagnetics/nmag-0.2.1/doc/html/manual.html>`__

Example files can be found in::

    ~/nmag-examples/

The tests are wrapped in a Makefile, and can be run as root by commanding::

    sudo su
    cd /opt/nmag/nmag-0.2.1/nsim/tests
    make
    exit

Note that HLib is not installed, and so tests requiring HLib will fail.
