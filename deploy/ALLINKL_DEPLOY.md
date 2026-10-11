# ALL-INKL: bezbjedna veza GitHub -> hosting

## Trenutna faza: SAMO STAGING
Nas Blue & Gold sajt radi sa GitHubom i Cloudflare Pages.
Trenutni javni domen tumac-njemacki.me je na ALL-INKL-u u folderu /tumac-novi/.

Ova automatizacija NE SMIJE i NECE sada postavljati fajlove u /tumac-novi/.
Nije ukljucena automatska objava niti postoji FTP nalog za produkciju.
Prije prelaska treba sacuvati trenutno aktivni sajt sa pravnim stranicama, privatnoscu i Google Ads mjerenjem.

## ALL-INKL KAS: izolovani test
1. Napraviti provjerenu rezervnu kopiju cijelog /tumac-novi/ direktorijuma, ukljucujuci index.html, impressum.html, datenschutz.html, README.txt i assets/.
2. U WebFTP napraviti NOVI PRAZAN folder /tumac-staging/. Ne dirati /tumac-novi/.
3. U novom /tumac-staging/ folderu preko WebFTP > New file napraviti fajl .tumac-staging-guard ciji je jedini tekst TUMAC_STAGING_ONLY_V1 (bez dodatnog teksta). Bez tog sigurnosnog markera workflow odbija upload.
4. U KAS > Subdomains otvoriti preview.tumac-njemacki.me i povezati ga sa /tumac-staging/. Aktivirati SSL i provjeriti da poddomen radi.
5. U KAS > FTP > Create new FTP user napraviti dodatnog, posebnoga FTP korisnika ciji je Directory ISKLJUCIVO /tumac-staging/. Ne koristiti glavni korisnik w01a14cb.
6. Postaviti novu jaku lozinku. NE SLATI LOZINKU U CHAT NITI U GITHUB FAJLOVE.

## GitHub Secrets
Otvoriti GitHub repozitorijum -> Settings -> Secrets and variables -> Actions -> New repository secret.
Unijeti:
- ALLINKL_STAGE_FTP_USER : dodatni FTP korisnik ogranicen na staging direktorijum.
- ALLINKL_STAGE_FTP_PASSWORD : njegova posebna nova lozinka.

FTP host je w01a14cb.kasserver.com. Koristi se explicit FTPS uz provjeru TLS sertifikata.
Automatizacija PRVO provjerava da FTP root sadrzi .tumac-staging-guard sa sadrzajem TUMAC_STAGING_ONLY_V1. Ako ga nema, odbija upload. Tek nakon te provjere salje fajlove u FTP root dodatnog korisnika, bez brisanja udaljenih fajlova.

## PRVI test (rucni)
1. GitHub -> Actions -> ALL-INKL staging (manual, isolated) -> Run workflow -> main.
2. Sacekati zelen status. Ako FTPS TLS provjera ne uspije, ne iskljucivati certifikat.
3. Testirati https://preview.tumac-njemacki.me/me/ i /de/; /en/ mora preusmjeriti na /me/ (V3).
4. Provjeriti CSS, telefon, WhatsApp, Viber na mobilnom uredjaju, navigaciju i brzinu.
5. Provjeriti da preview domen ne moze u Google: staging robots.txt je Disallow: / i Apache header je noindex.
6. Provjeriti da korijenska adresa preview domena vodi na /me/ preko privremenog HTTP 302.
7. Ne objavljivati testni paket na glavnom domenu; nema svih produkcijskih elemenata.

## PRIJE PREBACIVANJA PRODUKCIJE
1. Provjeriti rezervnu kopiju i postupak vracanja stare verzije.
2. Preuzeti postojeci Impressum, Datenschutz i odgovarajuci sistem saglasnosti.
3. Dodati Google Ads tag AW-837134242 i konverzije uz pravilno postovanje izbora korisnika.
4. Promijeniti trenutne kanonske URL-ove (sada pages.dev) na https://tumac-njemacki.me, ukljucujuci canonical, hreflang, og:url, sitemap.xml i robots.txt.
5. Potvrditi Google Ads i pravne stranice na testnom okruzenju.
6. Tek tada napraviti odvojeni produkcijski FTP nalog i produkcijsku GitHub Actions objavu. Potreban je pristup ogranicen na novi odobren produkcijski direktorijum.
7. Nakon uspjesne objave na novom direktorijumu moze se promijeniti Document Root sa /tumac-novi/ na novu verziju, uz provjeren rollback.

## Automatsko objavljivanje nakon testiranja
Prvo je deployment rucan, bez mogucnosti slucajne produkcijske objave.
Kada test prodje, workflow moze dobiti okidac za push na main.
Kasnije se odvojeni produkcijski proces moze automatizovati nakon provjerenog cutovera.
GitHub ostaje centralni izvor sajta, a Cloudflare Pages moze sluziti za razvoj.

## Sigurnost
- Ranije podijeljenu ALL-INKL lozinku treba promijeniti.
- Staging se nikad ne smije povezati sa glavnim FTP nalogom.
- Nema FTP lozinki u kodu, porukama niti u screenshotima.
- E-mail, DNS i nameserveri se ne mijenjaju u ovoj fazi.

Izvori:
- ALL-INKL FTPS: https://all-inkl.com/wichtig/faq
- GitHub Actions Secrets: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
