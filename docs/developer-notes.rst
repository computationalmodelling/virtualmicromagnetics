.. _dev-notes:

Developer Notes (valid for version 1.0.2)
=========================================

In :ref:`getting-started-poweruser`, we created a virtual environment from
scratch that can be shared with other users. Here, we show how you can
completely specify your own environment. Knowledge of Ansible is needed, which
can be gleaned from their excellent documentation at
http://docs.ansible.com/ansible/.

.. _dev-build-process:

Overview
--------

.. image:: images/graph.png

The Build Process
-----------------

The build (make) process in step 3 in :ref:`getting-started-poweruser` allowed
us to create a virtual environment. The Makefile in the software repository can
build multiple targets. Each target runs Ansible on the ``master.yml``
playbook, which in turn runs the ``create_vm`` role in the roles
directory. This creates a virtual machine and provisions it with the playbook
passed as a command-line argument in ``Makefile``, which lives in the jobs
directory. It will also do some post-provisioning tasks using the hookbook,
again passed as a command-line argument. The fundamental difference between the
playbook and the hookbook is that the playbook is run on the guest virtual
machine by vagrant, and the hookbook is run on the host machine. Different
Makefile targets may place different build artefacts in the artefacts
directory.

Roles add or configure software, playbooks describe the roles that must be
enacted to provision the machine, hookbooks describe what to do with that
machine (like creating a :term:`box file`), and jobs are Makefile targets that
produce certain machines.

To add a new environment, one needs to add a job that follows the pattern of
existing jobs.

Where Things Are
----------------

In order to add jobs, one should edit ``Makefile``. In order to do that, one
would need to know where things are, hence the purpose of this section. The
:term:`virtual micromagnetics` repository is structured as follows:

  - ``Makefile``: This is the Makefile through which all jobs are conducted.

  - ``ansible.cfg`` and ``inventory.txt``: These files are used by Ansible when
    the master.yml playbook is run. They contain configuration information.

  - ``roles/``: This directory contains roles (obviously). Each role is given a
    subdirectory, and should not overlap. Each role directory contains tasks,
    and may also contain the subdirectories:

    - ``vars/`` (variable definitions),
    - ``templates/`` (files to duplicate to the guest virtual machine),
    - ``meta/`` (metadata, such as role dependencies),
    - ``files/`` (files used by tasks that aren't covered by the usecases of
      templates)

  - ``jobs/``: This directory contains playbooks and directories that can be
    thought of as jobs in ``Makefile``. They are either provisioning playbooks,
    or post-provisioning hookbooks.

  - ``machines/``: This directory is created by ``Makefile``, and houses the
    vagrant environment for each individual virtual machine. The provision
    process is recorded to a log file in the machine's directory (for example,
    the provision log for the lite build job exists in
    machines/virtualmicromagnetics-lite/virtualmicromagnetics-lite.log)

  - ``artefacts/``: This directory is created by ``Makefile``, and houses build
    artefacts.

An Example
----------

Lets create a custom machine that contains Fidimag, but no X server called
doc-example. Firstly, we add a target to ``Makefile`` (run from the repository
root directory)::

  printf "
  # This target builds a virtual hard disk file containing an OOMMF and Fidimag
  # installation.
  doc-example:
      ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars=\"vm_name=virtualmicromagnetics-doc-example playbook=provision_virtualmicromagnetics_doc-example.yml hookbook=hook.yml extra_resources_dir=guest_resources/\"
  " >> Makefile

Now we need to describe what the state of the machine should be, by modifying
playbook `provision_virtualmicromagnetics_doc-examples.yml`::

  printf "
  ---
  # This Ansible playbook is a provision playbook designed to be used with
  # vagrant. This playbook provisions a machine suitable for micromagnetic
  # simulation with fidimag. It is executed by the virtual machine.

  - hosts: all

    vars:
      vm_name: virtualmicromagnetics-doc-example

    roles:
      - fidimag
      - fidimag_examples
      - add_super_user
      - { role: set_hostname, HOSTNAME: \"{{ vm_name }}\" }
  " > jobs/provision_virtualmicromagnetics_doc-example.yml

Now we are ready to build the environment by commanding (again, from the repository root directory)::

  make doc-example

This creates another :term:`virtual environment` in the artefacts directory.

Adding Software
---------------
