#!/usr/bin/python2

# The purpose of this script is to create a graph that shows the processes
# involved for the user.

from graphviz import Digraph
import subprocess

# Node properties
font = "verdana"

envNodeProps = {"shape": "egg", "fontname": font, "fillcolor": "lavender",
                "margin": "0.1, 0.1", "style": "filled"}
machNodeProps = {"fontname": font, "fillcolor": "skyblue", "style": "filled"}
graphProps = {"fontname": font}

# Edge properties
vagrant = "purple"
vboxVagrant = "blue"
ansible = "red"

# Create user graph.
userGraphName = "User"
userGraphColour = "lightpink1"
userGraph = Digraph(name="user")
userGraph.body.append("label = \"{}\"".format(userGraphName))
userGraph.body.append("style = filled")
userGraph.body.append("fillcolor = {}".format(userGraphColour))

# Define user graph nodes and edges.
outputEnv = "Output Environment\n(at atlas.hashicorp.com)"
userMach = "User's Virtual\nMachine"
userGraph.node(outputEnv, **envNodeProps)
userGraph.node(userMach, **machNodeProps)
userGraph.edge(outputEnv, userMach, "Vagrant and\nVirtualBox Creates",
               {"color": "blue", "fontname": font})

# Create developer graph.
devGraphName = "Developer"
devGraph = Digraph(name="dev")

# Define developer graph nodes and edges.
inputEnv = "Input\nEnvironment"
devMach = "Developer's\nVirtual Machine"
devGraph.node(outputEnv, **envNodeProps)
devGraph.node(inputEnv, **envNodeProps)
devGraph.node(devMach, **machNodeProps)
devGraph.edge(inputEnv, devMach, "Vagrant and\nVirtualBox Creates",
              {"color": vboxVagrant, "fontname": font, "rank": "same"})
devGraph.edge(devMach, devMach, "Ansible\nProvisions",
              {"color": ansible, "fontname": font})
devGraph.edge(devMach, outputEnv, "Vagrant\nPackages",
              {"color": vagrant, "fontname": font})

# Combine and print graphs.
masterGraph = Digraph(name="user-dev-graph", graph_attr=graphProps)
masterGraph.subgraph(userGraph)
masterGraph.subgraph(devGraph)
masterGraph.render("../images/graph", cleanup=True)

# Convert to PNG using ImageMagick.
subprocess.call(["convert", "-density", "400", "../images/graph.pdf",
                 "../images/graph.png"])
subprocess.call(["rm", "../images/graph.pdf"])
