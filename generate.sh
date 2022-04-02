#! /bin/sh
deactivate
rm -rf ~/CM
python3 -m venv ~/CM
source ~/CM/bin/activate
pip install pip -U
pip install -r requirements.txt


sphinx-build -b html documentation/source/ documentation/build/html

cd documentation/source
