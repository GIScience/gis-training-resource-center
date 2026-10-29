# 📚 IFRC Network GIS Training Platform

Welcome! This repository holds the source of the **IFRC Network GIS Training Platform**. It's a free, open collection of training material for teaching QGIS and GIS for humanitarian work in the Red Cross Red Crescent network.

🌐 **Live site:** https://gis-training.heigit.org/en/intro.html
(also available in [French](https://gis-training.heigit.org/fr/) and [Spanish](https://gis-training.heigit.org/es/))

The old address (`giscience.github.io/gis-training-resource-center`) redirects to the new site.

The platform is developed in a collaboration between [HeiGIT](https://heigit.org/), the [German Red Cross](https://www.drk.de/), the [British Red Cross](https://www.redcross.org.uk/) and the [Netherlands Red Cross](https://www.rodekruis.nl/). It includes:

- **Modules** that explain GIS concepts, from beginner to intermediate level
- **Exercises** that give trainees hands-on practice in QGIS
- **A Wiki** with practical how-to guides and videos
- **Trainers' corner** with training plans and guidance on teaching GIS
- **GIS in Anticipatory Action** case studies, and reusable **Tools & Methods**

We welcome contributions from Red Cross and Red Crescent staff and volunteers, National Societies, other organisations, and anyone else who wants to improve GIS training for humanitarian work.

---

## Contents

- [How the platform is built](#how-the-platform-is-built)
- [Repository layout](#repository-layout)
- [Getting started](#getting-started)
- [Building a local preview](#building-a-local-preview)
- [Branching workflow](#branching-workflow)
- [Localisation (translations)](#localisation-translations)
- [Contributing](#contributing)
- [License and contact](#license-and-contact)

---

## How the platform is built

All content is written in Markdown ([MyST](https://mystmd.org/) flavour). [Jupyter Book](https://jupyterbook.org/) turns it into a static website. English is the source language, and each language (English, French, Spanish) is built as a separate book.

The site is built and hosted by HeiGIT:

- The `Dockerfile` builds the three books and packs them into an nginx image, with English at `/en/`, French at `/fr/` and Spanish at `/es/`.
- The Jenkins pipeline (`Jenkinsfile`) builds this image on every push to `main` and deploys it to an internal test site for the HeiGIT team. To see your own changes, [build a local preview](#building-a-local-preview).
- Only **releases** go live on [gis-training.heigit.org](https://gis-training.heigit.org). A release is a git tag that matches the version in `pyproject.toml` (for example `0.2.0`).
- The GitHub workflow **Deploy GitHub Pages redirects** replaces the old GitHub Pages site with redirects to the new domain. Rerun it by hand after adding pages if old links to them should redirect too.

Changes for readers are listed on the [What's new](content/en/whats_new.md) page.

## Repository layout

```
gis-training-resource-center/
├── content/
│   ├── en/              English source content (the book you edit)
│   ├── fr/              French content, generated from Crowdin (do not edit by hand)
│   └── es/              Spanish content, generated from Crowdin (do not edit by hand)
├── docs/                Known issues and release milestones
├── fig/                 Images and figures used across the platform
├── scripts/             Link checker, redirect builder and localisation scripts
├── Dockerfile           Builds the site image (all three books + nginx)
├── Jenkinsfile          CI pipeline: builds main for internal testing, release tags go live
├── index.html           Root page, redirects to /en/
├── pyproject.toml       Python dependencies (managed by uv) and the release version
└── uv.lock              Locked dependency versions
```

The `localisation/` folder (XLIFF files exchanged with Crowdin) is written by the Crowdin workflows.

The folders `english/`, `french/`, `spanish/` and `_site/` are created by local builds. Git ignores them.

## Getting started

You'll need:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/) — it installs and manages the Python interpreter (3.14) and the project's dependencies. No separate Python install is needed.
- A text editor. [VS Code](https://code.visualstudio.com/) works well for Markdown.

### 1. Clone the repository

If you want to contribute, [fork the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) first and clone your fork. To only build the site locally, clone it directly:

```bash
git clone https://github.com/GIScience/gis-training-resource-center.git
```

### 2. Set up the Python environment with [uv](https://docs.astral.sh/uv/)

The project uses [uv](https://docs.astral.sh/uv/) to manage the Python environment. uv creates a virtual environment inside the repository (`.venv/`) and installs the exact locked dependencies.

If you don't have uv yet, install it: [uv install documentation](https://docs.astral.sh/uv/getting-started/installation/)

Then, from inside the repository folder, sync the environment:

```bash
cd gis-training-resource-center
uv sync --no-install-project
```

uv reads the Python version from `.python-version` (3.14) and installs it automatically if it isn't present. The `.venv/` folder is created in the repository root and is ignored by Git.

## Building a local preview

The preview builds all three books, combines them into one site in `_site/` and serves it at **http://localhost:8080**. This mirrors the published site.

### With Docker

If you have [Docker](https://docs.docker.com/get-docker/), this builds exactly the image that is deployed:

```bash
docker build -t gis-training .
docker run --rm -p 8080:80 gis-training
```

Then open http://localhost:8080/en/intro.html. Press `Ctrl+C` to stop the container.

### With uv

Make sure the environment is synced (`uv sync --no-install-project`), then run this from the repository root (on Windows, use Git Bash):

```bash
# Build the three language books
(cd content/en && uv run jupyter-book build . --path-output ../../english)
(cd content/es && uv run jupyter-book build . --config es_config.yml --toc es_toc.yml --path-output ../../spanish)
(cd content/fr && uv run jupyter-book build . --config fr_config.yml --toc fr_toc.yml --path-output ../../french)

# Combine them into one site
rm -rf _site && mkdir -p _site
cp -R english/_build/html _site/en
cp -R spanish/_build/html _site/es
cp -R french/_build/html  _site/fr

# Serve it
cd _site && uv run python -m http.server 8080
```

Then open http://localhost:8080/en/intro.html. Press `Ctrl+C` to stop the server.

> **Tip:** If you only changed English content, you can build just the English book (the first build line) and serve `english/_build/html` instead.

> **Why a local server and not just opening the HTML file?** Browsers restrict pages opened straight from disk (`file://`). Links to folders and some scripts behave differently there than on a web server. The local server is much closer to the live site.

### Checking links

After building, check the built site for broken links, images and anchors:

```bash
uv run python scripts/check_site_links.py              # all languages
uv run python scripts/check_site_links.py --lang en    # English only
uv run python scripts/check_site_links.py --external   # also check external URLs (slow)
```

The script lists every problem by page. It checks the built HTML rather than the build log,
because MyST doesn't recognise the stable `<a id="...">` heading anchors, so its link warnings
are switched off in the book configs. Known open issues are tracked in
[docs/known_issues.md](docs/known_issues.md).

Card links (`:link:` on `{card}` / `{grid-item-card}`) to other pages need `:link-type: doc` and
a path without `.md`, and text links need the `.md` extension, for example
`[Clip](../Wiki/en_qgis_geoprocessing_wiki.md#clip)`.

### Updating the vendored MathJax file

Mathematical formulas in the book are rendered with [MathJax](https://www.mathjax.org/). Instead of loading it from a CDN, the site bundles a self-contained copy of MathJax 3 in the repository at `_static/mathjax/tex-mml-chtml.js`, and the book configs point `mathjax_path` at it. To update the copy to a newer MathJax 3 release, download the file over the top of the existing one:

```bash
curl -fSL -o _static/mathjax/tex-mml-chtml.js "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
```

`@3` always resolves to the latest 3.x release. To pin a specific version instead, replace `@3` with a tag, for example `mathjax@3.2.2`. `tex-mml-chtml.js` is a single self-contained bundle (TeX + MathML + HTML output), so the one file is all that's needed — no separate helper scripts. After updating, rebuild the local preview to confirm the math still renders on a page with formulas (for example Module 5).

## Branching workflow

| Branch / tag          | Purpose                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------|
| `main`                | The current version of the platform. All changes are merged here through pull requests.     |
| Release tag (`0.2.0`) | A published version. Tagging a release deploys it to gis-training.heigit.org.               |
| `l10n-crowdin-<lang>` | Created automatically by the translation workflow (see below).                              |

### Contributing changes

Contributions come in as **pull requests into `main`**, from a fork or from a branch.

1. **Fork the repository** on GitHub ([how to fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)) and clone your fork. Members of the GIScience organisation can create a branch in this repository instead.
2. Create a branch for your change from an up-to-date `main`:
   ```bash
   git switch main
   git pull
   git switch -c my-change
   ```
3. Make your changes and [build a local preview](#building-a-local-preview) to check them. There is no public test site, so the local preview is the place to see your changes before they're merged.
4. Commit and push your branch:
   ```bash
   git add <files>
   git commit -m "Short description of the change"
   git push -u origin my-change
   ```
5. Open a **pull request into `main`** and describe what you changed. The HeiGIT team reviews it and merges it.

If your pull request is open for a while, update it with the latest `main` before it's merged (`git pull origin main` on your branch, or `git pull upstream main` from a fork).

### Publishing a release (maintainers)

1. Bump `version` in `pyproject.toml` and add the changes to the [What's new](content/en/whats_new.md) page.
2. Tag the commit on `main` with the same version, for example `git tag 0.3.0 && git push --tags`. Jenkins builds the release and deploys it to the live site.

## Localisation (translations)

The platform is available in English, French and Spanish. **English is the only language edited directly in this repository.** French and Spanish are translated on [Crowdin](https://crowdin.com/) and brought back in automatically.

Please **don't edit files in `content/fr/` or `content/es/` by hand**. The next translation import would overwrite your changes. Fix the English source instead, or correct the translation on Crowdin.

### How the pipeline works

```
 content/en/*.md
       │   1. "Crowdin Upload Source XLIFF" workflow
       ▼
 localisation/xliff/sources/*.xlf ──► Crowdin
                                         │  2. translators work on Crowdin
                                         ▼
                               approved translations
       ┌─────────────────────────────────┘
       │   3. "Crowdin Download and Merge Translations" workflow
       ▼
 content/fr/  or  content/es/   ──►  pull request from l10n-crowdin-<lang>
```

1. **Upload sources.** In GitHub, go to **Actions → Crowdin Upload Source XLIFF → Run workflow**. The workflow converts the English Markdown into XLIFF files with [Okapi Tikal](https://okapiframework.org/), commits them to `localisation/xliff/sources/`, and uploads them to Crowdin.
2. **Translate.** Translators translate and approve the text on Crowdin.
3. **Download and merge.** Go to **Actions → Crowdin Download and Merge Translations → Run workflow** and pick the language (`fr` or `es`). The workflow downloads the approved translations, merges them back into Markdown with Okapi Tikal, and writes them to `content/<lang>/`. Links to English pages are pointed at the translated pages, and every page that isn't translated yet gets a placeholder ("not translated yet", with a link to the English page) that the translation replaces later. The French or Spanish menu is updated to follow the English one, listing only translated pages. It then opens a pull request from the branch `l10n-crowdin-<lang>` against `main`.
4. **Review.** Check out the `l10n-crowdin-<lang>` branch and build the French or Spanish book locally before merging. Translations go live with the next release.

Both workflows use `main` by default, so you don't need to change the branch inputs.

If you'd like to help translate, please contact us (see below) and we'll add you to the Crowdin project.

## Contributing

Contributions of all sizes are welcome: fixing a typo, improving an explanation, adding an exercise, sharing a case study, or translating.

Before you start:

1. **Get in touch** at **gis-training-platform@heigit.org**. Tell us what you'd like to work on so we can coordinate and avoid duplicate work.
2. **Read the [Contribution Plan](https://gis-training.heigit.org/en/contribution_plan.html)**. It explains the structure, style and review process for new content.

A few conventions:

- Write new content in **English** in `content/en/`. Translations follow through Crowdin.
- English files use the `en_` prefix, for example `en_qgis_buffer.md`.
- Put images in `fig/` and link to them with a relative path.
- New pages must be added to `content/en/_toc.yml` to appear on the site.
- Always build the local preview before opening a pull request.

Found a problem but don't have time to fix it? [Open an issue](https://github.com/GIScience/gis-training-resource-center/issues). That helps too.

## License and contact

© HeiGIT gGmbH. This repository uses two licenses:

- **Training content:** everything in `content/` and `fig/` is released under [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). See [LICENSE](LICENSE).
- **Code:** the scripts in `scripts/` and the GitHub workflows in `.github/workflows/` are released under the [MIT License](scripts/LICENSE).

Questions, feedback or ideas? Email **gis-training-platform@heigit.org**. We look forward to hearing from you.

