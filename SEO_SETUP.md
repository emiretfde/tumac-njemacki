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
- **Dosadašnja objavljena produkcija** koristila je **302** za root/www. Produkcioni build skript na trenutnom `main` sada priprema **301** za root/www/`index.html` (PR #25); izmjena nije živa dok ručni produkcioni workflow ne bude uspješno pokrenut i provjeren.

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


### Potvrda korisnika o zahtjevima za indeksiranje (11.10.2026)

Korisnik je potvrdio `REQUEST INDEXING` za dvije servisne stranice o vozilima, nakon što su obje prošle Live Test. `/de/` je već ranije bilo prijavljeno. Ne ponavljati zahtjeve danas; čekati Google obradu. Posljednji vidljivi rezultat i dalje je **1/4 indeksirana** stranica (ME početna). GSC sitemap status `Couldn't fetch` još je pod praćenjem.

Dva odvojena predloga bez objave: `PR #21` host-specifični `noindex` za Cloudflare razvojni host (Cloudflare službeno podržava sintaksu apsolutnih URL-ova i host placeholdera); te promjena trajnog kanonskog preusmjeravanja root/www sa 302 na 301, tek nakon provjere. Oboje mora ostaviti zvanične ME/DE stranice indeksabilnim i ne smije mijenjati dizajn.


### Google Business Profile odložen (11.10.2026)

Emir navodi da Sead, prema njegovom saznanju, **nema stalnu kancelariju**. Zato je donesena odluka da se Google Maps / Business Profile **zasad ne otvara**; nastavlja se besplatni organski SEO na domenu i Search Console. Bez provjerenog poslovnog mjesta nikako ne navoditi četiri grada preuzimanja kao četiri kancelarije. Google dopušta service-area business bez izložene adrese **ako postoji stvarni lični kontakt na lokaciji klijenata**; isključivo online poslovanje nema pravo na profil. Ako Sead naknadno potvrdi terensku uslugu sa ličnim kontaktom, ponovno ocijeniti podobnost. Izvori: https://support.google.com/business/answer/3038177 ; https://support.google.com/business/answer/13763036 .


### Posljednje SEO promjene na GitHubu (11.10.2026)

- **PR #25 merged**: `301` canonical host i root/home preusmjeravanja u produkcionom **build skriptu**; za objavu čeka ručno odobreni ALL-INKL production workflow i provjeru. Do tada ne tvrditi da je to trenutno live HTTP ponašanje.
- **PR #27 merged**: `_headers` postavlja `X-Robots-Tag: noindex` samo za Cloudflare Pages development i branch preview hostname; ne kopira se u ALL-INKL production build. HTTP efekat na Pages domeni još nije nezavisno izmjeren. Stari draft PR #21 zatvoren bez mergea.
- **GSC**: zadnji korisnički screenshotovi potvrđuju 1 indeksiran od 4 URL-a; zahtjevi za indeksiranje preostala tri poslati. Sitemap status `Couldn't fetch` još čeka ponovnu Google provjeru. Google Business Profile odložen.
- **Naredni koraci:** korisnička potvrda produkcionog deploya, provjera 301/200/410 odgovora i Cloudflare noindex zaglavlja, pa pregled Search Console narednih dana. Ne ponavljati već poslato indeksiranje.


### Produkciona objava potvrđena, HTTP provjera čeka — 11.10.2026

GitHub Actions [production #8](https://github.com/emiretfde/tumac-njemacki/actions/runs/38148026015) **Success** na `main` commitu `6df1d5137` (paket sa `301` pravilima objavljen). Direktan spoljašnji HTTP test nije uspio zbog DNS/mrežnih ograničenja ChatGPT okruženja, pa status javnih `301` odgovora ostaje **za potvrdu**.

Pripremljen je read-only [Verify live SEO HTTP responses](https://github.com/emiretfde/tumac-njemacki/actions/workflows/verify-live-seo.yml) GitHub Actions workflow: ručno pokrenuti na `main`; provjerava root/www/index redirect, četiri aktivne stranice, EN 410, XML sitemap i robots, te kao zasebno upozorenje Cloudflare Pages noindex. Ne koristi tajne ili upis i ne mijenja produkciju. Nakon testiranja ažurirati handoff konkretnim rezultatima.
