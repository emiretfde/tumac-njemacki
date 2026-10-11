# Production cutover — tumac-njemacki.me (not performed)

## Verified so far
- Production ALL-INKL domain: tumac-njemacki.me -> /tumac-novi/ (confirmed in KAS).
- Original website is still online at /tumac-novi/.
- Backup on SAME server: /tumac-novi-backup-20261011/ — second independent/offsite backup still required.
- Preview: https://preview.tumac-njemacki.me -> /tumac-staging/.
- Staging FTP is limited to /tumac-staging/ and GitHub Actions deployed successfully.
- User confirmed preview site, all three languages, SSL and V18 legal/consent design work.
- GitHub auto-deployment currently affects staging ONLY.
- Live release folder /tumac-bluegold-live/ has been created, separate from current /tumac-novi/.
- Dedicated production FTP user f018eb1d has root /tumac-bluegold-live/ (activation shown as in progress; verify active before testing).
- Domain mail/DNS are kept on ALL-INKL; do not edit MX, nameservers or email during cutover.

## Latest status
- Sead has confirmed the source Impressum and privacy text (reported by user on 2026-10-11).
- All six localized legal pages have had their explicit draft banners removed; this is editorial approval, NOT an independent legal opinion.
- Independent backup archive of the original /tumac-novi/ site was prepared from the original five files and given to user; confirm user has downloaded/stored it before cutover.
- Production guard .tumac-production-guard with TUMAC_PRODUCTION_ONLY_V1 was created at /tumac-bluegold-live/ and GitHub secrets were added.
- Manual FTPS read-only live connection check passed in GitHub Actions.
- The production workflow still has no automatic trigger; production upload and domain switch have NOT happened yet.

## Mandatory before live cutover
1. Sead confirmed the supplied legal texts, as reported by user. Keep a record of his confirmation.
   For legal certainty, a qualified adviser may still review the notices, appointment and retention claims.
2. The explicit draft banners were removed from all 6 localized legal pages after Sead's confirmation.
   deploy/prepare-allinkl-production.sh remains protected: it FAILS if any draft banner returns.
3. Review external Google Fonts and platform processing; consider local fonts if needed.
4. Independently back up old active /tumac-novi/ to a computer (not only the existing
   same-server duplicate) and verify it opens.
5. Validate current Google Ads setup including WhatsApp conversion label and consent
   on the final domain. Recorded clicks are not confirmed WhatsApp messages.
   The tracking code runs only on tumac-njemacki.me and www.tumac-njemacki.me after opt-in.
6. In the existing /tumac-bluegold-live/ folder create a NEW FILE named EXACTLY
   .tumac-production-guard with exact contents TUMAC_PRODUCTION_ONLY_V1.
   This sentinel must be at the FTP account's root; no other directory should contain it.
7. Confirm in KAS > FTP that dedicated production user f018eb1d is active and rooted
   ONLY at /tumac-bluegold-live/. Put credentials in separate GitHub Actions repo secrets:
   ALLINKL_LIVE_FTP_USER = f018eb1d
   ALLINKL_LIVE_FTP_PASSWORD = its separate generated password.
   NEVER paste passwords in chat or source. The production workflow is MANUAL ONLY;
   it requires entering PUBLISH_BLUEGOLD_LIVE and checking the exact guard in FTP root.
   As shipped, build checks explicitly block deployment while legal pages are marked drafts.
8. Build the production release with:
   bash deploy/prepare-allinkl-production.sh
   This copies site assets (incl. self-hosted fonts), the 4 legal pages, /me /de and the sitemap,
   rewrites canonical/hreflang/JSON-LD/OG and sitemap to https://tumac-njemacki.me,
   and creates production .htaccess with / -> /me/ 301.
   Current site SOURCE remains on pages.dev; build must not change preview canonicals.
9. Make a temporary test subdomain pointing to the isolated release folder, with
   valid HTTPS. IMPORTANT: do not let search engines index release preview pages
   before the final switch. Use temporary noindex at preview virtual host level
   (not global .htaccess in the final domain folder), or protect the preview host.
10. Test desktop/mobile, all language links, legal pages, consent choices, phone,
    WhatsApp, Viber and Google Ads tag behavior on the intended live hostname.
11. In KAS > Domains > Edit, change ONLY tumac-njemacki.me Document Root from
    /tumac-novi/ to /tumac-bluegold-live/. Do NOT change DNS, mail or server config.
12. Verify https://tumac-njemacki.me and /me /de, 410 Gone for /en/ URLs, HTTPS and redirection
    immediately. Check all legal links, tag firing only after opt-in, site speed,
    robots.txt and sitemap.xml, old site URLs and any redirects if necessary.
13. If there is an incident, restore Document Root to /tumac-novi/ in KAS.
14. After stable launch configure scheduled/automatic GitHub -> dedicated live folder
    deployment with safety guard, audit trail and rollback versioning.
15. Submit https://tumac-njemacki.me/sitemap.xml to Google Search Console,
    check indexing and Google Ads reporting after publication.

## What NOT to do
- Do not point the active domain to /tumac-staging/.
- Do not copy the staging .htaccess with its noindex header to production.
- Do not set pages.dev canonicals for production.
- Do not publish the unapproved legal pages as definitive legal text.
- Do not use the primary FTP account to automate deployments.
- Do not delete original site, backups, email users or DNS records.
- Do not claim production is ready or live solely because the staging workflow succeeded.

## SEO compatibility
- Existing /index.html, /impressum.html and /datenschutz.html URLs are mapped by Apache 301 redirects to the new /me/ URLs in the production package.
- Cloudflare Pages source remains unchanged so its staging URLs continue to work for development.

## ALL-INKL root redirect fix (2026-10-11)
- The first live switch showed a 404 with `/www/htdocs/w01a14cb/tumac-bluegold-live/me/` in the URL because Apache converted relative RewriteRule destinations into filesystem paths.
- Production packaging now generates absolute HTTPS targets for `/`, `/index.html`, `/impressum.html` and `/datenschutz.html`.
- Redirects are temporarily HTTP 302 to avoid permanent caching during verification; after confirmed public behavior, switch to 301 and redeploy.
- Re-run the existing MANUAL ALL-INKL production GitHub workflow to upload the corrected `.htaccess`. Do not change KAS Document Root or DNS.
- Previously cached 301 redirects may persist in an existing browser profile. Test in a fresh private window and on another device; old cached URLs may require clearing site data.
