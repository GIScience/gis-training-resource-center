# Repo for the 📚 GIS Training Resource Center [TRC]

:warning:
:construction: Under Construction :construction: 

We use markdown documents with rich media hosted elsewhere that serve as comprehensive guides, tutorials and reference materials. 
The markdown files are built to a static webpage via `jupyter-book`.

## :tractor: Dev setup

* set up python environment, e.g. `python3 -m venv venv`
* activate environment: `source venv/bin/activate`
* install dependencies: `pip install -U jupyter-book nbconvert`
* change the content of the markdown files or jupyter notebooks
* build the website and slides: `make html`

## CI / CD
* every commit to the `main` branch is deployed through a github actions pipeline
* we might change this later to a dev / main system with releases

