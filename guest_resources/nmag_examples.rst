Nmag Examples
-------------

Nmag examples can also be run, and can be found in section 2 (Guided Tour) of
the manual found here:

    http://nmag.soton.ac.uk/nmag/current/manual/html/manual.html

or locally in:

    `~/nmag-0.2.1/doc/html/manual.html </home/virtualmicromagnetics/nmag-0.2.1/doc/html/manual.html>`__

Example files can be found in::

    ~/nmag-examples/

A test suite is also available for the discerning user. To use the test suite,
configuration must first be performed::

    sudo su  # We need to run this as root for permissions purposes.
    cd /opt/nmag/nmag-0.2.1/nsim/tests/config
    PATH=$PATH:/opt/nmag/nmag-0.2.1/nsim/bin
    bash find_nsim.sh
    exit

The tests are wrapped in a Makefile, and hence can only be run after the
configuration by commanding::

    sudo su
    cd /opt/nmag/nmag-0.2.1/nsim/tests
    make
    exit
