.. _software:

Virtual Machines and Other Software
===================================

A :term:`virtual machine` is a software that imitates a certain other software,
usually an operating system or environment, on a certain hardware. For our
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
