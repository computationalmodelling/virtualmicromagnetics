Glossary
========

.. glossary::

   Box File

   Vagrant

   Vagrant Environment

   Virtual Environment
       See :term:`box file`, not to be confused with :term:`Vagrant
       environment`.

   Provider
   Virtual Machine Provider

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
       virtual machine is created. Virtual machines created on a host are
       managed by :term:`virtual machine provider`\s, which typically list the
       machines they are maintaining.

   Virtual Micromagnetics
       "Enabling accessible and reproducible micromagnetic simulation."

       The name of this project, which represents the collection of virtual
       environments and the software written to create them.

.. rubric:: References

.. [#smith05] Smith, J., Nair, R. (2005). "The Architecture of Virtual
   Machines". Computer (IEEE Computer Society) 38 (5): 32–38.
   doi:10.1109/MC.2005.173
