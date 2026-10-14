# HANDOFF — Sead Crnovršanin / tumac-njemacki.me
**Stanje: 11. oktobar 2026. | V3.0.2 mobile-first uživo; SEO 301 i razvojni noindex potvrđeni javnim HTTP testom | izvor istine za narednu Claude sesiju**

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
| Posljednja produkciona objava | GitHub Actions [**run #38148026015**](https://github.com/emiretfde/tumac-njemacki/actions/runs/38148026015) — **Success**, `main` commit `6df1d5137`, 11.10.2026, oko 16:39 CG |
| Posljednja javna SEO HTTP provjera | GitHub Actions [**run #38148909477**](https://github.com/emiretfde/tumac-njemacki/actions/runs/38148909477) — **Success**, 11.10.2026, 16:52 CG; 301, 200, 410, sitemap i Cloudflare noindex potvrđeni |
| Trenutno stanje PR-ova | Nema otvorenih PR-ova. PR #25 (301), #27 (Cloudflare noindex) i #29 (read-only provjera) spojeni. |

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
- Viber deep linkovi u `assets/site.js`: iOS `viber://chat?number=%2B38267998199` (od V3.0.1, ranije `viber://contact`, koji je otvarao samo karticu kontakta, a ne chat); Android `viber://chat?number=38267998199`; ostalo postojeći `viber://chat?number=%2B38267998199`. Postoji dugme „Kopiraj broj“. V3 primjenjuje platformsku izmjenu na **sve** Viber linkove.
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
- **Produkcija pri posljednjem uspješnom live deployu** (`d66efe4`) koristila je **302** za root/www. U sadašnjem `main` je produkciona build skripta promijenjena na **301** za root/www/`index.html` (PR #25), ali ta izmjena **nije objavljena uživo** dok korisnik ne odobri novi manual production deploy. Alias preusmjeravanja pravnih stranica ostaju 302; EN ostaje 410.
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

**P5 — Završni mali SEO posao:** `301` za root/www/`index.html` već je pripremljen i spojen u `main`, ali treba ručni odobreni production deploy i provjeru HTTP odgovora. Google Business Profile trenutno odložen (nema potvrđene stalne kancelarije ili terenske usluge). Google Ads ne otvarati osim na izričit zahtjev; ne pokretati trošak.

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


### Dopuna 11.10.2026, oko 15:47 (Google Search Console — screenshotovi korisnika)

- **ME početna je potvrđeno indeksirana:** GSC URL Inspection za `https://tumac-njemacki.me/me/` prikazuje **“URL is on Google”** i **“Page is indexed”**; HTTPS je zelen.
- **Pages zbirni izvještaj još nije spreman:** Google prikazuje **“Processing data, please check again in a day or so”**. Zbog toga nema pouzdanog ukupnog broja indeksiranih/neindeksiranih URL-ova.
- **Prijavljeni sitemap još prikazuje grešku:** `/sitemap.xml` ima status **“Couldn't fetch”**, tip **“Unknown”**, otkriveno **0** URL-ova. U detaljima: **“Sitemap could not be read”**; `Last read: 10/11/26`. Ovo je stanje iz GSC interfejsa u ovom trenutku, a ne dokaz da je javni XML neispravan.
- **Kontrolni dokaz suprotan grešci:** GitHub Actions read-only test #38132882924 ranije istoga dana uspješno je dohvatio javni XML, `HTTP 200`, `application/xml`, četiri ME/DE URL-a. Novi neposredni mrežni test u ChatGPT okruženju nije bio moguć (DNS ograničenje samog okruženja), pa **ne tvrditi da je ponovo potvrđen Googlebotov pristup**.
- **Zaključak:** Moguće je da Search Console još nije obradio novi sitemap; Googleova pomoć navodi i druge razloge poput privremenog nedostupnog servera, robots zabrane ili manual action. Nije pronađen dokaz konkretne greške koju treba mijenjati na serveru. **Ne brisati/resubmitovati sitemap u krug.** Sačekati 24–72 sata pa provjeriti GSC izvještaj; ako status i dalje stoji, provjeriti robots, pristup Googlovog robota, hosting logove i konkretne HTTP odgovore sa spoljne mreže.
- **Naredni ručni korak:** URL Inspection `https://tumac-njemacki.me/de/`, zatim `/me/prevod-saobracajne-dozvole.html` i `/de/prevod-saobracajne-dozvole.html`. Ako imaju status “URL is not on Google” uz uspješan Live Test, zatražiti indeksiranje pojedinačno.
- **Odvojena SEO promjena:** draft PR #21 `seo/noindex-cloudflare-development` predlaže `_headers` za razvojni Pages hostname; **nije spojen, nije objavljen**, nije dio ovog GSC nalaza. Prije spajanja treba potvrditi semantiku Cloudflare `_headers` i provjeriti da zaista važi samo na razvojnom hostu. Nikako ne dodati `noindex` na produkciju.
- Nema izmjena HTML/CSS/JS, vizuelnog dizajna ili produkcionog deploya tokom ovog koraka.


### Dopuna 11.10.2026, oko 16:10 — pregled svih 4 produkciona indeksabilna URL-a (screenshotovi)

| URL | Google Index / status | Google Live Test |
| --- | --- | --- |
| `/me/` | **Indeksiran** — `URL is on Google` / `Page is indexed` | raniji uspješan test |
| `/de/` | **Nije indeksiran** — `URL is unknown to Google`; `No referring sitemaps detected`; `Last crawl: N/A` | **Indexable** — `URL is available to Google` |
| `/me/prevod-saobracajne-dozvole.html` | **Nije indeksiran** — `URL is unknown to Google`; `No referring sitemaps detected`; `Last crawl: N/A` | **Indexable** — `URL is available to Google`; **Breadcrumbs: 1 valid item** |
| `/de/prevod-saobracajne-dozvole.html` | **Nije indeksiran** — `URL is unknown to Google`; `No referring sitemaps detected`; `Last crawl: N/A` | **Indexable** — `URL is available to Google`; **Breadcrumbs: 1 valid item** |

- Potvrđeno je **1/4 indeksiran**, 3/4 trenutno još nijesu u Google indeksu. Uspješan Live Test ne znači da je URL već indeksiran.
- Google Search Console `Pages` zbirni izvještaj još obrađuje podatke, a `sitemap.xml` i dalje pokazuje `Couldn't fetch` / 0 discovered prema GSC screenshotovima oko 15:47, bez nove potvrde statusa poslije toga. Ranija nezavisna XML HTTP dijagnostika je prošla.
- `/de/` je **već ranije poslat** putem Request Indexing; ne slati opet bez potrebe.
- **Korisniku je preporučeno** da pojedinačno klikne `REQUEST INDEXING` na dvije stranice o vozilima, **ako nije ranije**; nema potvrde da je to već uradio. Ne evidentirati kao urađeno dok ne potvrdi.
- Ne mijenjati SEO HTML/CSS/server zbog sadašnjeg statusa; sačekati novo Google indeksiranje i ponovno čitanje sitemap-a. Provjeriti ponovo narednih dana. **Status nije dokaz blokade indeksiranja.**
- Nema nove izmjene produkcionog sajta, DNS-a, robota ili plaćenih kampanja. Postojeći nacrt PR #21 za Cloudflare razvojni noindex ostaje zasebno na čekanju.


### Dopuna 11.10.2026 — poslat Request Indexing za servisne stranice

- Emir je nakon pregleda rezultata potvrdio **„Kliknuo sam request indexing“** za dvije ranije razmatrane stranice o saobraćajnim dozvolama (`/me/prevod-saobracajne-dozvole.html` i `/de/prevod-saobracajne-dozvole.html`). Raniji zahtjev za `/de/` je već bio poslat. **Ne ponavljati ove zahtjeve bez potrebe.**
- **Posljednji potvrđeni indeksni status i dalje je 1/4** (ME početna u indeksu; DE početna i dvije servisne stranice imaju uspešan Live Test, ali nijesu bile indeksirane na zadnjem screenshotu). Zahtjev za indeksiranje nije dokaz da je indeksiranje završeno.
- GSC Sitemaps posljednji screenshot: `Couldn't fetch` / 0 discovered; tehnički read-only XML test je prošao. Sačekati dalju obradu i provjeriti opet za 24–72 sata; nema potrebe dirati sitemap odmah.
- Pregledane javne preporuke: Cloudflare Pages službeno podržava host-specifični apsolutni URL u `_headers` pravilima i `:version` placeholder u hostname-u (https://developers.cloudflare.com/pages/configuration/headers/). Zato nacrt PR #21 tehnički odgovara Cloudflare dokumentovanoj sintaksi; **još je draft i nije spojen niti nezavisno testiran na live Pages hostu**.
- Google preporučuje **trajno 301 preusmjeravanje** kada je kanonski URL stabilan (https://developers.google.com/search/docs/crawling-indexing/301-redirects). Produkcioni root i www trenutno su 302, pa je prelazak na 301 zasebna predložena tehnička SEO optimizacija — bez objave dok se ne odobri i provjeri.


### Dopuna 11.10.2026 — Google Business Profile (Google Maps) odložen

- Emir procjenjuje da Sead **nema stalnu kancelariju** za prijem klijenata. To je preliminarna informacija, još ne potvrđeno sa Seadom.
- **Odluka:** ne otvarati, ne verifikovati i ne oglašavati novu Google Maps/Business Profile lokaciju. Lokalni SEO nastaviti kroz postojeći sajt, Google Search Console i korisne ME/DE stranice. Nema promjene u HTML-u, dizajnu ili produkciji.
- **Nijansa u Google pravilima:** stalni lokal nije neophodan ako biznis zaista **lično dolazi kod kupaca/klijenata** (service-area business, sa skrivenom javnom adresom). Međutim, potpuno online model bez fizičkog kontakta sa klijentima nije podoban. Izvor: https://support.google.com/business/answer/3038177 i https://support.google.com/business/answer/13763036 .
- Samo ako Sead kasnije potvrdi redovan **neposredan kontakt sa klijentima na terenu**, razmotriti da li ispunjava Googleove uslove za service-area business. Samo preuzimanje preko kurira / online komunikacija nije dovoljan dokaz podobnosti. **Ne izmišljati poslovnu adresu ni fiksne kancelarije u četiri grada.**


## 14. Završene male SEO promjene u GitHubu — 11.10.2026. (NAJNOVIJE STANJE)

**Urađeno u kodu, a ne na zvaničnoj produkciji:**
- **PR #25 SPOJEN**, merge `a9c977c`: u `deploy/prepare-allinkl-production.sh` root `/` → `/me/`, `/index.html` → `/me/`, `www` → apex mijenjaju status preusmjeravanja sa **302 na 301**. Nema drugih promjena odredišta. Pravne alias adrese ostaju 302, a `/en/*` 410. **Dok se manual production workflow ne pokrene i provjeri, zvanični sajt i dalje koristi staru, ranije objavljenu konfiguraciju.**
- **PR #27 SPOJEN**, merge `ce8192f`: izvorni `_headers` sadrži **host-specifični** `X-Robots-Tag: noindex` isključivo za `tumac-njemacki.pages.dev/*` i branch preview na Cloudflare Pages. ALL-INKL produkcioni build ima eksplicitnu copy-listu i **ne kopira** `_headers`; zvanične ME/DE stranice time nijesu označene kao noindex. Sintaksa potvrđena u https://developers.cloudflare.com/pages/configuration/headers/ . Cloudflare Pages HTTP header **nije potvrđen uživo** zbog mrežnog ograničenja trenutnog izvršnog okruženja. Potrebna je provjera nakon Cloudflare objave.
- Stari **draft PR #21 ZATVOREN bez mergea**; sadržavao je zastarjeli handoff i zamijenjen je čistim PR #27. Nema više otvorenih PR-ova pri ovoj provjeri.
- Posljednji potvrđeni Google indeks: **1/4 URL-a** (ME početna); zahtjevi za indeksiranje druge 3 stranice su poslati (DE početna ranije, dvije servisne po korisničkoj potvrdi). `Pages` izvještaj se još obrađivao, a `Sitemaps` u posljednjem screenshotu pokazivao `Couldn't fetch` / 0 discovered. Nema novijih podataka iz Google konzole. Tehnička XML dijagnostika je prethodno prošla. Ne mijenjati sitemap bez novog dokaza problema.
- Google Business Profile za sada **odložen** dok Sead ne potvrdi uslove za lični kontakt sa klijentima. Ne izmišljati adresu.

**Sljedeći konkretan korak / obavezna potvrda:**
1. Za zvanični sajt korisnik treba **izričito odobriti i pokrenuti** ručni zaštićeni `ALL-INKL production (manual, guarded)` workflow na `main`, unos `release_approval=PUBLISH_BLUEGOLD_LIVE`. Ne tvrditi da je 301 aktivan prije `Success` i provjere.
2. Poslije objave provjeriti `https://tumac-njemacki.me/` → 301 `https://tumac-njemacki.me/me/`, `https://www.tumac-njemacki.me/me/` → 301 apex `/me/`, `/index.html` → 301 `/me/`, i dalje `/me/`, `/de/`, dvije stranice za vozila 200/indexable, `/en/` 410 i sitemap 200/XML. Ako test nije moguć u alatu, tražiti korisnički potvrđen rezultat.
3. Pregledati stvarno `X-Robots-Tag` zaglavlje na `tumac-njemacki.pages.dev/me/` (treba noindex) i zvaničnom hostu (ne smije noindex); provjera još čeka.
4. Poslije 24–72 sata ponovo pregledati Google Search Console status svih stranica i sitemap-a. Ne ponavljati Request Indexing nepotrebno.
5. Poslije završne provjere ažurirati ovaj handoff sa **potvrđenim live statusom**; Claude i ChatGPT koriste isti izvor istine.

**Bez novih kampanja, troškova, frontend dizajnerskih ili sadržajnih promjena.**


## 15. Produkcioni deployment i završni SEO HTTP test — 11.10.2026, oko 16:42

- **Potvrđeno iz GitHub Actions API-ja i screenshot-a korisnika:** `ALL-INKL production (manual, guarded) #8`, https://github.com/emiretfde/tumac-njemacki/actions/runs/38148026015, **Success**, `main` commit `6df1d5137895864468c08bfe154f7562af100e6a`, 11.10.2026. u 14:38:49–14:39:30 UTC. Prošli su `Verify site and legal readiness`, provjera ograničenog FTP naloga, guard marker i `Upload production package`. Build na tom commitu sadrži pripremljena **301** preusmjeravanja za `www`, `/` i `/index.html`.
- **Ograničenje dokaza:** uspješan workflow dokazuje da je paket prenijet u ograničeni LIVE folder, ali **nije** nezavisna potvrda kako javni HTTP server odgovara na svaku adresu. Direktni `curl` iz ChatGPT izvršnog okruženja i alat za web pristup nijesu mogli da razriješe/dohvate domen; ovo je ograničenje okruženja, ne dokazana greška sajta. Zato ne označavati javne 301/200/410 odgovore kao testirane dok ne postoji nova potvrda.
- **Novi read-only dijagnostički workflow:** `.github/workflows/verify-live-seo.yml`, ručno `workflow_dispatch`, **bez secrets, FTP-a i upisa**. Poslije spajanja dostupan je na https://github.com/emiretfde/tumac-njemacki/actions/workflows/verify-live-seo.yml . Treba ga jednom pokrenuti sa `main` i pročitati `check-public-site` rezultate za: root/www/index `301`, sve četiri ME/DE stranice `200` bez `noindex`, `/en/` `410`, `sitemap.xml` ispravan XML sa četiri URL-a, `robots.txt` referencu. Cloudflare `pages.dev` `X-Robots-Tag: noindex` je odvojeno **upozorenje**, jer još treba potvrditi da je Pages automatski objavio izvorni `_headers`.
- **Završni status:** produkcioni deploy **potvrđeno uspješan**; javna HTTP dijagnostika još **čeka pokretanje ili nezavisnu potvrdu**. Ne raditi novu produkcionu objavu samo radi read-only testa. Poslije testa zabilježiti konkretne HTTP statuse i eventualne popravke.
- Google Search Console: posljednje potvrđeno **1/4 indeksiran**, request indexing poslato za preostale 3 stranice, sitemap još `Couldn't fetch` na starijem screenshotu. Ne ponavljati zahtjeve bez potrebe; ponovo pregledati narednih dana.


## 16. ZAVRŠNA JAVNA SEO HTTP PROVJERA — 11.10.2026, 16:52 CG (NAJNOVIJE)

**Izvor:** [GitHub Actions run #38148909477](https://github.com/emiretfde/tumac-njemacki/actions/runs/38148909477), `check-public-site` **Success**, commit `3dbdee0a6f8ce71789a69835fb9900c2765d332a`. Rezultati pročitani iz stvarnog GitHub Actions job loga.

| URL / resurs | Izmjeren rezultat |
| --- | --- |
| `https://tumac-njemacki.me/` | **301** → `https://tumac-njemacki.me/me/` |
| `https://tumac-njemacki.me/index.html` | **301** → `https://tumac-njemacki.me/me/` |
| `https://www.tumac-njemacki.me/me/` | **301** → `https://tumac-njemacki.me/me/` |
| `/me/`, `/de/` | **200**, HTML, canonical na zvaničnom domenu, bez noindex |
| `/me/prevod-saobracajne-dozvole.html`, `/de/prevod-saobracajne-dozvole.html` | **200**, HTML, canonical na zvaničnom domenu, bez noindex |
| `/en/` | **410 Gone** |
| `/sitemap.xml` | **200**, `application/xml`, validan XML sa tačno četiri očekivana URL-a |
| `/robots.txt` | **200**, `Sitemap:` upućuje na produkcioni XML |
| `https://tumac-njemacki.pages.dev/me/` | **200**, `X-Robots-Tag: noindex` (razvojni host) |

**Sve javne HTTP provjere su prošle, bez upozorenja.** Raniji navodi u sekcijama 14–15 da „301/noindex čekaju objavu/provjeru” su ISTORIJSKO stanje prije ovog testa; ne ponavljati produkcionu objavu. Zvanični sajt nije označen kao noindex.

**Otvorena stavka ostaje samo Google Search Console:** zadnji korisnički izvještaj je **1/4 indeksiran** (ME početna), za ostale tri stranice je poslat Request Indexing; GSC sitemap je na starijem screenshotu prijavljivao `Couldn't fetch / 0 discovered`, iako su javni HTTP/XML testovi uspješni. Čekati novu GSC obradu i provjeriti za 24–72 sata. Ovaj test ne dokazuje da je Google već indeksirao sve četiri stranice.

Nema novih kampanja/troškova, dizajnerskih promjena ni dodatnih produkcionih akcija. Cloudflare `noindex` i `301` preusmjeravanja su završena i provjerena.
