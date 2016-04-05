---
layout: default
category: 'Getting Started'
title: With Vagrant (and VirtualBox)
---

The intended way to use the Virtual Micromagnetics environment is through
[Vagrant](https://www.vagrantup.com/) using
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) as a provider (see
[About](/about/)). Commanding the following in an empty directory with Vagrant
and VirtualBox installed will download and run the full Virtual Micromagnetics
environment:

    vagrant init virtualmicromagnetics/full
    vagrant up --provider virtualbox

The complete list of virtualmicromagnetics environments can be found
[here](https://atlas.hashicorp.com/virtualmicromagnetics). For example, to
download and run the OOMMF Virtual Micromagnetics environment:

    vagrant init virtualmicromagnetics/oommf
    vagrant up --provider virtualbox