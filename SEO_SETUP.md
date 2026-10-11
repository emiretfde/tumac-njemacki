# SEO — tumac-njemacki.me

## Current deployment
The production-like preview currently uses https://tumac-njemacki.pages.dev/
The real domain **tumac-njemacki.me** must not be used as the canonical host until its DNS and Pages Custom Domain are actually configured.

## Crawlable localized pages
- /me/ — Montenegrin (Latin script), hreflang `sr-Latn-ME` (a supported language/script/region syntax; no two-letter ISO 639-1 code for Montenegrin)
- /de/ — German, hreflang `de`
- /en/ — REMOVED in V3. No page, hreflang or sitemap entry; /en/ URLs return 410 Gone (see below).
- / redirects permanently to /me/
- Every page has its own title, description, self-canonical, reciprocal hreflang, localized real HTML content and JSON-LD.
- Shared CSS and JavaScript are at /assets/site.css and /assets/site.js. JavaScript is NOT required for translation.
- /sitemap.xml contains the four indexable URLs (ME/DE home, ME/DE vehicle documents), and /robots.txt links to the sitemap.
- `x-default` points to the ME page of each pair.
- Viber mobile deep links are platform-specific and the copy-number fallback remains.

## IMPORTANT: changes required on real-domain launch
After linking **tumac-njemacki.me** in Cloudflare Pages and verifying HTTPS and existing email:
1. Replace `https://tumac-njemacki.pages.dev` with `https://tumac-njemacki.me` across **me/*.html, de/*.html, sitemap.xml and robots.txt** (done automatically by deploy/prepare-allinkl-production.sh).
2. Configure `www.tumac-njemacki.me` to redirect to the canonical host (or the inverse, consistently). Do not set mixed canonical URLs.
3. Keep redirects, language navigation, and reciprocal hreflang accurate after the switch.
4. Confirm that Pages preview URLs are not competing for indexation with the custom-domain canonical pages.
5. Verify and submit `https://tumac-njemacki.me/sitemap.xml` in Google Search Console, and optionally Bing Webmaster Tools.
6. Inspect all three URLs with Google URL Inspection. Indexing and rankings are not instant or guaranteed.
7. Run Lighthouse/PageSpeed on mobile and desktop and check Search Console indexing, Core Web Vitals, and search queries.
8. Test phone, WhatsApp, Viber on real devices, and separately test e-mail send/receive after nameserver changes.

## V3 — English removed completely (no redirects)
Decision by the site owner (2026-10-11): English is removed entirely, not redirected.
- ALL-INKL production and staging: every /en, /en/… URL returns **410 Gone** (`RewriteRule ^en(/.*)?$ - [G]`),
  even when old /en/ files are still in the folder (the FTP mirror never deletes files). Visitors see /404.html
  with links to /me/ and /de/ and the phone number; the page is `noindex`.
- Cloudflare Pages (development): /en/… is simply missing and returns 404 with /404.html.
- No page, hreflang, sitemap entry or link points to /en/.
- Search Console: the earlier indexing request for /en/ will end in "Not found (404/410)" — expected.
  Optionally use Removals → Temporary removal for https://tumac-njemacki.me/en/ to speed it up.
Verified locally on Apache 2.4 (410 for /en, /en/, /en/index.html, legal and vehicle URLs; /ennio stays 404).

## Fonts
V3 self-hosts Cormorant Garamond and Manrope (SIL OFL, licences in assets/fonts/) with latin + latin-ext subsets,
so č ć š ž đ render correctly. The site makes no request to Google Fonts any more; the Google Fonts
sentences were removed from both privacy policies with the owner's approval (2026-10-11).

## Content quality
Avoid fabricated reviews, price claims, instant availability, an office address, or credentials without proof. Current area references describe document collection locations, not necessarily offices.
Use genuine service updates and clear answers to actual client questions rather than artificial keyword-stuffed city pages.

## Google Search Console
- Add the custom domain as a **Domain property** (requires DNS TXT record at the active DNS provider), or use URL-prefix verification.
- Submit sitemap and inspect individual language URLs.
- If Google Business Profile applies, it requires a real, eligible business location or service-area setup; do not invent a street address.
- Build trustworthy citations/backlinks from relevant professional/local directories and official sources when appropriate.

## Notes
- Search visibility and impressions improve over time; code changes alone cannot guarantee top positions.
- Official Google guidance: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites
- Cloudflare Pages redirects: https://developers.cloudflare.com/pages/configuration/redirects/
