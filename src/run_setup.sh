#!/bin/bash
#checking python version
if ! [[ -x "$(command -v python3)" ]]
then
  pyv="$(python -V 2>&1)"
  if [[ $pyv == "Python 3"* ]]
  then
    python src/main.py
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
#creating the virtual environment
python3 -m venv .venv
source .venv/bin/activate
#installing the required packages
pip install -r requirements.txt
echo "Installed correctly. Please run run_app.sh. A way to do this is by typing bash src/run_app.sh"
