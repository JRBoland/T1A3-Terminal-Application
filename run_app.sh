#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  pyv="$(python -V 2>&1)"
  if [[ $pyv == "Python 3"* ]]
  then
    python main.py
  else
    echo 'Error: 
    This program runs on Python3, but it looks like Python3 is not installed.
    To install Python, check out https://installpython3.com/' >&2
  fi
  exit 1
else
    echo 'Preparing...'
fi
echo "Installing requirements..."
python3 -m venv .venv
source venv/bin/activate
pip install -r ./requirements.txt
echo "Running Dog Shelter Feeding Helper..."
python3 main.py
