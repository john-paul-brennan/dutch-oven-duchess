# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Local Development

Serve the site locally using Python (required for Instagram embeds to load):

```bash
cd "C:\Users\johnp\OneDrive\Documents\Claude\Web Design"
python -m http.server 8080
```

Then open `http://localhost:8080` in the browser.

## Project Structure

Single-file website (`index.html`) with all styles and content inline. No build step, no dependencies to install.

- `index.html` — the entire site: markup, Tailwind utility classes, and a `<style>` block for custom CSS classes
- `DutchOvenDutchess` — workflow instructions for recreating reference website designs from screenshots

## Stack

- **Tailwind CSS** via CDN (`https://cdn.tailwindcss.com`) — configured inline via `tailwind.config` script block
- **Fonts** via Google Fonts: Bitter (serif, body/headings) and Lato (sans-serif, UI labels)
- **Instagram embeds** via `//www.instagram.com/embed.js` (loaded once before `</body>`)

## Design Tokens

| Purpose | Value |
|---|---|
| Primary (backgrounds, buttons) | `rgb(254, 186, 209)` |
| Accent text / links | `rgb(200, 100, 140)` |
| Dark text on pink surfaces | `rgb(100, 40, 70)` |
| Footer background | `rgb(210, 120, 155)` |
| Body text | `rgb(77, 77, 77)` |

Custom CSS classes (defined in the `<style>` block): `.site-bg`, `.site-color`, `.site-border`, `.section-label`, `.nav-link`, `.continue-reading`, `.view-more-btn`, `.post-category`, `.tab-active`, `.footer-heading`, `.footer-link`.

## Instagram Embeds

The scroll row lives between the tabbed recipe section and the cookbook CTA. To add a post:
1. Get the `<blockquote class="instagram-media" ...>` embed code from Instagram (⋯ → Embed on any post)
2. Wrap it in `<div style="flex:0 0 auto;width:320px;">...</div>` inside the horizontal scroll container
3. The single `embed.js` script tag before `</body>` handles all cards — do not add more script tags
