#!/bin/sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install pandas matplotlib
venv/bin/python3 -m pip install --upgrade pip
venv/bin/python3 main.py