# Sina Hosseini: personal academic website

This folder is the complete source of `https://sinahosseini7.github.io`.
It is a small Jekyll site built for the default GitHub Pages build (Jekyll 3.10.0, no GitHub Actions).

You change the site by editing text files only:

| What you want to change | File to edit |
|---|---|
| Name, tagline, email, city, profile links, Scholar on/off | `_data/profile.yml` (and see "Fields kept in two places") |
| Menu labels, button texts, section titles, small labels | `_data/ui.yml` |
| The three research themes (Home cards) | `_data/themes.yml` |
| Publications | `_data/publications.yml` |
| CV page sections | `_data/education.yml`, `experience.yml`, `skills.yml`, `awards.yml`, `volunteering.yml` |
| A project page and its card | `_projects/<slug>.md` |
| About text and Beyond Research (Home) | `index.md` |
| Research page | `research.md` |
| Intro lines of Projects and Publications | `projects.md`, `publications.md` |
| Image sizes (width and height) | `_data/images.yml` |

You never need to edit `_layouts/`, `_includes/`, `assets/css/` or `assets/js/` for content changes.

---

## 1. Run the site on your computer (Windows 11)

Tested here with Ruby 3.3.6, Bundler, the `github-pages` gem version 232, Jekyll 3.10.0, Liquid 4.0.4 and kramdown 2.4.0.

### One-time setup

1. Download **Ruby+Devkit 3.3.x (x64)** from <https://rubyinstaller.org/downloads/> and run the installer.
   Keep "Add Ruby executables to your PATH" ticked.
2. On the last screen, keep "Run 'ridk install'" ticked and click Finish.
   A black window opens: type `3` (MSYS2 and MINGW development toolchain) and press Enter.
   When it finishes, press Enter again to close it.
   (If you missed this step, open a new terminal and run `ridk install`.)
3. Open **a new** PowerShell window in this folder (in File Explorer: right-click inside the folder → "Open in Terminal").
4. Run:

   ```powershell
   gem install bundler
   bundle install
   ```

### Every time you want to preview the site

```powershell
bundle exec jekyll serve
```

Open <http://localhost:4000> in your browser. The site rebuilds when you save a file.
Press `Ctrl+C` in the terminal to stop it.
After you change `_config.yml`, stop and start `jekyll serve` again: Jekyll reads that file only at start.

### Common Windows errors and fixes

| You see | Fix |
|---|---|
| `'bundle' is not recognized` | Close the terminal and open a new one (PATH is read at start). If it still fails, run `gem install bundler`. |
| `Failed to build gem native extension` while installing `wdm` | Run `ridk install`, choose `3`, then `bundle install` again. If it still fails, delete the `gem "wdm" ...` line from `Gemfile` and run `bundle install` (only the file watching becomes a little slower). |
| `cannot load such file -- webrick` | Run `bundle install` again: `webrick` is already in the `Gemfile`. |
| `invalid byte sequence in UTF-8` or garbled characters such as °, µ, − | Run `chcp 65001` in the same window, then `bundle exec jekyll serve` again. |
| `Address already in use - bind(2) for 127.0.0.1:4000` | Another `jekyll serve` is still running. Close it, or run `bundle exec jekyll serve --port 4001` and open <http://localhost:4001>. |
| `GitHub Metadata: No GitHub API authentication could be found` | Harmless. It can appear once; the site still builds. |
| `Bundler could not find compatible versions` | Run `bundle update`, then `bundle install`. |
| A change does not appear | Refresh with `Ctrl+F5`. If you changed `_config.yml`, restart `jekyll serve`. |

---

## 2. Before you publish

### Your images and PDFs

Copy your `assets/img/` and `assets/files/` contents into the same folders here.
Do **not** overwrite these three files, which belong to this repository: `assets/img/og-image.png`, `assets/img/favicon.svg`, `assets/img/profile-320.webp`.
Names are case-sensitive and must match `_data/images.yml` exactly.

### The four brand icons

The GitHub, LinkedIn, ORCID and Google Scholar logos are brand logos, so they are not drawn in this repository.
Download each as an SVG file and save it with exactly this name:

| Icon | File |
|---|---|
| GitHub | `assets/img/icons/github.svg` |
| LinkedIn | `assets/img/icons/linkedin.svg` |
| ORCID | `assets/img/icons/orcid.svg` |
| Google Scholar | `assets/img/icons/google-scholar.svg` |

A good source is Simple Icons (<https://simpleicons.org>, CC0): search the name, then use "Download SVG".
The site draws each file as a shape in the current text colour, so the logos follow the light and dark themes automatically. Any single-colour SVG works.
Until a file is in place, its icon is blank but the link still works, and the site still builds.

### The CV PDF (open item OI-11)

Add your updated CV as exactly `assets/files/Sina_Hosseini_CV.pdf` before or with the first push.
Both "Download CV" (Home) and "Download PDF" (CV page) point to this file and save it as `Sina_Hosseini_CV.pdf`.

---

## 3. Everyday edits

### Fields kept in two places (edit both together)

| Field | Place 1 | Place 2 |
|---|---|---|
| Tagline | `_data/profile.yml` → `tagline` | `_config.yml` → `tagline` |
| Meta description | `_data/profile.yml` → `meta_description` | `_config.yml` → `description` |
| Project summary | `_projects/<slug>.md` → `summary` | the same file → `description` |
| Project cover alt text | `_projects/<slug>.md` → `cover_alt` | the same file → `image: { alt: ... }` |
| Social preview image alt | `_data/ui.yml` → `alt: og_image` | `_config.yml` → `defaults` → `image: alt` |

`_config.yml` also holds `job_title: "Chemical Engineer"`. It is used only in the hidden structured data that search engines read.

### Add a publication

Open `_data/publications.yml` and copy an existing entry into the right list (`journal`, `conference` or `in_preparation`).

```yaml
journal:
  - authors: "A. Author, S. Hosseini, B. Author"   # "S. Hosseini" is made bold automatically
    title: "Paper title"
    venue: "Journal name, 1(2), 3–4"
    year: 2027
    pdf: /assets/files/papers/short-name.pdf     # or "" if you do not host a PDF
    doi: "10.xxxx/xxxx"                          # or ""
    url: ""                                      # page on the publisher's site, used when there is no DOI
    project: ""                                  # a project slug, or ""
    thumb: /assets/img/pubs/short-name.webp      # first-page thumbnail, or ""
```

- Journal and conference lists are shown newest first (by `year`). Manuscripts keep the order of the file.
- Buttons appear only when they have a target: PDF (`pdf`), DOI (`doi`), Link (`url`, used only when there is no DOI), Project (`project`).
- For a conference talk, add `presentation: oral` to show the "Oral presentation" badge.
- For a manuscript, use `status:` with one of `in preparation`, `submitted`, `under review`.
- Add the thumbnail size to `_data/images.yml` (see "Add an image").

### Add a project

1. Copy one file in `_projects/`, for example `picophone.md`, to `_projects/new-slug.md`.
   The file name becomes the page address: `/projects/new-slug/`.
2. Edit the front matter:
   - `group`: one of `industry`, `academic`, `software`, `personal` (the four groups of the Projects page).
   - `order`: the position inside its group (1, 2, 3 …). Previous/next links follow this order.
   - `featured: true` puts the card on Home. Keep exactly three featured projects.
   - `summary` and `description`: the same sentence (`description` is what link previews show).
   - `cover` and `cover_alt`, and the same two values in `image: { path: ..., alt: ... }`.
   - `theme`: one anchor from `_data/themes.yml` (`heat-transfer-cfd`, `insulation-porous`, `thermal-management-storage`) or `""`.
   - `outputs`: a list of `{ label: "...", url: "..." }`. An empty `url` shows the label as plain text.
3. Put the images in `assets/img/projects/new-slug/` and add each one to `_data/images.yml`.
4. In the text, add a figure with:

   ```liquid
   {% include figure.html src="/assets/img/projects/new-slug/figure.webp" alt="What the image shows" caption="Caption text." %}
   ```

   Start the page text at `## ` headings (the title is the page's only top-level heading).

### Add an image

1. Use WebP, at most 1600 px wide (covers: 1200 px, 16:9).
2. Save it under `assets/img/...` with a lower-case name.
3. Add one line to `_data/images.yml` with its real size in pixels:

   ```yaml
   "/assets/img/projects/new-slug/figure.webp": { w: 1600, h: 900 }
   ```

   The key must be exactly the path you use in the page. Without the line the image still shows, but the page may jump while it loads.

### Replace the CV

Save the new PDF as exactly `assets/files/Sina_Hosseini_CV.pdf` (same name, same folder), replacing the old one.
Then update the CV data files (`_data/education.yml`, `experience.yml`, …) if anything changed.

### Turn Google Scholar on or off

In `_data/profile.yml`, set `show_scholar: true` (icon shown) or `show_scholar: false` (icon hidden).
The link itself is `links: scholar:`.

### Research page: the two "Methods & Tools" columns

The two columns are keyed to the heading texts `### Computational` and `### Experimental` in `research.md`
(Jekyll turns them into the ids `computational` and `experimental`).
If you rename either heading, the lists still show, but in one column.
The theme anchors (`{#heat-transfer-cfd}` and so on) must stay as they are: links in your emails point to them.

### After changing the photo, name or tagline: rebuild the two generated images

`assets/img/profile-320.webp` (Home photo) and `assets/img/og-image.png` (link preview) are made from
`assets/img/profile.webp` and the `name` and `tagline` in `_data/profile.yml`.
Run in this folder:

```powershell
py -m pip install pillow
py _tools/make_images.py
```

The first run downloads the two fonts into `_tools/fonts/` (ignored by Git). Then commit the two new images.

---

## 4. Publish (merge-and-publish guide)

1. Unzip this repository.
2. Copy your `assets/img/` and `assets/files/` contents into the same paths. Do not overwrite `og-image.png`, `favicon.svg` or `profile-320.webp`.
3. Add the four brand icon SVGs to `assets/img/icons/` (section 2).
4. Run the site locally (section 1) and check every page.
5. On GitHub, create the public repository `sinahosseini7.github.io`.
6. Add `assets/files/Sina_Hosseini_CV.pdf` before or with the first push (OI-11).
7. Push to the `main` branch.
8. On GitHub: Settings → Pages → Source: "Deploy from a branch", Branch: `main`, folder `/ (root)`. Save.
9. After a minute or two, check the live site on a phone and on a computer, including a link preview of one project page (paste its address into a chat app).

The footer date ("Last updated") changes automatically on every push.

---

## 5. Notes

- `_tools/` holds the image generator. Jekyll ignores it; it is never published.
- The empty `.gitkeep` files keep the empty asset folders in Git. You can leave them.
- `sitemap.xml` and `robots.txt` are made automatically. The CV PDF is deliberately not listed in the sitemap.
- Fonts: Plus Jakarta Sans (headings) and Inter (text), loaded from Google Fonts.
- Light and dark themes follow the visitor's system setting until they use the toggle; the choice is then remembered.
