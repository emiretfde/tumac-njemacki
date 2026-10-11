# Production cutover — tumac-njemacki.me (not performed)

## Verified so far
- Production ALL-INKL domain: tumac-njemacki.me -> /tumac-novi/ (confirmed in KAS).
- Original website is still online at /tumac-novi/.
- Backup on SAME server: /tumac-novi-backup-20261011/ — second independent/offsite backup still required.
- Preview: https://preview.tumac-njemacki.me -> /tumac-staging/.
- Staging FTP is limited to /tumac-staging/ and GitHub Actions deployed successfully.
- User confirmed preview site, all three languages, SSL and V18 legal/consent design work.
- GitHub auto-deployment currently affects staging ONLY.
- Domain mail/DNS are kept on ALL-INKL; do not edit MX, nameservers or email during cutover.

## Mandatory before live cutover
1. Verify legal facts with Sead, including address, 2022 appointment and its validity,
   the privacy notice's data processing and actual retention policies, cookie consent.
2. Remove the explicit draft notices from ALL 6 localized legal pages only after review.
   deploy/prepare-allinkl-production.sh intentionally FAILS while legal pages are drafts.
3. Review external Google Fonts and platform processing; consider local fonts if needed.
4. Independently back up old active /tumac-novi/ to a computer (not only the existing
   same-server duplicate) and verify it opens.
5. Validate current Google Ads setup including WhatsApp conversion label and consent
   on the final domain. Recorded clicks are not confirmed WhatsApp messages.
6. Add an isolated production-target folder (proposed: /tumac-bluegold-live/).
   Create an additional FTP account with its root restricted ONLY to that folder.
   Keep production credentials in different GitHub secrets, never chat or source.
7. Prepare a separate, guarded production GitHub Actions workflow. It should upload
   only to the isolated folder, NOT /tumac-novi/, and require manual approval first.
8. Build the production release with:
   bash deploy/prepare-allinkl-production.sh
   This copies site assets, all 6 legal pages, /me /de /en and the sitemap,
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
12. Verify https://tumac-njemacki.me and /me /de /en, HTTPS and redirection
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
