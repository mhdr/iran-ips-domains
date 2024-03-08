#!/bin/bash

python -m venv venv

venv/bin/python -m pip install --upgrade tld
venv/bin/python -m pip install --upgrade requests