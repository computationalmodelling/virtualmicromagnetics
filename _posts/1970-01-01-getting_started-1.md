---
layout: default
category: 'Getting Started'
title: With Vagrant (and VirtualBox)
---

The intended way to use the Virtual Micromagnetics environment is through
[Vagrant](https://www.vagrantup.com/) using
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) as a provider (see
[About](/virtualmicromagnetics/about/)). Commanding the following in an empty
directory with Vagrant and VirtualBox installed will download and run the full
Virtual Micromagnetics environment:

    vagrant init virtualmicromagnetics/full
    vagrant up --provider virtualbox

and for the lite environment:

    vagrant init virtualmicromagnetics/lite
    vagrant up --provider virtualbox