# Xingjian Wang's personal homepage

A plain, static academic homepage using Marc A. Rieffel's Berkeley homepage
(https://math.berkeley.edu/~rieffel/) as a layout reference. The template keeps
the white background, serif text, blue links, contact block, and simple lists
of academic work. All bracketed text is a placeholder, not a biographical claim.

## Personalize

- Edit `index.html` to add your affiliation, contact information, introduction,
  research interests, papers, and notes. Delete sections you do not need.
- Replace the bracketed text in `teaching/index.html`, `papers/index.html`, and
  `notes/index.html`, or link the homepage titles directly to your PDFs instead.
- Put your documents in `papers/` or `notes/` and use relative links so the site
  works on GitHub Pages and other static hosts.
- `styles.css` contains the minimal shared styling. No JavaScript or external
  fonts are required by the homepage.

## Original project

The existing Forex Graph is preserved at `experiments/forex/`. Its exchange
rates are a historical repository snapshot, not live financial data. The
original Python tools and root data file are retained as well.

## Preview and build

Run `python3 -m http.server 8000` in this directory, then open
http://localhost:8000. No installation is needed.

Run `python3 tools/build.py` to copy the static website into `dist/` for Sites
hosting. The same source files can be served directly by GitHub Pages from the
root of the `main` branch; `.nojekyll` disables Jekyll processing.

The `.openai/hosting.json` file identifies the separate Sites preview. Publishing
that preview does not update the original GitHub repository or GitHub Pages.
