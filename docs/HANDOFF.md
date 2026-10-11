# HANDOFF — tumac-njemacki.me / V3.0 (stanje 11.10.2026)

## Ko, šta, gdje
- **Klijent:** Sead Crnovršanin, sudski tumač za njemački jezik (Crna Gora). Sajt: **https://tumac-njemacki.me**
- **Ja (Emir)** vodim tehnički dio sajta. Sead daje sadržaj i odobrava tekstove.
- **Repo:** `emiretfde/tumac-njemacki` (GitHub), grana `main`.
- **Hosting:** ALL-INKL (statički HTML/CSS/JS, bez CMS-a i baze).
- **Test okruženje:** https://preview.tumac-njemacki.me (staging, noindex, robots `Disallow: /`).
- **Cloudflare Pages** (`tumac-njemacki.pages.dev`) služi samo za razvoj. Izvorni HTML ima pages.dev canonicale, a produkcioni build ih zamjenjuje sa `tumac-njemacki.me`.

## Trenutno stanje
- **V3.0 je LIVE** na tumac-njemacki.me od 11.10.2026. Produkcioni workflow run `38132612919` je uspio, a `main` je na commitu `d66efe4`.
- Uspješno je urađen i read-only `Diagnose public sitemap` na živom domenu: 4 URL-a, ispravan XML i Content-Type.
- Emir je na telefonu potvrdio da **Viber i WhatsApp rade**.
- PR-ovi: **#17** (V3.0 redizajn), **#18** (bez dupliranog naslova + dostava kurirom), **#19** (naslov usluga + bez linka na spisak tumača). Svi su spojeni.

## Šta je V3.0
Mobile-first redizajn, rađen jer je preko 99% Google Ads saobraćaja sa telefona. Ciljna grupa su stariji i informatički manje iskusni korisnici.
- **Stari problemi (riješeni):** zaglavlje se preklapalo na iPhone-u (`.nav-cta` je prikazan na mobilnom zbog redosljeda CSS-a), hamburger je bio van ekrana (stranica široka 406 px), H1 je imao 65 px, a stranica je bila visoka ~8.300 px. Font Italiana nije imao č/ć/š/ž/đ.
- **Struktura početne:** gornja traka (telefon + ME|DE) → ime + Meni → linija povjerenja → H1 „Sudski tumač za njemački jezik" → kratki opis → gradovi + „Ostali gradovi: dostava kurirom" → dugmad **Pozovite / Viber / WhatsApp** + e-mail → „Prevod dokumenata sa njemačkog i na njemački" (6 stavki) → 3 koraka → O meni → Preuzimanje i dostava → Česta pitanja → Kontakt.
- **Traka na dnu (telefon):** Pozovite · Viber · WhatsApp. Pojavljuje se tek kad prva dugmad nestanu, a skrivena je u kontakt sekciji, dok je consent baner otvoren i na desktopu.
- **Fontovi su lokalni:** Cormorant Garamond (naslovi) + Manrope (tekst), OFL licence u `assets/fonts/`. Nema Google Fonts.
- **Stranice:** `/me/` i `/de/` — početna, `prevod-saobracajne-dozvole.html`, `impressum.html`, `datenschutz.html`. Tu je i `/404.html` (dvojezična, noindex).

## Odluke koje su donijete (ne mijenjati bez pitanja)
1. **Samo ME i DE.** Engleski je **potpuno uklonjen, bez redirekcija.** Na ALL-INKL-u `/en` i `/en/...` vraćaju **410 Gone** (`RewriteRule ^en(/.*)?$ - [G]`), čak i ako stari /en/ fajlovi ostanu na serveru. Na Cloudflare Pages je 404.
2. **Google Fonts rečenice su uklonjene** iz politike privatnosti (ME i DE) uz Emirovu saglasnost. Ostali pravni tekst je nepromijenjen.
3. **Povjerenje:** navodi se rješenje ministra pravde **UPI-05-109/22-1418-1 od 26.12.2022** (kao u Impressumu), a ne spisak iz 2018.
4. **Nikakav link na spisak svih sudskih tumača (gov.me).** Sead ne želi „reklamu drugima". Stara root `index.html` sa tim linkom zamijenjena je noindex redirekcijom na /me/.
5. Naslov usluga je „Prevod dokumenata sa njemačkog i na njemački" (Sead: „Šta prevodim" mu se nije dopalo). DE: „Übersetzung von Dokumenten aus dem und ins Deutsche".
6. Na početnoj u zaglavlju stoji samo ime, bez ponavljanja „Sudski tumač…" (H1 to već kaže). Podstranice zadržavaju liniju sa zanimanjem.
7. **Ne dodavati Facebook** dok Sead ne dostavi zvanični link. Ne izmišljati cijene, rokove ni kancelarije po gradovima.

## Pravila koja moraju ostati
- **Viber logika u `assets/site.js` je ista kao u V10** (Emir ju je lično testirao): iOS `viber://contact?number=%2B38267998199`, Android `viber://chat?number=38267998199`, ostalo `viber://chat?number=%2B38267998199` + dugme „Kopiraj broj". Sada se primjenjuje na **sva** Viber dugmad.
- **Consent / Google Ads** (`AW-837134242`, WhatsApp konverzija) radi samo na produkcionom domenu i samo uz opt-in. Logiku i tekst banera ne mijenjati bez pregleda.
- **Pravni tekst** (Impressum, Datenschutz) mijenja se samo uz izričito odobrenje. Generator ga prenosi bajt po bajt.
- Google verifikacioni fajl `google9ea0a3ecbd8b4bde.html` ne dirati.
- Bez plaćenih servisa, frameworka i novih kampanja.

## Kako se mijenja sadržaj
- **Sav tekst za početnu i stranicu o vozilima je u `tools/build_pages.py`** (rječnik `C` za `me` i `de`). HTML se NE uređuje ručno. Promijeni tekst tamo, pa pokreni:
  `python3 tools/build_pages.py`
- Pravne stranice: generator čita `<main>` iz postojećeg fajla i samo ga prepakuje. Pravni tekst se, uz odobrenje, mijenja direktno u `me|de/impressum.html` / `datenschutz.html`, pa se pokrene generator.
- Stil: `assets/site.css` (napisan iznova, mobile-first, bez `!important` slojeva). JS: `assets/site.js`.
- Kada se mijenjaju CSS i JS, povećaj `ASSET_V` u `build_pages.py` (sada `3.0.0`) zbog keša.

## Objava (deploy)
- **Staging:** svaki push/merge na `main` automatski ide na preview.tumac-njemacki.me (workflow „ALL-INKL staging"). Bezbjedno je, noindex.
- **Produkcija:** samo ručno, workflow „ALL-INKL production (manual, guarded)" uz unos `PUBLISH_BLUEGOLD_LIVE`. Uploaduje u `/tumac-bluegold-live/` (domen već pokazuje tamo). Može i preko API-ja:
  `gh api -X POST repos/emiretfde/tumac-njemacki/actions/workflows/380988153/dispatches -f ref=main -f "inputs[release_approval]=PUBLISH_BLUEGOLD_LIVE"`
- **Produkciju pokretati samo uz izričitu Emirovu potvrdu.** Ne mijenjati DNS, e-mail, Document Root, FTP naloge ni zaštite u workflowima.
- Prije objave lokalno pokreni `bash deploy/prepare-allinkl-production.sh`. Skripta blokira build ako se EN vrati, ako fale fontovi ili ako ostane pages.dev canonical.
- Na ALL-INKL-u redirekcije moraju koristiti **apsolutne javne URL-ove**, inače server otkriva `/www/htdocs/...` putanju.
- Radni tok koji se pokazao dobro: grana → PR → merge (staging) → Emir pregleda na telefonu → ručna produkcija.

## Testirano
- Širine 320, 360, 375, 390, 414, 430, 768, 1280 i 1440 px na svim stranicama (Chromium): bez horizontalnog skrola i preklapanja, dodirna polja ≥44 px, tekst ≥14 px (osnovni 17 px).
- Tastatura, rad bez JavaScripta, HTML validacija, canonical/hreflang (ME `sr-Latn-ME`, DE `de`, `x-default` = ME).
- Produkcioni i staging `.htaccess` testirani na Apache 2.4: 410 za /en, `/` → 302 na /me/, nema curenja putanje, sitemap `application/xml`, fontovi `font/woff2`.
- Safari/WebKit nije testiran u razvojnom okruženju. Emir je na iPhone-u potvrdio da sajt, Viber i WhatsApp rade.

## Otvoreno / sljedeći koraci
1. **Google Search Console:** Sead ne zna šta je to. Vjerovatno je vezan za Emirov Google nalog (emirsijaric@gmail.com). Emir treba da provjeri na search.google.com/search-console i pošalje `sitemap.xml`. Ako svojstva nema, prijaviti ga ponovo (preporuka: DNS TXT zapis u ALL-INKL KAS, Domain property). Kasnije dodati Seada kao vlasnika.
2. Redirekcije `/` → `/me/` i `www` → apex su još **302** (privremeno, iz V26). Kad se sve pokaže stabilnim, mogu se prebaciti na 301 u `deploy/prepare-allinkl-production.sh`.
3. Na serveru u `/tumac-bluegold-live/` ostaju stari `/en/` fajlovi (FTP mirror ne briše). Bezopasno je zbog pravila 410, a mogu se ručno obrisati preko KAS WebFTP-a.
4. Screenshotovi u `docs/v3/` su iz prve verzije V3 (prije PR #18 i #19), samo za istoriju.
5. **Google Ads mjerenje:** trenutno se kao konverzija broji samo klik na WhatsApp (`drLwCI3GgpYdEKLPlo8D`). Klikovi na **Pozovite** (`data-contact="phone"`) i **Viber** se ne broje. Za to Emir prvo pravi nove konverzije u Google Ads nalogu, pa se njihove oznake dodaju u `assets/site.js` (ista consent pravila kao za WhatsApp). Final URL u oglasima treba da bude `https://tumac-njemacki.me/me/` (bez 302 preko `/`).
6. Povezan projekat: **Tumač AI** (alat za pripremu prevoda dokumenata za vozila) planira subdomen `app.tumac-njemacki.me` na zasebnom VPS-u. Glavni sajt to ne dira.

## Mapa fajlova
- `me/`, `de/` — stranice (generisane)
- `404.html`, `index.html` (root: noindex redirekcija na /me/)
- `assets/site.css`, `assets/site.js`, `assets/fonts/`
- `tools/build_pages.py` — generator stranica i sav tekst
- `sitemap.xml` (4 URL-a), `robots.txt`, `_redirects` (Cloudflare)
- `deploy/prepare-allinkl-production.sh`, `deploy/prepare-allinkl-staging.sh`, `deploy/PRODUCTION_CUTOVER.md`, `deploy/ALLINKL_DEPLOY.md`
- `SEO_SETUP.md` — SEO pravila i odluka o uklanjanju EN
- `.github/workflows/` — staging (auto na main), production (ručno, zaštićeno), live connection check i diagnose-sitemap (read-only)

## Komunikacija
Emir piše na crnogorskom (ijekavica), kratko i direktno. Odgovaraj na istom jeziku, bez tehničkog žargona kad nije potreban. Seadove komentare prenosi Emir, često kao screenshotove poruka.
