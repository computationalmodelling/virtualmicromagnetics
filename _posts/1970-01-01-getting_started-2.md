---
layout: default
category: 'Getting Started'
title: With Docker
---

Virtual Micromagnetics container environments also exist through
[Docker](https://www.docker.com/). Commanding this will download and run the
lite Virtual Micromagnetics container environment in a terminal on your
machine:

    docker run -ti virtualmicromagnetics/lite:release /bin/bash -l

The complete list of Virtual Micromagnetics container environments can be found
[here](https://hub.docker.com/u/virtualmicromagnetics). For example, to
download and run the Nmag Virtual Micromagnetics container environment:

    docker run -ti virtualmicromagnetics/nmag:release /bin/bash -l
