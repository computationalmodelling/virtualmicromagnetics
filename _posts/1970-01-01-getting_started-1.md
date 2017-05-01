---
layout: default
category: 'Getting Started'
title: With Vagrant (and VirtualBox)
---

The intended way to use the Virtual Micromagnetics environment is through
[Vagrant](https://www.vagrantup.com/) using
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) as a provider (see
[About](/about/)). Commanding the following in an empty directory with Vagrant
and VirtualBox installed will download and run the lite Virtual Micromagnetics
environment:

    vagrant init virtualmicromagnetics/lite
    vagrant up --provider virtualbox

The complete list of Virtual Micromagnetics environments can be found
[here](https://atlas.hashicorp.com/virtualmicromagnetics). For example, to
download and run the OOMMF Virtual Micromagnetics environment:

    vagrant init virtualmicromagnetics/oommf
    vagrant up --provider virtualbox

While you're in the Virtual Micromagnetics environment, you're active as a user
with the following credentials:

- User: virtualmicromagnetics
- Password: virtualmicromagnetics
