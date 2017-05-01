.. _environments:

Virtual Micromagnetics Environments and Simulation Software
===========================================================

In :ref:`getting-started-user`, we created a :term:`virtual machine` based on
the Full :term:`Virtual Micromagnetics` environment. Here, we detail the
micromagnetic simulation packages and other software supported and used by
Virtual Micromagnetics, and we describe the list of available Virtual
Micromagnetics environments.

Software
--------

The following micromagnetic simulation packages are supported by Virtual
Micromagnetics:

 - OOMMF (http://math.nist.gov/oommf/)
 - MagPar (http://www.magpar.net/)
 - Nmag (http://nmag.soton.ac.uk/nmag/)
 - Fidimag (http://computationalmodelling.github.io/fidimag/)

Each environment that uses a simulation package also contains its examples, and
a link to its documentation page which can be opened in the virtual
machine. The following infrastructure software is also used in all
environments:

 - Ubuntu (http://www.ubuntu.com/) 14.04
 - XFCE4 (http://www.xfce.org/)
 - Python (https://www.python.org/) 2.7, IPython (http://ipython.org/)

Environments
------------

The Full environment contains all simulation packages supported by Virtual
Micromagnetics, as well as dependencies requested by our users, including:

 - Cython(http://cython.org/)
 - FEniCS (http://fenicsproject.org/)
 - Gmsh (http://gmsh.info/)
 - Netgen (https://sourceforge.net/projects/netgen-mesher/)
 - ParaView (http://www.paraview.org/)
 - Sundials (http://acts.nersc.gov/sundials/)

We recognise that many of our users will not require these tools. To that end,
a "Lite" environment can be used instead, which contains all of the simulation
packages the Full environment does, without these optional packages. To
download and use the Lite Virtual Micromagnetics environment, command::

  vagrant init virtualmicromagnetics/lite
  vagrant up --provider virtualbox

Note that this is syntactically similar to the command used in
:ref:`getting-started-user`, and can be adapted for all other Virtual
Micromagnetics environments. Environments exist for specific simulation
packages, such as "virtualmicromagnetics/oommf". The following table shows the
list of environments available under Virtual Micromagnetics, and the software
they contain:


+--------------------------+----+----+-----+------+----+-------+
| Software vs. Environment |Full|Lite|OOMMF|Magpar|Nmag|Fidimag|
+=================+========+====+====+=====+======+====+=======+
|Micromagnetic    | OOMMF  | ✔  | ✔  |  ✔  |      |    |       |
|                 +--------+----+----+-----+------+----+-------+
|                 | Magpar | ✔  | ✔  |     |  ✔   |    |       |
|                 +--------+----+----+-----+------+----+-------+
|                 | Nmag   | ✔  | ✔  |     |      | ✔  |       |
|                 +--------+----+----+-----+------+----+-------+
|                 |Fidimag | ✔  | ✔  |     |      |    |   ✔   |
+-----------------+--------+----+----+-----+------+----+-------+
|Infrastructure   | Ubuntu | ✔  | ✔  |  ✔  |  ✔   | ✔  |   ✔   |
|                 +--------+----+----+-----+------+----+-------+
|                 |  XFCE  | ✔  | ✔  |  ✔  |  ✔   | ✔  |   ✔   |
|                 +--------+----+----+-----+------+----+-------+
|                 |Python 2| ✔  | ✔  |  ✔  |  ✔   | ✔  |   ✔   |
|                 +--------+----+----+-----+------+----+-------+
|                 |IPython | ✔  | ✔  |  ✔  |  ✔   | ✔  |   ✔   |
+-----------------+--------+----+----+-----+------+----+-------+
|Other            | Cython | ✔  |    |     |      |    |       |
|                 +--------+----+----+-----+------+----+-------+
|                 | FEniCS | ✔  |    |     |      |    |       |
|                 +--------+----+----+-----+------+----+-------+
|                 |  Gmsh  | ✔  |    |     |      |    |       |
|                 +--------+----+----+-----+------+----+-------+
|                 | Netgen | ✔  |    |     |      |    |       |
|                 +--------+----+----+-----+------+----+-------+
|                 |ParaView| ✔  |    |     |      |    |       |
|                 +--------+----+----+-----+------+----+-------+
|                 |Sundials| ✔  |    |     |      |    |       |
+-----------------+--------+----+----+-----+------+----+-------+

See :ref:`getting-started-poweruser` if more fine-grained control over your
software interests you. However, we firstly recommend reading
:ref:`vm-software` to understand more about :term:`virtual machine`\s,
:term:`virtual environment`\s, and the software used to create them in the
Virtual Micromagnetics project.
