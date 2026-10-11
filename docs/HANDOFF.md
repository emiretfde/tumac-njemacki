# HANDOFF — Sead Crnovršanin / tumac-njemacki.me
**Stanje: 11. oktobar 2026. | V3.0.2 mobile-first | izvor istine za narednu Claude sesiju**

> **Pročitaj prvo.** Ovo je nastavak postojećeg projekta, NE novi projekat i NE poziv za novi redizajn. Prije rada uporedi `main` sa ovim dokumentom i posljednjim GitHub Actions rezultatima. Ne pretpostavljaj da je Google Search Console nepovezan, da je engleski aktivan ili da je produkcija još na Cloudflare Pages.

## 1. Kratki pregled / status

| Stavka | Provjereno stanje 11.10.2026. |
| --- | --- |
| Klijent | Sead Crnovršanin, sudski tumač za njemački jezik u Crnoj Gori |
| Osoba koja vodi sajt | Emir; odobrava tehničke promjene, posreduje Seadove tekstualne zahtjeve |
| GitHub | https://github.com/emiretfde/tumac-njemacki ; glavna grana `main` |
| Posljednji aplikativni commit na `main` | `d66efe495f99e5eae72715a321809950ccea2f92` — V3.0.2 / PR #19 |
| Zvanični sajt | https://tumac-njemacki.me → ALL-INKL, document root `/tumac-bluegold-live/` |
| Staging | https://preview.tumac-njemacki.me — ALL-INKL izolovani test, `noindex` |
| Cloudflare Pages | https://tumac-njemacki.pages.dev — razvojna adresa; nije produkcioni hosting |
| Jezici | Samo **ME `/me/` i DE `/de/`**; engleski je povučen |
| Kontakt | `+382 67 99 81 99`, `info@tumac-njemacki.me`; telefon, WhatsApp i Viber |
| Status objave | GitHub Actions **Production run #38132612919 — success**, `main` commit `d66efe4`, 11.10.2026. u 12:37 UTC |
| Provjera sitemap-a | GitHub Actions **read-only #38132882924 — success**, četiri URL-a i XML MIME |
| Aktivni PR prije ovog sređivanja | #20, `docs/handoff-v3`, **dokumentacija**; nema novih funkcionalnih izmjena od PR #19 |

**Granice potvrde:** GitHub potvrđuje završetak workflowa i verziju koda. To nije zamjena za nezavisan vizuelni test na iPhoneu/Safariju. Sead/Emir su ranije potvrdili da Viber radi; novo kompletno regresiono testiranje nije obavljeno ovim dokumentovanjem.

## 2. Šta je urađeno: V3.0 → V3.0.2

- PR **#17** (V3.0): potpuno nov mobile-first izgled, sa fokusom na posjetioce koji nijesu informatički vješti; samo ME/DE; pojednostavljen naslov, meni i koraci; veći i jasniji CTA za poziv, Viber, WhatsApp; kontakt traka na dnu telefona; lokalni fontovi. PR je spojen.
- PR **#18** (V3.0.1): uklonjeno ponavljanje naslova u zaglavlju i pojašnjena dostava kurirom za ostale gradove. Spojen.
- PR **#19** (V3.0.2): naslov usluga prilagođen Seadovoj želji; uklonjen link na državni spisak svih sudskih tumača. Spojen.
- U PR #17 opisan je smanjen približan vertikalni raspon početne stranice **~8.300 → ~4.400 px** pri testu 375 px; to je mjerenje iz Claudeovog testnog izvještaja, ne univerzalna metrika za sve telefone.
- Stari problemi vidljivi na korisnikovim screenshotovima: zaglavlje se preklapalo, sadržaj širio preko mobilnog ekrana, ogromni H1 i naslovi usluga, mnogo skrolovanja, font Italiana miješao oblike slova sa dijakriticima. V3 uvodi CSS iznova, mobilni layout, Cormorant Garamond + Manrope sa lokalnim latin/latin-ext fontovima.
- Screenshot Google Ads izvještaja imao je **100% klikova i 99,6% prikaza na telefonima** u tom prikazanom uzorku. Ne tvrditi da je to cjelokupan saobraćaj na sajtu ili Google organska statistika.

## 3. Šta je trenutno na sajtu

Indeksabilne stranice, ukupno **4**:
1. `https://tumac-njemacki.me/me/` — početna na našem jeziku.
2. `https://tumac-njemacki.me/de/` — početna na njemačkom.
3. `https://tumac-njemacki.me/me/prevod-saobracajne-dozvole.html` — vozila/saobraćajne dozvole.
4. `https://tumac-njemacki.me/de/prevod-saobracajne-dozvole.html` — njemački pandan.

Pravne stranice `/me/impressum.html`, `/de/impressum.html`, `/me/datenschutz.html` i `/de/datenschutz.html` su prisutne sa oznakom `noindex`; tekstovi su ranije odobreni od Seada. `/404.html` postoji za nedostupne URL-ove.

**EN je namjerno povučen:** u GitHubu nema `en/` ni EN linkova u sitemap-u ili hreflang-u. Produkcioni Apache `RewriteRule ^en(/.*)?$ - [G,L,NC]` vraća **410 Gone**, čak i ako stari EN HTML ostane fizički u ALL-INKL folderu (FTP upload ne briše udaljene fajlove). Ne vraćati EN niti preusmjeravati EN na ME/DE bez nove odluke. Raniji zahtjev za indeksiranje `/en/` je zastario; očekivano je njegovo ispadanje iz indeksa.

**Produkcioni canonical:** izvorni HTML i sitemap čuvaju `pages.dev` URL-ove zbog razvojnog okruženja; `deploy/prepare-allinkl-production.sh` pri pakovanju mijenja ih u `https://tumac-njemacki.me`. Ne kopirati sirove izvorne HTML datoteke direktno na produkciju.

## 4. Potvrđene poslovne i UX odluke — sačuvati

- Sajt je za **brz kontakt**, posebno za starije i informatički manje iskusne posjetioce. Premium izgled treba biti miran, profesionalan, pristupačan i čitljiv, ne „showcase” pun animacija.
- Na početnoj u zaglavlju je Seadovo ime bez dupliranja titule; H1: **„Sudski tumač za njemački jezik“**.
- Sead je odabrao naslov usluga **„Prevod dokumenata sa njemačkog i na njemački“**, a njemački **„Übersetzung von Dokumenten aus dem und ins Deutsche“**. Ne vraćati „Šta prevodim“.
- Ne postavljati link na opšti državni spisak svih sudskih tumača. Sead nije želio da vodi klijente ka konkurenciji.
- Podaci o imenovanju su iz **rješenja ministra pravde UPI-05-109/22-1418-1 od 26.12.2022**, navedenog u odobrenom Impressumu. Ne vraćati staru referencu na spisak iz 2018. Ne izmijeniti ili preuveličavati ovlašćenje.
- Podgorica, Bar, Bijelo Polje i Rožaje su mjesta **dogovorenog preuzimanja/dostave**, ne tvrdnja o četiri stalne kancelarije. Za ostale gradove navodi se mogućnost kurirske dostave po dogovoru.
- Bez izmišljanja cijena, rokova, lažnih recenzija, nezagarantovanih ishoda, „otvoreno 24/7“, kancelarija ili drugih poslovnih činjenica.
- **Facebook:** nema verifikovanog poslovnog linka. Pitati Seada; ne izmišljati profil.
- Dizajn zadržava kvalitetnu tamnoplavu/zlatnu estetiku, ali telefonski UX ima prednost.

## 5. Kontakt, privatnost i oglašavanje

### Kontakt koji se ne smije pokvariti
- Broj: `+38267998199`; e-mail: `info@tumac-njemacki.me`.
- Viber deep linkovi u `assets/site.js`: iOS `viber://contact?number=%2B38267998199`; Android `viber://chat?number=38267998199`; ostalo postojeći `viber://chat?number=%2B38267998199`. Postoji dugme „Kopiraj broj“. V3 primjenjuje platformsku izmjenu na **sve** Viber linkove.
- WhatsApp: `https://wa.me/38267998199` uz lokalizovanu početnu poruku. Klikovi nijesu garancija poslatog upita.
- Kontakt traka na dnu mobilnog ekrana: poziv, Viber, WhatsApp. JS je skriva dok je vidljiv cookie-consent i u kontakt sekciji, pojavljuje se nakon prvih hero dugmadi; testirati pri promjenama.
- Emir je izričito potvrdio da **Viber radi**. Svaku promjenu njegovog linkovanja prvo testirati na stvarnom telefonu.

### Google Ads / saglasnost
- Emir **ne želi da pokreće nove Google Ads kampanje niti da plaća nove usluge**; fokus je besplatni organski SEO.
- U naslijeđenom kodu i dalje postoji **consent-gated Google Ads tag `AW-837134242`** i konverzija za klik na WhatsApp `drLwCI3GgpYdEKLPlo8D`. Učitava se samo na zvaničnom hostname-u nakon eksplicitnog prihvatanja. To **nije** dokaz da su oglasi aktivni ili da je zabilježen stvaran lead; status Seadovih ranijih kampanja i troška nije potvrđen u ovom handoffu.
- Ne kreirati nove kampanje, budžete, konverzije, naloge niti unositi kartice bez izričitog zahtjeva. Ako Emir bude želio da ukloni Ads tracking, razmotriti zasebnu odobrenu izmjenu JS-a i tekstova privatnosti (ne uklanjati napamet).
- Saglasnost, cookie postavke i odobreni **pravni tekstovi** nijesu slobodni dizajnerski sadržaj. Mijenjati samo uz Emirovo/Seadovo odobrenje. Lokalni fontovi ne šalju zahtjeve Google Fonts; povezane rečenice iz oba teksta privatnosti su prethodno uklonjene uz odobrenje.

## 6. Google Search Console i SEO — važna ispravka starog handoffa

**Search Console je VEĆ podešen i verifikovan. Ne započinjati od nule.**
- Verifikovana je **URL-prefix property** `https://tumac-njemacki.me/` preko fajla `google9ea0a3ecbd8b4bde.html` (sadržaj mora ostati tačan). Korisnik je poslao screenshot Googleove potvrde **Ownership verified**.
- `sitemap.xml` je ranije prijavljen u Search Console. Neposredno poslije lansiranja konzola je pokazivala **“Couldn't fetch” / “Sitemap could not be read”**. Ovo je stanje iz ranije faze, **nije potvrđen trenutni Search Console status**.
- Tehnički neovisna provjera sa GitHub Actions run **#38132882924** uspješno je dohvatila novi javni sitemap: **HTTP 200, application/xml, validan XML, 4 ME/DE URL-a**. To pokazuje da sitemap nije trivijalno pokvaren, ali ne dokazuje da ga je Google indeksirao ili da je GSC ranija greška nestala.
- Prije redizajna zatraženo je indeksiranje za `/me/`, `/de/` i `/en/`. Nakon uklanjanja EN ne ponavljati zahtjev za `/en/`. Nove servisne stranice ME/DE treba posebno pregledati u Search Console i eventualno zatražiti indeksiranje.
- Provjeriti Search Console **Sitemaps, Pages, URL Inspection, Performance**. Ako je ranije prisutan “Couldn't fetch”, najprije osvježiti prikaz i pogledati datum posljednje provjere; ne brisati niti beskonačno prijavljivati sitemap bez potrebe.
- Canonical/hreflang u produkcionom buildu: ME `sr-Latn-ME`, DE `de`, `x-default` = ME; parovi su recipročni. sitemap ima **4** URL-a.
- **Nikakva DNS izmjena** nije nužna radi ponovnog verifikovanja URL-prefix property. Domain property putem TXT-a je opcija za kasnije, ne preduslov.

## 7. GitHub / održavanje koda

| Mjesto | Namjena |
| --- | --- |
| `tools/build_pages.py` | **Izvor istine za tekst i markup** početnih i vozila stranica; rječnik `C` za ME/DE |
| `me/`, `de/` | Generisani HTML; ne mijenjati ručno bez usklađivanja generatora |
| `assets/site.css` | Novi V3 mobile-first CSS; self-hosted Cormorant Garamond i Manrope u `assets/fonts/` |
| `assets/site.js` | Meni, Viber, sticky kontaktna traka, consent/Ads |
| `me|de/impressum.html`, `me|de/datenschutz.html` | Pravni tekst; generator čuva `<main>` i pravne naslove, ali diff pregled je obavezan |
| `sitemap.xml`, `robots.txt`, `_redirects` | Pretraga/Cloudflare; produkcioni paket mijenja domenu |
| `google9ea0a3ecbd8b4bde.html` | Search Console verifikacija — ne dirati |
| `deploy/prepare-allinkl-production.sh` | Lokalni produkcioni paket, canonical rewrite, provjere i Apache `.htaccess` |
| `deploy/prepare-allinkl-staging.sh` | Test paket i `noindex` zaštita |
| `.github/workflows/` | Staging auto na `main`, produkcija samo ručno; dodatne dijagnostike |
| `docs/v3/` | Screenshotovi prvobitnog V3; nisu nužno posljednja verzija |
| `docs/HANDOFF.md` | Ovaj dokument — glavni handoff za sljedeću sesiju |

**Tipični sadržajni tok:** nova grana → izmjena `tools/build_pages.py` → `python3 tools/build_pages.py` → pregled generisanog diff-a (naročito pravni tekstovi/consent) → provjere → PR → merge na `main` → automatski **staging** → pregled na telefonu → **samo uz odobrenje** ručni production.

Pri promjenama CSS-a ili JS-a povećati `ASSET_V` u generatoru (trenutno `3.0.0`) radi cache-bustinga. Nakon generisanja provjeriti da nema neplaniranog odstupanja pravnih tekstova i da ME/DE ostaju usklađeni.

## 8. Objava i bezbjednost

- **Staging:** GitHub Actions `ALL-INKL staging (auto + manual, isolated)` na push/merge u `main`. Na testnom hostu robots zabrana i noindex. Ne treba dirati produkcioni Document Root.
- **Produkcija:** GitHub Actions `ALL-INKL production (manual, guarded)`; isključivo ručni `workflow_dispatch` s parametrom `release_approval=PUBLISH_BLUEGOLD_LIVE`. Provjerava odvojeni ograničeni FTP nalog, marker `.tumac-production-guard` sa `TUMAC_PRODUCTION_ONLY_V1` i odobrene pravne stranice. FTP mirror ne briše udaljene fajlove.
- **Posljednja uspješna produkciona objava:** run https://github.com/emiretfde/tumac-njemacki/actions/runs/38132612919, izvorni commit `d66efe4` (V3.0.2).
- Korisniku prvo dati link do testnog sajta i zatražiti potvrdu. **Nikada automatski ne pokreći produkcioni deployment**, ne mijenjati DNS/KAS, e-mail postavke, FTP korisnike, nikad objavljivati lozinke ili mijenjati zaštitne mehanizme.
- Apsolutni javni URL-ovi u Apache redirectima su neophodni jer relativni preusmjerivači na ALL-INKL mogu otkriti `/www/htdocs/...` putanju.
- Root `/` → `/me/` i `www` → apex su trenutno **302**, a ne 301, prema `deploy/prepare-allinkl-production.sh`. Eventualni prelaz na 301 planirati poslije potvrde i testova, bez naglog mijenjanja svih pravila.
- EN `/en/*` na produkciji je **410**. Zbog nedeletujućeg FTPS-a stari fajlovi možda fizički postoje; ne uklanjati ručno bez backup-a, a 410 pravilo ne dirati bez razloga.

## 9. Šta je testirano, a šta još treba provjeriti

**Prema PR #17 i Claudeovom izvještaju:** testovi renderovanja na širinama 320, 360, 375, 390, 414, 430, 768, 1280 i 1440 px, bez horizontalnog skrola i preklapanja; HTML/SEO i keyboard/no-JS; Apache `.htaccess` lokalno. U repozitorijumu su screenshotovi. Ovo nije nezavisno ponovljen test u trenutku pisanja handoffa.

**Prema GitHub Actions:** staging i produkcija za `d66efe4` su uspješno završeni, a dijagnostika sitemap-a poslije te objave je uspješna.

**Treba ponovo ručno provjeriti na uređajima:** stvarni iPhone/Safari (manji i veći), Android/Chrome, duge naslove i header/meni, mobilnu kontakt traku i cookie banner, klik na poziv/Viber/WhatsApp/mail, copy-number fallback, prikaz ME/DE i pravnih stranica, kontrast/dodirna polja, `/en/` i korijenski redirect. Ne tvrditi da je WebKit/Safari automatizovano testiran ako nije.

## 10. Otvoreno / prioriteti za narednu Claude sesiju

**P0 — Bez novih izmjena produkcije.** Provjeriti da `main` i posljednji live workflow odgovaraju V3.0.2. Pročitati ovaj handoff, `tools/build_pages.py` i završne Seadove komentare.

**P1 — Zajedno sa Emirom pregledati mobilni UX**, prvenstveno stvarni iPhone i Android. Eventualne sitne korekcije u novoj grani, bez vraćanja predugih hero naslova i suvišnih dekoracija. Ako je sajt čitljiv, ne pokretati novi redizajn bez potrebe.

**P2 — Search Console:** otvoriti već verifikovanu property, provjeriti sadašnji status prijavljenog sitemap-a i indeksiranja, pregledati četiri aktivne adrese, posebno dvije nove stranice za vozila; EN je povučen. Ne obećavati poziciju ili datum indeksiranja.

**P3 — SEO/on-page:** uz odobrenje Seada unaprijediti korisne sadržaje za stvarne upite (sudski tumač njemački, ovjereni prevod, saobraćajne dozvole), ali bez doorway stranica i bez izmišljenih usluga.

**P4 — Potvrditi kod Seada** postoji li Facebook poslovna stranica; tek sa ispravnim linkom dodati dugme. Provjeriti poslovne činjenice prije objave.

**P5 — Opcionalno nakon stabilizacije:** promjena root/www `302` u `301` (provjeriti pažljivo), Google Business Profile samo ako ispunjava stvarne uslove, dodatna funkcionalna/SEO provjera. Google Ads ne otvarati osim na izričit zahtjev; ne pokretati trošak.

**Odvojeni projekat:** U ranijem Claude handoffu pominje se ideja „Tumač AI“ za rad sa dokumentacijom vozila na mogućem `app.tumac-njemacki.me`. To **nije** dio ovog sajta i ne smije mijenjati trenutni hosting/DNS bez zasebnog projekta i odobrenja.

## 11. Kako da Claude nastavi bez pitanja za već poznate stvari

> Nastavljamo postojeći sajt tumac-njemacki.me. Prvo pročitaj `docs/HANDOFF.md`, provjeri zadnji `main` commit i posljednji GitHub Actions production run, pa mi u 5–8 rečenica reci stvarno trenutno stanje i najvažniji sljedeći korak. Ništa ne mijenjaj na produkciji bez moje izričite potvrde. Fokus je jednostavan mobile-first sajt za stvarne klijente, ME/DE i besplatni SEO, uz očuvanje Vibera, pravnih tekstova, kontakata i Search Console verifikacije. O novim kampanjama, troškovima ili projektu „Tumač AI“ ne radi dok ih posebno ne zatražim.

## 12. Referentni tragovi

- V3 redizajn: https://github.com/emiretfde/tumac-njemacki/pull/17
- V3.0.1: https://github.com/emiretfde/tumac-njemacki/pull/18
- V3.0.2: https://github.com/emiretfde/tumac-njemacki/pull/19
- Staging/production status: https://github.com/emiretfde/tumac-njemacki/actions
- Produkcija V3.0.2: https://github.com/emiretfde/tumac-njemacki/actions/runs/38132612919
- Sitemap HTTP dijagnostika: https://github.com/emiretfde/tumac-njemacki/actions/runs/38132882924

**Komunikacija:** crnogorski / latinica / ijekavica; kratko, jasno i direktno. Nepoznate poslovne činjenice pitati umjesto da se izmisle.
