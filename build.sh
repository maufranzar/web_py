source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --fronted-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate