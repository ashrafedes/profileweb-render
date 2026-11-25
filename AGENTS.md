# Project notes

## Commands

### "facebook poster"
Posts website articles to the Facebook page "ICT Consulting" (page id `616593318997613`).

- Script: `_fb_post_articles.py`
- Run: `python _fb_post_articles.py` (from repo root; run in background)
- Rate: 5 posts/hour (12 min spacing), max 20 posts/day — exits at daily cap; run again next day
- Resume: `_fb_state.json` tracks `idx`, `posted` URLs, `day`, `day_count` — safe to restart anytime
- Stop: create empty file `_FB_STOP` in repo root, or kill the python process
- Log: `_fb_log.txt`
- Token: Page Access Token lives in `TOKEN` inside the script; if posts start failing with HTTP 190/463 the token expired — get a fresh Page token via `/me/accounts` from a long-lived user token (Graph API Explorer, permissions: pages_manage_posts, pages_read_engagement, pages_show_list)

Each post = article hero image + caption (emoji, title, excerpt, question, URL, hashtags).
Article list source: `sitemap.xml` (`/en/articles/*.html`).

### "new article"
Publishes a complete bilingual article from a JSON spec.

- Script: `_new_article.py` — run `python _new_article.py draft.json` (add `--force` to overwrite an existing slug)
- Spec fields: `slug` (optional, derived from EN title), `category_en`, `category_ar`, `date`, `reading_time` (auto), `featured`, `image`, `tags`, `related` (auto-picks 3 same-category), `en`/`ar` each with `title`, `description`, `body`
- Body accepts HTML or plain text (`## ` = h2, blank lines = paragraphs)
- Generates: EN + AR static pages, root `/articles/` stub, `articles.json` entry, index-grid card (top, both languages), sitemap URLs
- IMPORTANT: index pages are pre-rendered static HTML — articles.json alone never displays an article; a card must exist in `en|ar/articles/index.html`. The script handles this.
- After running: review the pages, then commit + push.
