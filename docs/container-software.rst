.. _container-software:

Containers and Related Software
===============================

In :ref:`getting-started-user`, we created a :term:`container` in addition to a
:term:`virtual machine` based on the Full :term:`Virtual Micromagnetics`
environment. This page talks about containers and how the
:term:`provider`\-:term:`manager`\-:term:`provisioner` model applies to
container creation. We recommend reading :ref:`vm-software`, if you have not
already.

Containers and Images
---------------------

A :term:`container` is a virtualisation mechanism similar to a :term:`virtual
machine`\, in that it allows users to run software in a controlled environment
with a cap on available computing resources (like memory). Where a virtual
machine contains the entire software stack above and including the operating
system, a container uses the operating system and kernel of the host machine to
produce its environment. Containers are created from :term:`image`\s (container
templates, analogous to :term:`box file`\s) to run a single process, and are
usually destroyed once that process has been completed.

Images can be distributed to other users so that they can run :term:`Virtual
Micromagnetics` environments from a container.

Software Related to Containers
------------------------------

As with :term:`virtual machine`\s, :term:`container`\s require supporting
software to function. The
:term:`provider`\-:term:`manager`\-:term:`provisioner` model outlined for
virtual machines in :ref:`vm-software` also applies to containers as follows:

 - Provisioner: Ansible is also used to provision containers. In :term:`Virtual
   Micromagnetics`, scripts to provision containers and virtual machines with
   software are very similar, encouraging code reuse.

 - Manager: Vagrant is used to manage containers in this project in a similar
   way to how virtual machines are managed. An exception is that Vagrant can
   only be used to host :term:`box file`\s, meaning another hosting method is
   needed for :term:`images`.

 - Provider: Docker is used in Virtual Micromagnetics to create containers for
   simulation (as the user) and for provisioning (as the poweruser). Docker
   also supports online hosting of images; this is used in Virtual
   Micromagnetics as a distribution method.

Summary
-------

:term:`Container`\s are another virtualisation mechanism, like :term:`virtual
machines`. Containers virtualise fewer elements of the software stack so they
are smaller, but consequently impose more requirements on the :term:`host
machine`. Like virtual machines, containers can be provisioned, managed, and
distributed.

You are now ready to :ref:`get started as a
poweruser<getting-started-poweruser>`, which explains how to create custom
environments containing software you choose, as well as instructions for adding
new software or configuring your own virtual environment.
