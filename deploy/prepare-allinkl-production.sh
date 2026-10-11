#!/usr/bin/env bash
set -euo pipefail

# Local-only packaging of the real-domain website.
# NEVER uploads, modifies DNS or changes the existing ALL-INKL Document Root.
# Block release while legal pages are explicitly marked as drafts.

destination="dist-allinkl-production"
rm -rf -- "$destination"
mkdir -p -- "$destination"

for source in assets me de favicon.svg 404.html sitemap.xml robots.txt google9ea0a3ecbd8b4bde.html; do
  test -e "$source" || { echo "Missing required source: $source" >&2; exit 1; }
  cp -R -- "$source" "$destination/"
done

for lang in me de; do
  for doc in impressum datenschutz; do
    file="$destination/$lang/$doc.html"
    test -s "$file" || { echo "Missing legal page: $file" >&2; exit 1; }
    if grep -q 'class="legal-draft"' "$file"; then
      echo "BLOCKED: $file is still explicitly labeled a legal draft." >&2
      echo "Obtain approval, verify the content, and remove draft warning in a reviewed change." >&2
      exit 1
    fi
  done
  test -s "$destination/$lang/index.html" || { echo "Missing language page: $lang" >&2; exit 1; }
  test -s "$destination/$lang/prevod-saobracajne-dozvole.html" || { echo "Missing vehicle service page: $lang" >&2; exit 1; }
done

test -s "$destination/assets/site.css"
test -s "$destination/assets/site.js"

# V3: self-hosted fonts must ship with the package (no Google Fonts requests).
for font in cormorant-garamond-latin-600-normal cormorant-garamond-latin-ext-600-normal manrope-latin-400-normal manrope-latin-ext-400-normal; do
  test -s "$destination/assets/fonts/$font.woff2" || { echo "Missing font: $font" >&2; exit 1; }
done

# V3: English was retired. It must not come back as a page, hreflang or sitemap entry.
if [[ -e "$destination/en" ]]; then echo "BLOCKED: /en/ must not be published (redirected instead)." >&2; exit 1; fi
if grep -R -q -E 'hreflang="en"|tumac-njemacki\.pages\.dev/en/' "$destination/me" "$destination/de" "$destination/sitemap.xml"; then
  echo "BLOCKED: English hreflang or URL still referenced." >&2; exit 1
fi

# Ownership verification must be publicly available at the domain root.
# Validate exact payload before publishing: no HTML wrapper or accidental edits.
verify_file="$destination/google9ea0a3ecbd8b4bde.html"
test "$(cat "$verify_file")" = "google-site-verification: google9ea0a3ecbd8b4bde.html" || {
  echo "Invalid Google Search Console ownership verification file." >&2
  exit 1
}

# Replace staging canonicals and reciprocal hreflang / social links,
# including URLs embedded in JSON-LD. Do not alter the source repo.
for lang in me de; do
  for html in "$destination/$lang/"*.html; do
    sed -i 's@https://tumac-njemacki.pages.dev@https://tumac-njemacki.me@g' "$html"
  done
done
sed -i 's@https://tumac-njemacki.pages.dev@https://tumac-njemacki.me@g' "$destination/sitemap.xml" "$destination/robots.txt"

if grep -R -q 'tumac-njemacki.pages.dev' "$destination/me" "$destination/de" "$destination/sitemap.xml" "$destination/robots.txt"; then
  echo "BLOCKED: staging canonical remains in production package." >&2
  exit 1
fi

# Protect directory listing and redirect root to the default language.
cat > "$destination/.htaccess" <<'EOF'
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html
ErrorDocument 410 /404.html

# Force correct XML MIME to prevent browsers from interpreting sitemap tags as HTML.
AddType application/xml .xml
AddType font/woff2 .woff2
<Files "sitemap.xml">
  ForceType application/xml
</Files>

RewriteEngine On
# Canonical host (permanent: stable public domain).
RewriteCond %{HTTP_HOST} ^www\.tumac-njemacki\.me$ [NC]
RewriteRule ^ https://tumac-njemacki.me%{REQUEST_URI} [R=301,L,NE]

# Use full public URLs: ALL-INKL exposes a filesystem path for relative redirects.
RewriteRule ^impressum\.html$ https://tumac-njemacki.me/me/impressum.html [R=302,L,NC]
RewriteRule ^datenschutz\.html$ https://tumac-njemacki.me/me/datenschutz.html [R=302,L,NC]
RewriteRule ^index\.html$ https://tumac-njemacki.me/me/ [R=301,L,NC]

# V3: English version removed completely. 410 Gone (no redirect), even if old
# /en/ files remain in the folder because the FTP mirror never deletes files.
RewriteRule ^en(/.*)?$ - [G,L,NC]
RewriteRule ^$ https://tumac-njemacki.me/me/ [R=301,L]

<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
</IfModule>
EOF

# Non-SEO fallback if .htaccess rewrite is unavailable.
cat > "$destination/index.html" <<'EOF'
<!doctype html>
<html lang="sr-Latn-ME"><head>
<meta charset="utf-8">
<meta name="robots" content="noindex,follow">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="0;url=/me/">
<link rel="canonical" href="https://tumac-njemacki.me/me/">
<title>Sead Crnovršanin — Sudski tumač</title>
</head><body><p><a href="/me/">Otvori sajt</a></p></body></html>
EOF

# A production package must have an indexable sitemap pointing to the right host.
grep -Fq 'https://tumac-njemacki.me/sitemap.xml' "$destination/robots.txt" || { echo "Bad robots sitemap URL" >&2; exit 1; }
for lang in me de; do
  grep -Fq "https://tumac-njemacki.me/$lang/" "$destination/$lang/index.html" || { echo "Missing real-domain URLs: $lang" >&2; exit 1; }
  grep -Fq "https://tumac-njemacki.me/$lang/prevod-saobracajne-dozvole.html" "$destination/$lang/prevod-saobracajne-dozvole.html" || { echo "Vehicle page still points at staging: $lang" >&2; exit 1; }
done

echo "Production package built locally. No remote changes performed."
