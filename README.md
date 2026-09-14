# Melrakki Systems : website essentials

Drop these into your repository. Unless noted, they belong at the repository **root**, next to `index.html`.

## Files and where they go
| File | Location | What it does |
|------|----------|--------------|
| `sitemap.xml` | root | Lists your page for search engines. Referenced by robots.txt. |
| `robots.txt` | root | Allows crawlers and points them at the sitemap. |
| `llms.txt` | root | Describes the site to AI assistants (llmstxt.org format). |
| `favicon.ico` | root | Classic multi size icon browsers request at `/favicon.ico`. |
| `favicon.svg` | root | Crisp vector favicon for modern browsers. |
| `apple-touch-icon.png` | root | Home screen icon on iOS. |
| `icon-192.png`, `icon-512.png` | root | App icons used by the web manifest. |
| `social-preview.png` | root | Image shown when the site is shared (Open Graph / Twitter). |
| `site.webmanifest` | root | Makes the site installable and sets theme colour. |
| `404.html` | root | Branded not found page (GitHub Pages serves it automatically). |
| `CNAME` | root | Tells GitHub Pages to serve the site at www.melrakki.systems. |
| `.nojekyll` | root | Stops GitHub Pages running Jekyll, so all files publish as is. |
| `humans.txt` | root | Optional credit file. |
| `security.txt` | **`/.well-known/`** | Security contact. Create a `.well-known` folder and put it there. |
| `head-snippet.html` | not deployed | Copy its contents into the `<head>` of `index.html`. |

## Important: wire up the head
Your current `index.html` is a JavaScript rendered export, and its `<head>` only contains a title. Search engines and social platforms that do not run JavaScript see only that head, so the description, canonical link, icons, theme colour and share image will not work until you paste the contents of `head-snippet.html` into the `<head>` of `index.html`, just after the existing `<meta charset>` line.

## Custom domain note
With the `CNAME` file in place, set your DNS so `www` points to GitHub Pages, then in the repository under Settings, Pages, confirm the custom domain `www.melrakki.systems` and enable Enforce HTTPS.

## To update later
When the content changes, update `<lastmod>` in `sitemap.xml` to the new date. If you add pages, add a `<url>` block for each.
