#!/bin/bash

pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel

pip install --target . -r requirements.txt
