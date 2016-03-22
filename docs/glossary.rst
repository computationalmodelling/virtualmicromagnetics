Glossary
========

.. glossary::

   Box File
       A file used by :term:`Vagrant` to create :term:`Vagrant
       environment`\s. A box file represents a template from which
       :term:`Virtual machine`\s can be created.

   Host
   Host Machine
       A machine that uses virtualisation software to host :term:`virtual
       machine`\s. Host machines allocate resources, including memory and disk
       space, to support the running of a virtual machine. Note that a virtual
       machine can host other virtual machines, making it both a host and
       virtual machine.

   Idempotent
   Idempotency
       <!>

   Manager
   Vagrant
       Manager software provides an interface for managing :term:`Virtual
       machine`\s from :term:`Virtual environment`\s. Vagrant is an example of
       manager software, which provides a command-line interface to virtual
       machine management which can be automated. See
       :ref:`introduction-managers`.

   Vagrant Environment
       The directory structure (including ``Vagrantfile``) created by Vagrant
       when ``vagrant init`` is commanded. A single virtual machine can be
       managed in a given environment.

   Virtual Environment
       Virtual environments produce the same :term:`virtual machine` on all
       virtualisation-capable computers. Virtual environments are also
       :term:`box file`\s, but are not :term:`Vagrant environment`\s.

   Provider
   Virtualiser
   VirtualBox
       Provider (or virtualiser) software supports the creation of, and
       interaction with, :term:`virtual machine`\s from a host
       machine. VirtualBox is an example of a free provider software. See
       :ref:`introduction-providers`.

   Provisioner
   Provisioning
   Ansible
       Provisioner software runs a set of commands on a machine, virtual or
       otherwise, to ensure it is in a particular state. Ansible is an example
       of provisioner software that enables :term:`idempotent`
       provisioning. See :ref:`introduction-provisioners`.

   System Virtual Machine
   Virtual Machine
       "An efficient, isolated duplicate of a real machine." [#smith05]_

       Software that imitates certain other software on certain hardware. In
       this project, this includes a complete operating system, and a
       combination of one or many simulation packages and dependencies. General
       system virtual machines are described in brief at
       :ref:`introduction-vms`.

       More strictly, a virtual machine is a specific instance of a
       :term:`virtual environment`. When we build :term:`box file` artefacts,
       we are creating :term:`virtual environment`\s, not virtual
       machines. Once :term:`Vagrant` creates a :term:`Vagrant environment`
       from a :term:`box file` and ``vagrant up`` is commanded, a corresponding
       virtual machine is created. Virtual machines created on a :term:`host`
       are managed by virtual machine :term:`provider`\s, which typically list
       the machines they are maintaining.

   Virtual Micromagnetics
       "Enabling accessible and reproducible micromagnetic simulation."

       The name of this project, which represents the collection of virtual
       environments and the software written to create them.

.. rubric:: References

.. [#smith05] Smith, J., Nair, R. (2005). "The Architecture of Virtual
   Machines". Computer (IEEE Computer Society) 38 (5): 32–38.
   doi:10.1109/MC.2005.173
