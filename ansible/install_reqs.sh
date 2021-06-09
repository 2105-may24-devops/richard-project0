#!/bin/bash

#Richard Hawkins
#June 9, 2021
#install all python dependencies for P0


python3 -m venv ~/venv
source venv/bin/activate

sudo apt update
sudo apt upgrade

sudo apt install python3-pip
pip3 install -r ~/project0/requirements.txt