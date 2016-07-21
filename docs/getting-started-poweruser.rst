.. _getting-started-poweruser:

Getting Started: As a Poweruser
===============================

In :ref:`environments`, we learned about the different :term:`Virtual
Micromagnetics` environments available to users, which bundle sets of
configured software. Here we outline how you can create virtual environments
yourself, which you can distribute to others. We recommend reading
:ref:`vm-software`, if you have not already.

To create a new, custom :term:`virtual environment`, you will need the
following software in addition to the software list in
:ref:`getting-started-user`:

- A GNU/Linux operating system (we use Ubuntu, https://www.ubuntu.com)
- 2.7 <= Python < 3.0 (https://www.python.org/)
- 1.9 <= Ansible < 2.0 (https://www.ansible.com/)

With this software:

1. Grab a copy of Virtual Micromagnetics. You can do this via Git by cloning
   our repository with ``git clone -b release
   https://github.com/computationalmodelling/virtualmicromagnetics.git``, or by
   grabbing a release version at
   https://github.com/computationalmodelling/virtualmicromagnetics/releases

2. Install some sub-packages:

   - Ansible role "blockinfile"; command ``ansible-galaxy install
     yaegashi.blockinfile -proles/`` from the Virtual Micromagnetics software
     directory

   - Vagrant plugin "vagrant-vbguest"; command ``vagrant plugin install
     vagrant-vbguest``

3. Make, with ``make`` from the Virtual Micromagnetics software directory, with
   an Internet connection.

After time of the order of hours, you should find a :term:`box file` at
``./artefacts/virtualmicromagnetics-full-*.box``. If not, see
:ref:`troubleshooting` for more help. If so, congratulations on building your
first Virtual Micromagnetics environment! This file represents your virtual
environment, which you can share with other users. You can use this environment
yourself by commanding the following in an empty directory::

 vagrant init $PATH_TO_BOX_FILE
 vagrant up --provider virtualbox

where ``$PATH_TO_BOX_FILE`` is the aforementioned artefact file. Now that you
can create :term:`virtual environment`\s, see :ref:`dev-notes` to learn how to
customise the software you place on them.
