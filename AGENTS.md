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
