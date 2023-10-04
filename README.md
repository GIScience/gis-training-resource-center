# Repo for the 📚 GIS Training Resource Center [TRC]

:warning:
:construction: Under Construction :construction: 


https://giscience.github.io/gis-training-resource-center/content/intro.html

We use markdown documents with rich media hosted elsewhere that serve as comprehensive guides, tutorials and reference materials. 
The markdown files are built to a static webpage via `jupyter-book`.

## :tractor: Dev setup

* clone the repo: `git clone https://github.com/GIScience/gis-training-resource-center`
* `cd gis-training-resource-center`
* set up a python environment, e.g. `python3 -m venv venv`
* activate the environment: `source venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`
* do your changes to the book in `contents`
* build it locally `jupyter-book build .`
* verify changes `cd _build/html/ && python3 -m http.server 8080`
* push source files via git to `main`
  * `git pull`
  * `git commit -m "yourmessage"`
  * `git push`
  * conflict: `git config pull.rebase false`
* push rendered html files to branch `gh-pages` via the command `ghp-import -n -p -f _build/html`. This will automatically delete the branch and recreate it to avoid a bloated history.




## CI / CD
* to be considered in the future

