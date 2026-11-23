# Xingjian Wang's personal homepage

A plain, static academic homepage using Marc A. Rieffel's Berkeley homepage
(https://math.berkeley.edu/~rieffel/) as a layout reference. The template keeps
the white background, serif text, blue links, contact block, and simple lists
of academic work. The homepage contains Xingjian's introduction and reading list.

## Personalize

- Edit `index.html` to update your introduction or add articles to the reading list.
- Add sections for research, papers, or notes when you have content to share.
- Use relative links for local documents so the site works on GitHub Pages and
  other static hosts. Add any new asset directories to `tools/build.py` so they
  are also included in the private Sites preview.
- `styles.css` contains the minimal shared styling. No JavaScript or external
  fonts are required by the homepage.

## Preview and build

Run `python3 -m http.server 8000` in this directory, then open
http://localhost:8000. No installation is needed.

Run `python3 tools/build.py` to copy the static website into `dist/` for Sites
hosting. The same source files can be served directly by GitHub Pages from the
root of the `main` branch; `.nojekyll` disables Jekyll processing.

The `.openai/hosting.json` file identifies the separate Sites preview. Publishing
that preview does not update the original GitHub repository or GitHub Pages.
