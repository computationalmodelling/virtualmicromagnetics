Virtual Micromagnetics Documentation
====================================

.. image:: images/virtual_micromagnetics_logo.png
   :scale: 50%
   :align: right
   :target: http://virtualmicromagnetics.org

Welcome to the :term:`Virtual Micromagnetics` project, where we aim to enable
accessible and reproducible micromagnetics simulation, without compromise.

Provided by Mark Vousden, Hans Fangohr, and others at the University of
Southampton. Funded by EPSRC's DTC grant EP/G03690X/1. The license for this
software is available `here
<https://github.com/computationalmodelling/virtualmicromagnetics/blob/development/LICENSE.md>`_.

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

Contents
--------

.. toctree::
   getting-started-user
   environments-software
   virtual-machine-software
   container-software
   getting-started-poweruser
   developer-notes
   troubleshooting
   glossary

.. figure:: images/oommf-simulation-1.png

   OOMMF running in :term:`Virtual Micromagnetics`.
