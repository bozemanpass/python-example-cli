# "source" this script to setup a dev venv
python3 -m venv dev
source ./dev/bin/activate
python3 -m pip install --upgrade pip
# Install shiv and flake8 here because they're "dev dependencies" only
pip install shiv
pip install flake8
pip install --editable .
