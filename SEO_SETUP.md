# SEO — tumac-njemacki.me

## Current deployment
The production-like preview currently uses https://tumac-njemacki.pages.dev/
The real domain **tumac-njemacki.me** must not be used as the canonical host until its DNS and Pages Custom Domain are actually configured.

## Crawlable localized pages
- /me/ — Montenegrin (Latin script), hreflang `sr-Latn-ME` (a supported language/script/region syntax; no two-letter ISO 639-1 code for Montenegrin)
- /de/ — German, hreflang `de`
- /en/ — English, hreflang `en`
- / redirects permanently to /me/
- Every page has its own title, description, self-canonical, reciprocal hreflang, localized real HTML content and JSON-LD.
- Shared CSS and JavaScript are at /assets/site.css and /assets/site.js. JavaScript is NOT required for translation.
- /sitemap.xml contains all three URLs, and /robots.txt links to the sitemap.
- Viber mobile deep links are platform-specific and the copy-number fallback remains.

## IMPORTANT: changes required on real-domain launch
After linking **tumac-njemacki.me** in Cloudflare Pages and verifying HTTPS and existing email:
1. Replace `https://tumac-njemacki.pages.dev` with `https://tumac-njemacki.me` across **me/index.html, de/index.html, en/index.html, sitemap.xml and robots.txt**.
2. Configure `www.tumac-njemacki.me` to redirect to the canonical host (or the inverse, consistently). Do not set mixed canonical URLs.
3. Keep redirects, language navigation, and reciprocal hreflang accurate after the switch.
4. Confirm that Pages preview URLs are not competing for indexation with the custom-domain canonical pages.
5. Verify and submit `https://tumac-njemacki.me/sitemap.xml` in Google Search Console, and optionally Bing Webmaster Tools.
6. Inspect all three URLs with Google URL Inspection. Indexing and rankings are not instant or guaranteed.
7. Run Lighthouse/PageSpeed on mobile and desktop and check Search Console indexing, Core Web Vitals, and search queries.
8. Test phone, WhatsApp, Viber on real devices, and separately test e-mail send/receive after nameserver changes.

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
