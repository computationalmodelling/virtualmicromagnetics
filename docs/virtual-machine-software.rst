.. _software:

Virtual Machines and Other Software
===================================

A :term:`virtual machine` is a software that imitates a certain other software
(usually an operating system or environment) on a certain hardware. For our
purposes however, it can be thought of as an operating system running in an
operating system. Virtual machines are useful because they allow software tasks
to be undertaken in precisely defined environments with little repercussion on
the host system they run on. These machines themselves can be described by
single files representing the equivalent of a hard disk of the machine, as well
as a description of the hardware that the virtual machine emulates.

Virtual machines must be supported by software in order to function. Only
provider software is necessary to run a virtual machine, but managers and
provisioners are useful for creating virtual machines and virtual environments
respectively.

.. _software-providers:

Providers
---------

Virtual machine providers are virtualiser software that supports creating,
running, destroying, and other interaction with :term:`virtual machine`\s on
your computer. VirtualBox (https://www.virtualbox.org) is an example of a
virtual machine provider that is open source and freely available under the GNU
GPL (https://www.gnu.org/copyleft/gpl.html), and is the provider supported by
this project. Other popular provider software includes VMWare, KVM, and Docker.
While many cloud computing organisations use virtual machines, they typically
use existing provider software.

.. _software-managers:

Managers
--------

While not essential for starting :term:`virtual machine`\s, specialist software
is useful for managing :term:`virtual environment`\s. Vagrant
(www.vagrantup.com) is an example of a virtual machine manager. It provides a
command-line interface to the creation and provision of virtual machines from
virtual environments. HashiCorp, the company behind Vagrant, also provides a
framework for sharing virtual environments. Most importantly for our purpose,
Vagrant can be automated to generate virtual machines containing an environment
without user intervention. This environment can then be used to complete our
objectives. To specify this environment however, provisioning software is
required.

.. _software-provisioners:

Provisioners
------------

Machines, virtual or otherwise, are created to serve a purpose. Machines must
be provisioned with software and settings if they are to satisfy their
purpose. For simple cases one could run a script on the machine to install
software and configure it for use, but for larger projects it is prudent to use
a provisioner. Provisioner software runs a set of commands on a machine to
ensure it is in a particular state. Ansible (<!>) is a Python-based provisioner
software that uses Yet Another Markup Language (YAML) to ensure the state of a
system in an :term:`idempotent` manner. Other popular provisioner software
inclues Puppet, Salt, and Chef, but any scriptable language can ultimately be
used as a provisioner

.. _software-summary:

Summary
-------
