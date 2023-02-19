#!/bin/bash
set -e
python -m venv .venv
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     script_location=.venv/bin/activate;;
    Darwin*)    script_location=.venv/bin/activate;;
#    CYGWIN*)    machine=Cygwin;;
    MINGW*)     script_location=.venv/Scripts/activate;;
    *)          echo "Unknown OS Type."
esac

echo ${script_location}
source ${script_location}
pip install -r requirements.txt