---
layout: default
category: 'Getting Started'
title: With Vagrant (and VirtualBox)
---

You can also use Virtual Micromagnetics environments through
[Vagrant](https://www.vagrantup.com/). Commanding the following in an empty
directory will download and run the full Virtual Micromagnetics environment:

    vagrant init virtualmicromagnetics/full
    vagrant up --provider virtualbox

and for the lite environment:

    vagrant init virtualmicromagnetics/lite;
    vagrant up --provider virtualbox