# Virtualmicromagnetics

## For users who want to run micromagnetic simulations

This project provides a ready-built virtual machine to run micromagnetic simulations. The following open source software packages are provided

* OOMMF 1.2a5 (The Object Oriented MicroMagnetic Framework): http://math.nist.gov/oommf/

  Documentation: http://math.nist.gov/oommf/doc/

* Nmag 0.2.1: http://nmag.soton.ac.uk/nmag/

  Documentation: http://nmag.soton.ac.uk/nmag/current/manual/singlehtml/manual.html

* Magpar 0.9 (Parallel Finite Element Micromagnetics Package): http://www.magpar.net/

  Documentation: http://www.magpar.net/static/magpar-0.9/doc/html/


If you need to use one of these packages, and you prefer not to install them directly in your computer, you can

1. Download the Virtualbox software: virtualbox is a program that allows running another (virtual) machine inside your real computer; the software pretends to be a real computer to the virtual machine operating system. For the real computer, which is generally called the 'host', virtualbox is just a program amongst many others. The virtual machine operating system and programs don't know they are executing in a virtual environment.

2. Download the [virtualmicromagnetics disk image](https://www.dropbox.com/s/1wzqdh6j2iau50u/virtualmicromagnetics_full_9df447e4cc.zip?dl=0). Once done, you can create a virtual machine (see SECTION TO BE WRITTEN) from this disk image.

3. Start the virtual machine, switch to full screen (if you like) and run your micromagnetic simulations in OOMMF, Magpar or Nmag in this virtual environment.


## For those who want to update/extend the automatic creation of this virtualbox 

Please read [docs/creating-virtual-machines.md](https://github.com/fangohr/virtualmicromagnetics/blob/master/creating-virtual-machines.md)

## FAQ

* Isn't a virtual machine slow when executing?

Not necessarily - modern CPUs support virtualisation with high efficiency.

* What operating system does the virtual machine run?

We have chosen Ubuntu Linux here as research codes often install (only or) better on Linux based systems.

* What does the virtual machine look like?

[insert snapshopt of virtual machine in window in host OS Desktop], [insert snapshot of full screen session, showing OOMMF session with TkWindows, maybe]
