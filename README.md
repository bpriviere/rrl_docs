
# README

This is a documentation repository for the Riviere Robot Lab (RRL). More information on doc page. 

## Doc page (hosted here temporarily): 
```
https://bpriviere.github.io/rrl_docs/index.html
```

## Quick start (Linux)

```bash
# from repo root
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make -C docs html
xdg-open docs/build/html/index.html
# or open docs/build/html/index.html in a browser
```