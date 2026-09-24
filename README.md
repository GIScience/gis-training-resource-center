# 📚 IFRC Network GIS Training Platform

Welcome! This repository holds the source of the **IFRC Network GIS Training Platform**. It's a free, open collection of training material for teaching QGIS and GIS for humanitarian work in the Red Cross Red Crescent network.

🌐 **Live site:** https://giscience.github.io/gis-training-resource-center/en/intro.html
(also available in [French](https://giscience.github.io/gis-training-resource-center/fr/) and [Spanish](https://giscience.github.io/gis-training-resource-center/es/))

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

All content is written in Markdown ([MyST](https://mystmd.org/) flavour). [Jupyter Book](https://jupyterbook.org/) turns it into a static website. English is the source language, and each language (English, French, Spanish) is built as a separate book. A GitHub Action combines the three books and publishes them to GitHub Pages whenever changes are merged into `main`.

## Repository layout

```
gis-training-resource-center/
├── content/
│   ├── en/              English source content (the book you edit)
│   ├── fr/              French content, generated from Crowdin (do not edit by hand)
│   └── es/              Spanish content, generated from Crowdin (do not edit by hand)
├── fig/                 Images and figures used across the platform
├── localisation/        XLIFF files exchanged with Crowdin
├── scripts/             Build and localisation helper scripts
├── build_preview_book.bat   One-click local preview on Windows
└── requirements.txt     Python dependencies
```

The folders `english/`, `french/`, `spanish/` and `_site/` are created by local builds. Git ignores them.

## Getting started

You'll need:

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) 3.11 or newer (the site is deployed with 3.13)
- A text editor. [VS Code](https://code.visualstudio.com/) works well for Markdown.

### 1. Clone the repository

```bash
git clone https://github.com/GIScience/gis-training-resource-center.git
```

### 2. Create a virtual environment next to the repository

Create the virtual environment **next to** the repository folder, not inside it. The Windows preview script looks for it at `..\venv`. Your folders should then look like this:

```
your-projects-folder/
├── gis-training-resource-center/
└── venv/
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r gis-training-resource-center\requirements.txt
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r gis-training-resource-center/requirements.txt
```

Run these commands from the folder that contains the repository.

### 3. Switch to the `dev` branch

```bash
cd gis-training-resource-center
git switch dev
git pull
```

## Building a local preview

The preview builds all three books, combines them into one site in `_site/` and serves it at **http://localhost:8080**. This mirrors the published site.

### Windows

Double-click **`build_preview_book.bat`** in the repository folder. You can also run it from a terminal:

```powershell
.\build_preview_book.bat
```

The script:

1. activates the virtual environment in `..\venv`
2. builds the English, Spanish and French books
3. combines them into `_site/en`, `_site/es` and `_site/fr`
4. starts a local server on port 8080 and opens your browser

Press `Ctrl+C` in the terminal window to stop the server.

### macOS / Linux

Activate your virtual environment, then run this from the repository root:

```bash
# Build the three language books
(cd content/en && jupyter-book build . --path-output ../../english)
(cd content/es && jupyter-book build . --config es_config.yml --toc es_toc.yml --path-output ../../spanish)
(cd content/fr && jupyter-book build . --config fr_config.yml --toc fr_toc.yml --path-output ../../french)

# Combine them into one site
rm -rf _site && mkdir -p _site
cp -R english/_build/html _site/en
cp -R spanish/_build/html _site/es
cp -R french/_build/html  _site/fr

# Serve it
cd _site && python3 -m http.server 8080
```

Then open http://localhost:8080/en/intro.html. Press `Ctrl+C` to stop the server.

> **Tip:** If you only changed English content, you can build just the English book (the first build line) and serve `english/_build/html` instead.

> **Why a local server and not just opening the HTML file?** Browsers restrict pages opened straight from disk (`file://`). Links to folders and some scripts behave differently there than on GitHub Pages. The local server is much closer to the live site.

## Branching workflow

| Branch                | Purpose                                                                               |
|-----------------------|---------------------------------------------------------------------------------------|
| `dev`                 | Where all changes go. Push your work here, or open a pull request into it.            |
| `main`                | The published version. Every merge into `main` redeploys the live site automatically. |
| `l10n-crowdin-<lang>` | Created automatically by the translation workflow (see below).                        |

The workflow:

1. Make your changes on `dev`, or on your own feature branch created from `dev`.
2. Build the local preview and check your changes.
3. Commit and push:
   ```bash
   git pull
   git add <files>
   git commit -m "Short description of the change"
   git push
   ```
4. When a set of changes is ready to publish, open a **pull request from `dev` into `main`**. Once it's merged, the site redeploys.

⚠️ **Please don't push directly to `main`.** We plan to add branch protection to `main` so that it can only be changed through reviewed pull requests.

If you're not a member of the GIScience organisation, [fork the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) and open a pull request from your fork into `dev`.

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
3. **Download and merge.** Go to **Actions → Crowdin Download and Merge Translations → Run workflow** and pick the language (`fr` or `es`). The workflow downloads the approved translations, merges them back into Markdown with Okapi Tikal, and writes them to `content/<lang>/`. It then opens a pull request from the branch `l10n-crowdin-<lang>`.
4. **Review.** Every push to an `l10n-crowdin-*` branch triggers the **preview-book** workflow. You can download the built site from that workflow run and check it before merging.

Run these workflows against `dev` (set the branch input when you start them), so translations go through the same review as other changes.

If you'd like to help translate, please contact us (see below) and we'll add you to the Crowdin project.

## Contributing

Contributions of all sizes are welcome: fixing a typo, improving an explanation, adding an exercise, sharing a case study, or translating.

Before you start:

1. **Get in touch** at **gis-training-platform@heigit.org**. Tell us what you'd like to work on so we can coordinate and avoid duplicate work.
2. **Read the [Contribution Plan](https://giscience.github.io/gis-training-resource-center/en/contribution_plan.html)**. It explains the structure, style and review process for new content.

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

