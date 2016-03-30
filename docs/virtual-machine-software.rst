.. _software:

Virtual Machines and Related Software
=====================================

In :ref:`getting-started-user`, we created a :term:`virtual machine` based on
the Full :term:`Virtual Micromagnetics` environment using a virtual machine
:term:`provider` and :term:`manager`. Here, we detail some of the underlying
mechanisms of :term:`virtual machine` creation, what providers, managers, and
:term:`provisioner`\s are, and how virtual machines and :term:`virtual
environment`\s are related through these virtual machine software.

Virtual Machines
----------------

A :term:`virtual machine` is a software that imitates a certain other software,
usually an operating system or environment, on a certain hardware. For our
purposes however, it can be thought of as an operating system running in an
operating system. Virtual machines are useful because they allow software tasks
to be undertaken in precisely defined environments with little repercussion on
the host system they run on. These machines themselves can be described by
single files representing the equivalent of a hard disk of the machine, as well
as a description of the hardware that the virtual machine emulates. This makes
them simple to distribute.

Virtual Machine Software
------------------------

Virtual machines must be supported by software in order to function. Only
provider software is necessary to run a virtual machine, but managers and
provisioners are useful for creating virtual machines and virtual environments
respectively.

.. _software-providers:

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

.. _software-managers:

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

.. _software-provisioners:

Provisioners
~~~~~~~~~~~~

Provisioning is the action of running select commands on a machine, virtual or
otherwise, to reach a desired end state. By "state", here we mean how storage
is populated with packages, environment definitions, and more. The user of a
provisioner describes the desired state of the system, and the provisioner
makes it so. In the absence of a provisioner, shell commands can be executed to
specify the state, but this becomes unwieldy for large projects because focus
is placed on the instructions needed to obtain the desired state, as opposed to
the state itself. Provisioning software, such as Ansible (www.ansible.com)
alleviates this problem. Ansible uses Yet Another Markup Language (YAML) to
describe plays to run on a machine to enact the desired end state. Since the
focus is on the end state of the system, :term:`idempotency` is essential.

.. _software-summary:

Summary
-------

:term:`Virtual machine`\s imitate hardware and software, but must be hosted on
a :term:`host machine`. Virtual machines are provided by :term:`provider`
software running on the host machine, and can be provisioned for use by a
:term:`provisioner` software. :term:`Manager` software links these two
concepts, allows the virtual machine to be preserved and distributed as a
:term:`virtual environment`, and simplifies the creation of virtual machines.

You are now ready to :ref:`get started as a
poweruser<getting-started-poweruser>`, which explains how to create custom
environments containing software you choose, as well as instructions for adding
new software or configuring your own virtual environment.
