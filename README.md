# net-tools
A set of simple network tools made with python.

The Tools were written (as of now) with Python 3.8 on Linux OS, and I recommend that you use the same. A good way to do so will be by using Conda.

# Environment Setup
Download Miniconda Installer Here : 

https://docs.conda.io/en/latest/miniconda.html

How to Install ?

https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

    conda create -n env_name python=3.8
    pip install scapy

Yayyy!! You are ready to go.

# ECHO

## Requirements

* socket (python module)
* python

## Usage

* This was just a simple fun experiment.
* Run the server in first in one terminal and run the client in a different terminal.
* You can alternatively use this is to keep a port open in your host, and run scripts with incoming data, as of now all it does is echo back whatever you send it.
* You can also connect via netcat.

    nc localhost <port_specified>

# Gatekeeper

# Python Port Scanner using Scapy

* The Port Scanner requires python to be run with admin access, since it has to form 
packets.

* Though it has a GUI interface, the output in displayed in CLI.

* The Scanner has the following dependancies
    * tkinter
    * Scapy
    * multiprocessing
    * os
* You can use the scanner alternatively as a CLI tool also, but with minimal funcationality.

# Chat App

* A simple python chat app that uses, socket and threading modules of python to work.
* The server has to be started first.
* The Chat App runs each client on a seperate thread.
* Use `!disconnect` to disconnect the client.
