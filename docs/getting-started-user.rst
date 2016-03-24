Getting Started: As a User
==========================

To start a :term:`Virtual Micromagnetics` environment, you will need the
following software:

 - VirtualBox >= 5.0 (https://www.virtualbox.org/wiki/downloads)

 - Vagrant >= 1.7.4 (https://www.vagrantup.com/downloads)

Then command the following in an empty directory::

  vagrant init virtualmicromagnetics/full
  vagrant up --provider virtualbox

These commands will download the Full Virtual Micromagnetics environment from
the Internet to your computer, and load the environment automatically. When
complete, you should be greeted with this window:

.. image:: images/user-window-1.png

This is output from a :term:`virtual machine` running on your computer! Virtual
machines produced in this way run Ubuntu GNU/Linux (https://www.ubuntu.com)
with the XFCE window manager. From here, follow instructions in the welcome
file on the desktop to run simulations with the pre-installed packages. Never
worry about software dependencies again!

Next, see :ref:`environments` for the environments that are available besides the
Full Virtual Micromagnetics environment, and the software on these
environments.
