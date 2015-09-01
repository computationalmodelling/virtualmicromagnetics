Objective
=========

To use virtual machine software VirtualBox and vagrant, and provisioning
software Ansible, to produce an environment suitable for micromagnetic
simulation.

Example Artefact
================

A successful Virtual Micromagnetics machine is available at the following
temporary link. To use the machine, download and unzip the file, and follow
the instructions in the README. VirtualBox, or another virtual machine
provider is needed to use the virtual hard disk file in the ZIP file.

https://www.dropbox.com/s/1wzqdh6j2iau50u/virtualmicromagnetics_full_9df447e4cc.zip?dl=0

Quick Start
===========

To get started with this repository and creating virtual machines without
understanding the underlying concepts, simply adhere to the "Requirements"
section below and use the Makefile as described in the "How to Use" section
following it.

Just remember that there is no shortcut to work done true and well.

Introduction to Concepts
========================

A number of different concepts interplay in this repository, so a brief
introduction to them is provided here.

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

Requirements
============

This repository was developed on and designed for use by Ubuntu GNU/Linux, but
should be usable by anyone using GNU/Linux and enough modification and
persistence. The following software are required to use this repository for its
intended purpose:

  - 2.6 <= Python < 3.0
    > A note for bleeding-edge distribution users like ArchLinux; Ansible
      doesn't like Python 3.0. You may need to create a virtualenv
      (https://pypi.python.org/pypi/virtualenv) to ensure you are working with
      an older python version
  - VirtualBox >= 5.0
    > available from https://www.virtualbox.org/wiki/downloads
  - Vagrant >= 1.7.4
    > available from https://www.vagrantup.com/downloads
  - Ansible >= 1.9
    > available from the python package index (https://pypi.python.org/pypi).
  - thydel.patch Ansible role
    > command "ansible-galaxy install thydel.patch -proles/" from the
      virtualmicromagnetics directory.
  - yaegashi.blockinfile Ansible role
    > command "ansible-galaxy install yaegashi.blockinfile -proles/" from the
      virtualmicromagnetics directory.

The following software is recommended:

  - Cowsay

How to Use
==========

Now that you have prepared your host machine by following the "Requirements"
section, you will probably want to build a virtual machine. By way of example,
if you want the full virtualmicromagnetics experience, command:

  make full

This Makefile uses the master.yml playbook, which runs the "create_vm"
role. This will create a virtual machine and provision it with the playbook
passed as a command-line argument in the makefile, which should live in the
jobs directory (see "Where things are" below). It will also do some
post-provisioning tasks using the hookbook, again passed as a command-line
argument. The fundamental difference between the playbook and the hookbook is
that the playbook is run on the guest virtual machine by vagrant, and the
hookbook is run on the host machine. Different Makefile targets may place
different build artefacts in the artefacts directory (see 'Where Things Are'
and 'Artefacts').

Artefacts
=========

After running a job from the Makefile, certain build artefacts may be
created. At present only *.vhd (virtual hard disk) files are created, but other
file types could be produced by future jobs. These files are to be used with
virtual machine providers, such as VirtualBox. To use these files with the
VirtualBox GUI, build a "New" machine with an 64 bit Ubuntu OS, and supply as
much RAM as you are able. All virtual machines in this repository are built off
such an operating system. The username/password for the virtual machine is
defined in roles/add_super_user/vars/main.yml, but both are
"virtualmicromagnetics" by default.

Where Things Are
================

In order to add jobs, one should edit the Makefile. In order to do that, one
would need to know where things are, hence the purpose of this section. This
repository is structured as follows:

  - Makefile: This is the makefile through which all jobs are conducted.

  - ansible.cfg and inventory.txt: These files are used by Ansible when the
    master.yml playbook is run. They contain configuration information.

  - roles/: This directory contains roles (obviously). Each role is given a
    subdirectory, and should not overlap. Each role directory contains
    tasks, and may also contain the subdirectories:

    - vars/ (variable definitions),
    - templates/ (files to duplicate to the guest virtual machine),
    - meta/ (metadata, such as role dependencies),
    - files/ (files used by tasks that aren't covered by the usecases of
      templates)

    as well as others we haven't thought of yet.

  - jobs/: This directory contains playbooks and directories that can be
    thought of as jobs in the Makefile. They are either provisioning playbooks,
    or post-provisioning hookbooks.

  - machines/: This directory is created by the Makefile, and houses the
    vagrant environment for each individual virtual machine. The provision
    process is recorded to a log file in the machine's directory (for example,
    the provision log for the lite build job exists in
    machines/virtualmicromagnetics-lite/virtualmicromagnetics-lite.log)

  - artefacts/: This directory is created by the Makefile, and houses build
    artefacts.

Postamble
=========

See LICENSE.md for licensing details regarding distribution and
liability. These tools are provided by the University of Southampton (Mark
Vousden, Max Albert, Hans Fangohr and others). Neither the University of
Southampton nor the authors assume any responsibility whatsoever for its use by
other parties, and makes no guarantees, expressed or implied, about its
quality, reliability, or any other characteristic.

List of Things to do
====================

  - Learn how YAML linebreaks work, and reduce the lengths of lines to <80
    characters.
  - Make syntax more consistent.
