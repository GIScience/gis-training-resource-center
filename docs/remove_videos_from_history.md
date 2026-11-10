# Checklist: remove the videos from the git history

The videos are now hosted on Nexus (`https://nexus.heigit.org/repository/gis-training-resource-center/videos/`),
but every old version is still in the git history: about 1.5 GB of the 2.1 GB a fresh clone
downloads. Rewriting the history removes them. Every commit hash and tag changes as a result.

## Before

- [ ] The Nexus switch is merged into `main`: no page links to `fig/*.mp4`, and no `.mp4` is left in `fig/`.
- [ ] All 198 videos are on Nexus (check with `python scripts/sync_videos_nexus.py PATH/TO/VIDEOS`; it should have nothing to upload).
- [ ] Open branches are merged or saved as patches (`ifrc-branding-changes`, `jupyterbook2`, `l10n-crowdin-fr`, open PRs). They can't be merged after the rewrite.
- [ ] Tell the team and contributors the date: after it, they need to clone the repo again.
- [ ] Keep a backup: `git clone --mirror https://github.com/GIScience/gis-training-resource-center.git backup.git`

## Rewrite

```bash
uv tool install git-filter-repo
git clone --mirror https://github.com/GIScience/gis-training-resource-center.git
cd gis-training-resource-center.git
git filter-repo --path-glob '*.mp4' --invert-paths
git count-objects -vH                      # size-pack should be about 0.5 GiB
git remote add origin https://github.com/GIScience/gis-training-resource-center.git
git push --force --all
git push --force --tags
```

- [ ] If branch protection or a ruleset blocks force pushes on `main`, allow them for this push only.

## After

- [ ] Delete your old local clones and clone again. Don't push from an old clone.
- [ ] Delete and recreate the open branches/PRs you saved before.
- [ ] Jenkins: wipe the workspaces of the multibranch job once. The tags have new hashes, so the release tags may build once more.
- [ ] Check a fresh clone: `git clone https://github.com/GIScience/gis-training-resource-center.git` downloads about 0.5 GB.
- [ ] The size GitHub shows may stay large for a while. If it doesn't go down, ask GitHub Support to remove unreachable objects.
- [ ] Contributors with a fork: delete the fork and fork again.

## Old clones and old forks

Old clones can't bring the videos back by accident:

- Pushing an old `main` is rejected (non-fast-forward), and `git pull` refuses to merge the
  unrelated histories. Only `--force` or `--allow-unrelated-histories` would bring the old history back.
- A PR from an old fork can't be merged on GitHub ("entirely different commit histories").

To take over a PR from an old fork without its history, copy only its commits onto the new `main`:

```bash
git fetch https://github.com/USER/gis-training-resource-center.git THEIR-BRANCH
git switch -c take-over-pr origin/main
git cherry-pick <first-commit-of-the-PR>^..<last-commit-of-the-PR>
git push -u origin take-over-pr          # then open a new PR from this branch
```

`cherry-pick` copies only the changes of those commits, not the old history.

## New videos in pull requests

Contributors without Nexus access may add a video to `fig/` in their PR. Before merging:

1. Upload it to Nexus (`python scripts/sync_videos_nexus.py PATH/TO/VIDEOS --apply`).
2. In the PR branch, change the link to the Nexus address and delete the video from `fig/`.
3. **Squash and merge.** `main` then gets one commit without the video. A normal merge would
   keep the video in the history, even though it's deleted afterwards.
