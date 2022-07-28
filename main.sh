#!/bin/sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -q pandas matplotlib numpy
venv/bin/python3 -m pip install -q --upgrade pip
venv/bin/python3 main.py