Examples
--------

This file outlines some examples that can be run using magpar, OOMMF, and
nmag on this virtual machine. For more information about these software, please
read `Welcome.html <Welcome.html>`__.


magpar
======

Examples of magpar are available in a seperate tarball to the one used for
installing magpar itself. The examples are already prepared on this virtual
machine (albeit slightly modified), but can be found at::

    ~/magpar-0_9_ex.tar.gz

To run one of these examples, simply navigate to the directory containing the
example and execute the run command using bash, like so::

    cd ~/magpar-examples/sphere_demag/
    bash run

This script will produce some output files visible in the directory.


OOMMF
=====

OOMMF examples are available from installation, and some can be found in::

    ~/oommf-oxs-examples/

To execute one of these examples, such as standard problem 1, command::

    oommf boxsi ~/oommf-oxs-examples/stdprob1.mif

Astute users may note that oommf may be executed from any directory.

Nmag
====

Nmag examples can also be run, and can be found in section 2 (Guided Tour) of
the manual found here:

    http://nmag.soton.ac.uk/nmag/current/manual/html/manual.html

or locally in:

    `~/nmag-0.2.1/doc/html/manual.html </home/vagrant/nmag-0.2.1/doc/html/manual.html>`__

Example files can be found in::

    ~/nmag-examples/

A test suite is also available for the discerning user. To use the test suite,
configuration must firstbe performed by commanding as root::

    cd /opt/nmag/nmag-0.2.1/nsim/tests/config
    PATH=$PATH:/opt/nmag/nmag-0.2.1/nsim/bin
    bash find_nsim.sh

The tests are wrapped in a Makefile, and hence can be run by commanding as root
(after the previous)::

    cd /opt/nmag/nmag-0.2.1/nsim/tests
    make
