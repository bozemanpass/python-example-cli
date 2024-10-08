# "source" this script to setup a dev venv
python3 -m venv dev
source ./dev/bin/activate
python3 -m pip install --upgrade pip
pip install --editable .
