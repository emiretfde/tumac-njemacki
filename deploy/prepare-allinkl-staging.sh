#!/usr/bin/env bash
set -euo pipefail

# Package only the site, never repository secrets or development files.
out="dist-allinkl-staging"
rm -rf -- "$out"
mkdir -p -- "$out"

for path in assets me de en favicon.svg; do
  if [[ ! -e "$path" ]]; then
    echo "Missing required site path: $path" >&2
    exit 1
  fi
  cp -R -- "$path" "$out/"
done

for language in me de en; do
  test -s "$out/$language/index.html" || {
    echo "Missing page for $language" >&2
    exit 1
  }
done
for language in me de en; do
  for legal in impressum datenschutz; do
    test -s "$out/$language/$legal.html" || {
      echo "Missing translated legal page: $language/$legal.html" >&2
      exit 1
    }
  done
done
test -s "$out/assets/site.css"
test -s "$out/assets/site.js"

# Staging is never intended for indexing.
cat > "$out/robots.txt" <<'EOF'
User-agent: *
Disallow: /
EOF

# Apache settings for an isolated test subdomain only.
cat > "$out/.htaccess" <<'EOF'
Options -Indexes
DirectoryIndex index.html
RewriteEngine On
RewriteRule ^$ me/ [R=302,L]
<IfModule mod_headers.c>
  Header always set X-Robots-Tag "noindex, nofollow, noarchive"
</IfModule>
EOF

# Fallback if URL rewrites are disabled.
cat > "$out/index.html" <<'EOF'
<!doctype html>
<html lang="sr-Latn-ME">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex,nofollow">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Sead Crnovršanin — testna verzija</title>
  <meta http-equiv="refresh" content="0;url=/me/">
</head>
<body><p><a href="/me/">Otvori testnu verziju sajta</a></p></body>
</html>
EOF

echo "Staging package ready. Existing production files have not been changed."
