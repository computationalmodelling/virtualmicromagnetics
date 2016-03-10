Introduction to Environment-Building Concepts
=============================================

A number of different concepts interplay in the Virtual Micromagnetics project,
so a brief introduction to them is provided here.

Virtual Machines
----------------

A virtual machine is a software that imitates a certain other software (usually
an operating system or environment) on a certain hardware. For our purposes
however, it can be thought of as an operating system running in an operating
system. Virtual machines are useful because they allow software tasks to be
undertaken in precisely defined environments with little repercussion on the
host system they run on. These machines themselves can be described by single
files representing the equivalent of a hard disk of the machine, as well as a
description of the hardware that the virtual machine emulates.

VirtualBox (www.virtualbox.org) is a virtualizer software that can create and
manage virtual machines, and is open source and freely available under the GNU
GPL (https://www.gnu.org/copyleft/gpl.html) at time of writing. It is a
"provider" of virtual machines. Other popular provider software includes VMWare
and KVM.

Vagrant (www.vagrantup.com) is a wrapper around multiple pieces of software. It
provides a command-line interface to the creation and provision of virtual
machines, and provides a framework in which virtual machines can be easily
shared. Most importantly for our purpose, this interfacing can be automated to
generate virtual machines containing an environment without user
intervention. This environment can then be used to complete our objectives. To
specify this environment however, provisioning software is required.

Provisioning
------------

In the context of virtual machines, provisioning is the action of taking an
existing virtual machine, and running select commands on it to result in a
desired end-state. By "state", here we mean how storage is populated with
packages, environment definitions, and more. The user of a provisioner
describes the desired state of the system, and the provisioner makes it so. In
the absence of a provisioner, shell commands can be executed by Vagrant to
specify the state of the system, but for large projects this becomes unwieldy
because focus is placed on the instructions needed to obtain the desired state,
as opposed to the state itself. Since nobody really likes to write large
projects in shell, a provisioner is recommended.

Ansible (www.ansible.com) is a provisioner supported by Vagrant. It uses YAML
syntax to describe plays to run on a remote system to define the
environment. Since the focus is on the end-state of the system, idempotency a
strong design concern, meaning that tasks only need to be run to achieve a
change in the state, and are not run if they do not change the state or obtain
information about it. Plays are described by playbook files, and may contain
many roles; hence the existence of a "roles" directory in this
repository. Roles are a way of breaking down a play into sensible sentence-like
instructions, which in turn contain a number of tasks. Examples of role
descriptions include "Install magpar." and "Configure passwordless SSH for
BitBucket access."

In addition to provisioning virtual machines, Ansible is a general framework
for running instructions to define a state on any machine. This means that
Ansible can be (and is) used by a host to create virtual machines using
vagrant. This is convenient due to its inherent idempotency; a virtual machine
need not be created and defined again from scratch if it already exists.

Tying it together
-----------------

To conclude, virtual machines are created in this repository to produce build
artefacts. Ansible is used to define the state of virtual machines, which are
managed by Vagrant. Vagrant commands VirtualBox to create and internally manage
virtual machines in an automated way. These virtual machines are in turn
provisioned by Ansible to define their internal state. Once this provisioning
has happened, a build artefact is produced according to the desired objective.
