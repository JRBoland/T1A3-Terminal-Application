#!/bin/bash


if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
else
    echo 'Python is installed on this device. Beginning Dog Shelter Feeding Helper'
fi
echo "Installing requirements.txt"
pip install -r requirements.txt

echo "Running Dog Shelter Feeding Helper..."
python3 main.py
