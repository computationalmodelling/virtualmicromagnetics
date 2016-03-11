#!/bin/bash

# This script builds HTML documentation using Sphinx, and optionally spawns a
# process that watches for changes. If it does this, it retains control of the
# shell it is run from.

# Sphinx-build installation check.
if [ "$(which sphinx-build > /dev/null 2>&1; echo $?)" -eq 1 ]; then
    echo "The 'sphinx-build' command was not found."
    exit
fi

# Watch logic.
if [ "$1" == "-w" ]; then

    # Sphinx-autobuild installation check.
    if [ "$(which sphinx-autobuild > /dev/null 2>&1; echo $?)" -eq 1 ]; then
        echo "The 'sphinx-autobuild' command was not found."
        exit
    fi

    sphinx-autobuild -b html -d _build/doctrees . _build/html -i ".*"

# Build logic.
else
    sphinx-build -b html -d _build/doctrees . _build/html
fi

