#!/usr/bin/env bash
set -euo pipefail

# Local-only packaging of the real-domain website.
# NEVER uploads, modifies DNS or changes the existing ALL-INKL Document Root.
# Block release while legal pages are explicitly marked as drafts.

destination="dist-allinkl-production"
rm -rf -- "$destination"
mkdir -p -- "$destination"

for source in assets me de en favicon.svg sitemap.xml robots.txt; do
  test -e "$source" || { echo "Missing required source: $source" >&2; exit 1; }
  cp -R -- "$source" "$destination/"
done

for lang in me de en; do
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
done

test -s "$destination/assets/site.css"
test -s "$destination/assets/site.js"

# Replace staging canonicals and reciprocal hreflang / social links,
# including URLs embedded in JSON-LD. Do not alter the source repo.
for lang in me de en; do
  sed -i 's@https://tumac-njemacki.pages.dev@https://tumac-njemacki.me@g' "$destination/$lang/index.html"
done
sed -i 's@https://tumac-njemacki.pages.dev@https://tumac-njemacki.me@g' "$destination/sitemap.xml" "$destination/robots.txt"

if grep -R -q 'tumac-njemacki.pages.dev' "$destination/me" "$destination/de" "$destination/en" "$destination/sitemap.xml" "$destination/robots.txt"; then
  echo "BLOCKED: staging canonical remains in production package." >&2
  exit 1
fi

# Protect directory listing and redirect root to the default language.
cat > "$destination/.htaccess" <<'EOF'
Options -Indexes
DirectoryIndex index.html
RewriteEngine On
# ALL-INKL Apache requires an absolute public URL for these redirects.
# Using a relative target exposed /www/htdocs/... in the browser and caused 404.
# Start with 302 during cutover testing; use 301 only once redirects are verified.
# Preserve old indexed legal URLs when the new site goes live.
RewriteRule ^impressum\.html$ https://tumac-njemacki.me/me/impressum.html [R=302,L,NC]
RewriteRule ^datenschutz\.html$ https://tumac-njemacki.me/me/datenschutz.html [R=302,L,NC]
RewriteRule ^index\.html$ https://tumac-njemacki.me/me/ [R=302,L,NC]
RewriteRule ^$ https://tumac-njemacki.me/me/ [R=302,L]
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
for lang in me de en; do
  grep -Fq "https://tumac-njemacki.me/$lang/" "$destination/$lang/index.html" || { echo "Missing real-domain URLs: $lang" >&2; exit 1; }
done

echo "Production package built locally. No remote changes performed."
