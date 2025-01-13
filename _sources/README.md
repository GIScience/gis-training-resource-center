# Repo for the 📚 GIS Training Resource Center [TRC]

:warning:
:construction: Under Construction :construction: 


https://giscience.github.io/gis-training-resource-center/content/intro.html

We use markdown documents with rich media hosted elsewhere that serve as comprehensive guides, tutorials and reference materials. 
The markdown files are built to a static webpage via `jupyter-book`.

## :tractor: Dev setup

* clone the repo: `git clone https://github.com/GIScience/gis-training-resource-center`
* set up a python environment, e.g. `python3 -m venv venv`
* activate the environment: `source venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`
* `cd gis-training-resource-center` !Do not create the venv inside the repository, otherwise build command will try to compile source files from /venv
* do your changes to the book in `contents`
* build it locally `jupyter-book build .`
* verify changes `cd _build/html/ && python3 -m http.server 8080`
* push source files via git to the `dev` branch
  * change the branch `git switch dev`
  * `git pull`
  * `git commit -m "yourmessage"`
  * `git push`
  * conflict: `git config pull.rebase false`
  * when you are finished with your changes, create a pull request to merge `dev` with `main`. 
* push rendered html files to branch `gh-pages` via the command `ghp-import -n -p -f _build/html`. This will automatically delete the branch and recreate it to avoid a bloated history.

## 🌐 Contributions

We warmly welcome everyone to contribute and collaborate in advancing the IFRC GIS Training Platform, fostering shared knowledge and growth.
Before contributing:

* Contact us on `gis-training-platform@heigit.org`
* Make sure to read through the [Contribution Plan](https://giscience.github.io/gis-training-resource-center/content/contribution_plan.md)

## CI / CD
* to be considered in the future

