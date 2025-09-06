# Installation (Linux) 

If you want to contribute documentation, you need to do these steps: 

## Prerequisites
- Linux distro with Python 3.10+
- `python3-venv` package

## Build the docs
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make -C docs html
xdg-open docs/build/html/index.html  # or open in your browser
```
