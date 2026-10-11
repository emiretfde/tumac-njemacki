# SEO — tumac-njemacki.me (ažurirano 11.10.2026)

> **VAŽNO:** Primarni izvor istine za nastavak projekta je [docs/HANDOFF.md](docs/HANDOFF.md). Ranije uputstvo da se povezuje domen sa Cloudflare Pages, verifikuje Search Console iz početka ili pregledaju tri aktivna jezika više ne važi.

## Sadašnje produkciono okruženje
- Sajt je **LIVE na ALL-INKL**: https://tumac-njemacki.me ; direktorijum `/tumac-bluegold-live/`.
- `main` odgovara V3.0.2, commit `d66efe495f99e5eae72715a321809950ccea2f92`. Produkcioni workflow [uspješan](https://github.com/emiretfde/tumac-njemacki/actions/runs/38132612919) 11.10.2026.
- Staging: https://preview.tumac-njemacki.me (ALL-INKL, noindex, robots blokada).
- `tumac-njemacki.pages.dev` je razvojna adresa, **nije** zvanični host ili kanonski domen produkcije.
- Izvorni `me/*.html`, `de/*.html`, `robots.txt` i `sitemap.xml` koriste `pages.dev` u GitHubu; `deploy/prepare-allinkl-production.sh` to automatski zamjenjuje domenom `https://tumac-njemacki.me` pri produkcionom pakovanju. Zato se SEO izvorni kod ne kopira direktno na live server.

## Indeksabilne stranice: četiri URL-a

| Jezik | Početna | Vozila |
| --- | --- | --- |
| ME (latinično) | `/me/` | `/me/prevod-saobracajne-dozvole.html` |
| DE | `/de/` | `/de/prevod-saobracajne-dozvole.html` |

- Posebni `<title>` i meta-description, canonical, recipročni hreflang za **ME `sr-Latn-ME`** i **DE `de`**, a `x-default` vodi na ME.
- Sitemap na `https://tumac-njemacki.me/sitemap.xml` ima samo četiri URL-a; `robots.txt` upućuje na taj sitemap.
- Pravne stranice (Impressum/Datenschutz) su postojeće, ali imaju `noindex,follow`; ne zahtijevati njihovo indeksiranje bez nove odluke.
- **Engleski je svjesno ugašen.** Nema `en/`, hreflang-a ni URL-ova u sitemap-u. Na produkciji `/en/*` vraća HTTP **410 Gone** (Apache `.htaccess`; razvojni Cloudflare Pages 404). Stari indeksacijski zahtjev za `/en/` je zastario i Google će ga vremenom ukloniti.
- Redirecti sa `/` na `/me/` i sa `www` na apex su **302** prema produkcionoj build skripti; eventualna promjena na 301 je odvojena izmjena, ne trenutna činjenica.

## Google Search Console — već verifikovan

1. Već postoji **URL-prefix property** `https://tumac-njemacki.me/`. Korisnik je 11.10.2026. dobio **Ownership verified** nakon HTML verifikacije; fajl `google9ea0a3ecbd8b4bde.html` je u repozitorijumu i produkcionom paketu. **Ne verifikovati ponovo** bez konkretnog razloga, ne mijenjati DNS.
2. `sitemap.xml` je ranije prijavljen u Search Console. Prilikom inicijalnog lansiranja prikazivao se status **Couldn't fetch / Sitemap could not be read**. **Trenutni status u Search Console nakon V3 nije potvrđen** u ovoj dokumentaciji.
3. Nezavisna GitHub Actions provjera [Diagnose public sitemap, run #38132882924](https://github.com/emiretfde/tumac-njemacki/actions/runs/38132882924) je uspješno dohvatila produkcioni sitemap (200, `application/xml`, validan XML, četiri ispravne adrese). Ovo potvrđuje tehničku dostupnost u toj provjeri, ne Google indeksiranje.
4. Prije redizajna korisnik je poslao **REQUEST INDEXING** za `/me/`, `/de/` i tadašnju `/en/`. Kako je EN uklonjen, dalje treba raditi samo sa ME/DE i dvije stranice za vozila.
5. Za nastavak rada: u već povezanom Search Console otvoriti **Sitemaps → Pages → URL Inspection** i pregledati najnovije stanje; po potrebi zatražiti indeksiranje dvije nove stranice o vozilima. Status Google indeksiranja i organskog saobraćaja nijesu potvrđeni GitHub Actions testom.

**Napomena:** DNS Domain property je samo moguća buduća opcija, ali **nije potrebna** da već verifikovana URL-prefix property radi.

## Lokalni SEO i sadržaj
- Primarni ciljevi: „sudski tumač za njemački“, „ovjereni prevod“, „prevod saobraćajne dozvole“, korisni upiti u Podgorici/Crnoj Gori.
- Ne izrađivati masovne „SEO stranice za svaki grad“, lažne kancelarije, cijene ili izmišljene recenzije.
- Sead je odabrao naslov usluga „Prevod dokumenata sa njemačkog i na njemački“; ne vraćati „Šta prevodim“.
- U listi gradova navedene su lokacije mogućeg preuzimanja po dogovoru, ne tvrdnja o fizičkim poslovnicama.
- Google Business Profile razmotriti samo uz potvrdu stvarne poslovne podobnosti i podataka od Seada.
- Organic SEO je cilj; **ne otvarati nove Google Ads kampanje ni unositi kartice**. Postojeći consent-gated tag za WhatsApp klikove je odvojena tema i ne potvrđuje stvarne konverzije.

## Tehnička provjera prije naredne objave
1. Izmjene teksta/markup-a raditi u `tools/build_pages.py`; generisati HTML sa `python3 tools/build_pages.py`.
2. Prekontrolisati `git diff` svih generisanih stranica, posebno odobreni pravni tekst i consent.
3. Pregledati UX na stvarnim telefonima (iPhone/Safari i Android/Chrome), klikove Pozovite, Viber, WhatsApp, e-mail, kontakt traku i mobilni meni.
4. Provjeriti dvije aktivne jezičke verzije, `sitemap.xml`, `/en/` 410, kanonske adrese poslije produkcionog builda.
5. Promjene na grani → PR → merge na `main` (automatski **staging**) → pregled/odobrenje → ručni produkcioni workflow **samo uz izričitu potvrdu korisnika**.
6. Ne mijenjati DNS, KAS Document Root, FTP sigurnosne provjere, verifikacioni fajl ili pravne tekstove bez odobrenja.

Službene SEO smjernice: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites


### Potvrđeni GSC status — 11.10.2026, oko 15:47 (screenshotovi)

- `/me/`: **“URL is on Google” / “Page is indexed”**. Ta stranica je indeksirana, a ne samo podobna za indeksiranje.
- Zbirni **Indexing → Pages**: **“Processing data, please check again in a day or so”** — nema ukupnih brojki.
- **Sitemaps → /sitemap.xml**: **“Couldn't fetch”**, **“Sitemap could not be read”**, posljednje čitanje 11.10.2026, **0 discovered pages**. Stanje i dalje postoji na dan objave.
- Nezavisni read-only GitHub Actions run [#38132882924](https://github.com/emiretfde/tumac-njemacki/actions/runs/38132882924) ranije je potvrdio HTTP 200, validan XML i 4 produkciona URL-a; time **nije** potvrđeno da je Google obradio sitemap.
- **Ne raditi odmah promjene servera ili brisati/re-submittovati sitemap.** Dati Googleu 24–72 sata za novu provjeru; ako ostane greška, dijagnostikovati HTTP pristup, robots i hosting logove. Prvo pregledati pojedinačne GSC statuse za `/de/` i obje stranice za vozila. 


### Potpuna pojedinačna URL Inspection provjera — 11.10.2026, oko 16:10

Prema GSC screenshotovima: **`/me/` je indeksirana**; `/de/` i obje stranice `/me/prevod-saobracajne-dozvole.html`, `/de/prevod-saobracajne-dozvole.html` još imaju `URL is not on Google` / `URL is unknown to Google`, bez prethodnog crawla. **Sve tri neindeksirane stranice imaju uspješan Live Test i dozvoljeno indeksiranje**; obje servisne strane imaju po jedan validan Breadcrumbs rezultat. Prijavljeni `sitemap.xml` je ranije istoga dana ostao na `Couldn't fetch` i 0 discovered, iako nezavisni test XML-a radi.

**Sljedeće:** Ne ponavljati Request Indexing za ranije poslatu `/de/`. Za obje servisne strane zatražiti indeksiranje po jednom (ako nije već urađeno; korisnička potvrda još nije dostavljena). Poslije čekati da Google ponovo obradi sitemap i ažurira Pages izvještaj. Nema dokazanog problema koji bi zahtijevao izmjene koda.
