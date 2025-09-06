
# Contribute

If you want to contribute documentation, you need to (i) install the docs package and (ii) learn how to contribute by writing, building, and submiting docs changes.


## Installation (Linux) 


### Prerequisites
- Linux distro with Python 3.8+
- `python3-venv` package


### Build the docs
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make -C docs html
xdg-open docs/build/html/index.html  # or open in your browser
```


## Contribute


### Add a page (most common will be to add a README)
- Decide which header you want to your page under: `my-header`
- Create new **Markdown** (MyST) file `docs/source/my-header/my-page.md`
- Add `my-page` to the toctree in `docs/source/my-header/index.md`
- Rebuild: `make -C docs html`


### Add a header
- Create new folder `docs/source/my-header`
- Add `my-header` to the toctree in `docs/source/index.md`
- Rebuild: `make -C docs html`


### Submit a doc change
- Run `make -C docs html` and verify docs work locally (open `docs/build/html/index.html` in a browser)
- We use a docs build check so you won't be able to push or PR if the changes do not at least work locally. 
- Submit a pull request (PR). See [README](readmes/github.md) for more information about that. 
