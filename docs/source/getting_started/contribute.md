# Contributing 

How to write, build, and submit docs changes.

## How to add a page
- Decide which header you want to your page under: `my-header`
- Create new **Markdown** (MyST) file `docs/source/my-header/my-page.md`
- Add `my-page` to the toctree in `docs/source/my-header/index.md`
- Rebuild: `make -C docs html`

## How to add a header
- Create new folder `docs/source/my-header`
- Add `my-header` to the toctree in `docs/source/index.md`
- Rebuild: `make -C docs html`

## Pull Request (PR) checklist
- Run `make -C docs html` and verify docs work locally (open `docs/build/html/index.html`). We use a docs build check so you won't be able to push or PR if the changes do not at least work locally. 
