# Proposed milestone: 2026.12

Status: proposal, 25 September 2026. Based on [known_issues.md](known_issues.md).

This is the first release under the new publication schedule. It has two goals:

1. Set up the release process itself (hosted preview book, protected `main`, announcements).
2. Fix the problems from the link check that can be fixed without new content.

## GitHub milestone

- **Title:** `2026.12`
- **Due date:** 1 December 2026
- **Description** (paste into the milestone):

  > First scheduled release of the GIS Training Resource Center. Sets up the preview book and
  > release process, and fixes broken links, images and downloads found in the September 2026
  > link check. Preview: https://giscience.github.io/gis-training-resource-center/preview/en/

## Timeline

| Date            | Step                                                                                |
|-----------------|-------------------------------------------------------------------------------------|
| Tue 27 Oct 2026 | Scope freeze: only issues in this milestone are merged into `dev` for this release  |
| Tue 3 Nov 2026  | Announcement: "Upcoming changes" post, banner in the live book, preview link shared |
| 3 Nov to 24 Nov | Feedback on the preview; only fixes are merged                                      |
| Tue 1 Dec 2026  | Release: merge `dev` into `main`, tag `v2026.12`, publish the GitHub Release        |

## Scope

Effort: **S** = under an hour, **M** = half a day, **L** = a day or more.
Each line is one proposed issue.

### A. Release process

| Issue                                                           | Effort | Notes                                                                                         |
|-----------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------|
| Deploy a preview book from `dev` at `/preview/`                 | S      | Workflow is ready in `deploy-book.yml`. Needs `dev` allowed in the `github-pages` environment |
| Protect `main` (changes only through reviewed PRs)              | S      | Repository settings                                                                           |
| Enable Discussions with an "Announcements" category             | S      | Repository settings                                                                           |
| Add a "What's new" page with the release schedule and changelog | M      | Linked from the announcement banner. French and Spanish follow through Crowdin                |
| Update the repository homepage URL to `/en/intro.html`          | S      | Still points to the old `/content/intro.html`                                                 |

%% As of 13.10.26: Deployment of preview book had issues and the action does not complete
%% Where to add "What's new" on hp. 
%% Update repo homepage?

### B. English content fixes

| Issue                                                                           | Effort | Notes                                                                                                 |
|---------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------|
| Replace links to old site addresses with relative links                         | S      | `Mobile_Data_collection/en_SMT_ex4_.md`                                                               |
| Restore the 404 downloads on nexus.heigit.org                                   | M      | Needs server access. Module 7 Exercise 1, SMT exercises 1, 2 and 6                                    |
| Add the missing `fig/SRCS_trigger_export_image_pdf.mp4` or remove the reference | S      | Drought trigger Somalia                                                                               |
| Check the third-party links that fail by hand                                   | M      | About 40 links, list in known issues section 3                                                        |
| Fill in the empty card links and `[text]()` links                               | M      | Needs content owners: public health track, Colombia MHU track, MDG drought EAP, SMT exercises 3 and 5 |
| Replace "PLACEHOLDING TEXT" in the Colombia MHU overview                        | S      | Needs content owners                                                                                  |
| Delete or move the 126 pages that aren't in any table of contents               | M      | `*_OLD.md`, `intro_new.md`, French files in the English folder                                        |

%% Replace links should be done
%% fix 404 downloads from nexus
%% add missing image
%% check thirdparty links
%% fill in empty cards or develop new card system and automatically add it to the other exercise pages?
%%    - Here we should also go through all the cards and actually add the correct links
%% Replace placeholding text
%% Check the 126 that arent in the ToC.
%%    - Here it is important to distinguish between actually outdated files and the exercise files
%%    - Also maybe we should add the exercises to the TOC in some sort of system (maybe beneath the Ex tracks)

### C. French and Spanish (through Crowdin)

These are fixed in the English source first. After that, they reach French and Spanish through
Crowdin, not by editing the translated files.

| Issue                                                                                                | Effort | Notes                                                    |
|------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------|
| Run Crowdin Download and Merge for `fr` and `es` after section B is done, then re-run the link check | S      | Should clear most of the 106 broken links                |
| Fix the remaining image and logo paths in French and Spanish                                         | M      | List in known issues section 1                           |
| Translate the licence line in the `fr_config.yml` footer                                             | S      | Config files aren't in Crowdin, so this is a manual edit |

%% This might be skipped as we dont have translated files yet. 
%% Here we should also find out what to do with the existing _es files

### D. Localisation pipeline

| Issue                                                                | Effort | Notes                                                                                                 |
|----------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------|
| Add anchors to translated pages that match the English section links | M      | Link rewrite is done. 108 Spanish and 15 French links open the top of the page instead of the section |
| Remove or fix `crowdin-sync-and-merge.yml`                           | S      | Not used, and misconfigured                                                                           |
| Add a licence file for the workflows in `.github/workflows/`         | S      | MIT is only stated in the README                                                                      |

%% Check again if everything works on crowdin

## Not in this milestone

These depend on translations or larger work and fit a later release:

- French Trainers' corner and French contribution plan (waiting on Crowdin)
- Jupyter-Book 2 upgrade (#256): changes the build and deploy, so it should be its own release
- Moving the Crowdin source branch from `main` to `dev` (once most of the platform is translated)
- Cleaning up the build warnings (duplicate labels, missing bibtex file, unknown directive options)

Open GitHub issues that could also be added if there's time: #72 (Sierra Leone airports data,
priority), #144 (Exercise 2.1 zip), #259 (French text in the English MDG cyclones track).
