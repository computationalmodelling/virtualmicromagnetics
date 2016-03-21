.. _introduction:

Introduction
============

Welcome to the :term:`Virtual Micromagnetics` project, where we aim to enable
accessible and reproducible micromagnetics simulation, without compromise.

.. _introduction-overview:

Overview
--------

The :term:`Virtual Micromagnetics` project creates :term:`virtual
environment`\s that run micromagnetic (and in some cases, atomistic)
simulations of magnetic behaviour. These environments produce :term:`system
virtual machine`\s which emulate a configured set of software on your
computer. This means you as a user only need to manage the software to support
the virtual machine, as opposed to the complicated set of dependencies most
simulation packages require. As a result, these virtual environments are far
simpler to maintain, meaning you have more time to solve the mysteries of the
universe instead of:

 - wondering why the latest version of a package is incompatible with earlier
   simulations.

 - wondering how to maintain multiple versions of a package to support old
   simulation software.

 - persuading your high-performance computing system administrator to support
   your long list of software dependencies.

 - setting up user accounts and packages for new students to run simulations.

.. _introduction-vms:

Virtual Machines
----------------

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

.. _introduction-providers:

Providers
~~~~~~~~~

Virtual machine providers are virtualiser software that supports creating,
running, destroying, and other interaction with :term:`virtual machine`\s on
your computer. VirtualBox (https://www.virtualbox.org) is an example of a
virtual machine provider that is open source and freely available under the GNU
GPL (https://www.gnu.org/copyleft/gpl.html), and is the provider supported by
this project. Other popular provider software includes VMWare, KVM, and Docker.
While many cloud computing organisations use virtual machines, they typically
use existing provider software.

.. _introduction-managers:

Managers
~~~~~~~~

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

.. _introduction-provisioners:

Provisioners
------------
