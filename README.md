# Sina Hosseini: personal academic website

Source of <https://sinahosseini7.github.io>, a small Jekyll site built by the default GitHub Pages build (no GitHub Actions).

## Where the content lives

All text and settings are in plain files; layouts, styles and scripts never need editing for content changes.

| What | File |
|---|---|
| Name, tagline, e-mail, city, profile links, Scholar on/off | `_data/profile.yml` |
| Menu labels, buttons, section titles and other fixed labels | `_data/ui.yml` |
| The three research themes (Home cards) | `_data/themes.yml` |
| Publications | `_data/publications.yml` |
| CV sections | `_data/education.yml`, `experience.yml`, `skills.yml`, `awards.yml`, `volunteering.yml` |
| Project pages and their cards | `_projects/<slug>.md` |
| Home (About, Beyond Research) | `index.md` |
| Research page | `research.md` |
| Intros of Projects and Publications | `projects.md`, `publications.md` |
| Image sizes | `_data/images.yml` |
| Brand icons (GitHub, LinkedIn, ORCID, Google Scholar) | `assets/img/icons/*.svg` (single-colour SVGs; they take the text colour) |
| Site settings | `_config.yml` |

## Run locally (Windows)

1. Install **Ruby+Devkit 3.3 (x64)** from <https://rubyinstaller.org/downloads/> and, on the last screen, let it run `ridk install` (choose `3`).
2. In this folder, run once:

   ```powershell
   bundle install
   ```

3. Start the preview and open <http://localhost:4000>:

   ```powershell
   bundle exec jekyll serve
   ```

The preview rebuilds when you save a file. After changing `_config.yml`, stop it (`Ctrl+C`) and start it again.

## Editing notes

### Fields kept in two places

Edit both places together:

| Field | Place 1 | Place 2 |
|---|---|---|
| Tagline | `_data/profile.yml` → `tagline` | `_config.yml` → `tagline` |
| Meta description | `_data/profile.yml` → `meta_description` | `_config.yml` → `description` |
| Project summary | `_projects/<slug>.md` → `summary` | same file → `description` |
| Project cover alt text | `_projects/<slug>.md` → `cover_alt` | same file → `image: { alt: … }` |
| Link-preview image alt text | `_data/ui.yml` → `alt: og_image` | `_config.yml` → `defaults` → `image: alt` |

### Add a publication

Copy an existing entry in `_data/publications.yml` into the right list (`journal`, `conference` or `in_preparation`):

```yaml
journal:
  - authors: "A. Author, S. Hosseini, B. Author"   # "S. Hosseini" is made bold automatically
    title: "Paper title"
    venue: "Journal name, 1(2), 3–4"
    year: 2027
    pdf: /assets/files/papers/short-name.pdf     # or ""
    doi: "10.xxxx/xxxx"                          # or ""
    url: ""                                      # publisher page, used when there is no DOI
    project: ""                                  # a project slug, or ""
    thumb: /assets/img/pubs/short-name.webp      # first-page thumbnail, or ""
```

- Journal and conference papers are listed newest first; manuscripts keep the file order.
- A button appears only when it has a target. Use `presentation: oral` for the "Oral presentation" badge, and `status:` (`in preparation`, `submitted`, `under review`) for manuscripts.

### Add a project

1. Copy a file in `_projects/` to `_projects/new-slug.md`; the page address becomes `/projects/new-slug/`.
2. In the front matter, set `group` (`industry`, `academic`, `software`, `personal`), `order` within the group, and `featured: true` for one of the three Home cards.
3. Keep `summary` and `description` identical, and repeat `cover` and `cover_alt` in `image: { path, alt }`.
4. Start the text at `##` headings and add figures with:

   ```liquid
   {% include figure.html src="/assets/img/projects/new-slug/figure.webp" alt="What the image shows" caption="Caption text." %}
   ```

### Add an image

Use WebP (at most 1600 px wide; covers 1200 px, 16:9) and add its size to `_data/images.yml`, using exactly the path used in the page:

```yaml
"/assets/img/projects/new-slug/figure.webp": { w: 1600, h: 900 }
```

### Other changes

- **CV:** replace `assets/files/Sina_Hosseini_CV.pdf` under the same name, and update the CV data files if needed.
- **Google Scholar:** set `show_scholar: true` or `false` in `_data/profile.yml`.
- **Research page:** the two "Methods & Tools" columns depend on the headings `### Computational` and `### Experimental`; the theme anchors (`{#heat-transfer-cfd}` and others) should stay unchanged because links point to them.
- **Photo, name or tagline:** rebuild the Home photo and the link-preview image with:

  ```powershell
  py -m pip install pillow
  py _tools/make_images.py
  ```

## Publishing

Push to the `main` branch; GitHub Pages rebuilds the site (Settings → Pages → Deploy from a branch: `main`, `/ (root)`). The "Last updated" date in the footer updates on every push.

## Credits

This website was built with the assistance of Claude Opus, an AI model by Anthropic.
