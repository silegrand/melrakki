# Melrakki Systems website

Single-page site for Melrakki Systems, ready for GitHub Pages.

## Structure
- `index.html` : the site (self-contained page, logos and product drawings embedded)
- `assets/`    : brand pack (favicon, apple-touch icon, social preview, lockups, marks, banners) and the three product concept drawings

## Deploy on GitHub Pages
1. Put `index.html` and the `assets/` folder in the root of your repository.
2. In the repository, open Settings, then Pages.
3. Under Build and deployment, set Source to "Deploy from a branch", branch `main`, folder `/ (root)`.
4. Save. Your site publishes at the Pages URL, or at your custom domain www.melrakki.systems once the domain is configured.

## Notes
- The favicon, Apple touch icon and social preview image are referenced from `assets/`, so keep that folder alongside `index.html`.
- Contact links use hello@melrakki.systems. Change this in `index.html` before launch if needed.
- The Harka Solar battery figure (24 VDC, 400 Ah) is provisional pending confirmation of the correct datasheet.
