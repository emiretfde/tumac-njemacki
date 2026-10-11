#!/usr/bin/env python3
"""Generate the V3 static pages for /me/ and /de/.

Run from the repository root:  python3 tools/build_pages.py

* Home and vehicle pages are written from the copy below.
* Legal pages (impressum, datenschutz): the <main> content and the page title are
  read from the CURRENT file and re-wrapped unchanged, so approved legal text is
  never retyped. The consent notice text of every page is also carried over as-is.
* Canonical/hreflang use the staging host; deploy/prepare-allinkl-production.sh
  rewrites them to https://tumac-njemacki.me for the live package.
No network access, no dependencies beyond the Python standard library.
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://tumac-njemacki.pages.dev"
PHONE_HREF = "tel:+38267998199"
PHONE = "+382\u00a067\u00a099\u00a081\u00a099"  # non-breaking spaces: the number never wraps
MAIL = "info@tumac-njemacki.me"
VIBER_HREF = "viber://chat?number=%2B38267998199"  # rewritten per platform by site.js (V10 logic)
HREFLANG = {"me": "sr-Latn-ME", "de": "de"}
ASSET_V = "3.0.0"

ICONS = {
 "phone": '<path d="M7.3 3.5H4.9c-.8 0-1.4.6-1.4 1.4A16.6 16.6 0 0 0 19.1 20.5c.8 0 1.4-.6 1.4-1.4v-2.4c0-.6-.4-1.2-1-1.3l-3.1-.7c-.5-.1-1 .1-1.3.5l-1.1 1.3a13 13 0 0 1-6.5-6.5l1.3-1.1c.4-.3.6-.8.5-1.3l-.7-3.1c-.1-.6-.7-1-1.3-1z"/>',
 "mail": '<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="m3.8 7 8.2 6 8.2-6"/>',
 "whatsapp": '<path d="M20.3 11.8a8.3 8.3 0 0 1-12.2 7.3L3.6 20.5l1.5-4.4a8.3 8.3 0 1 1 15.2-4.3z"/><path d="M8.5 8.7c.2-.3.5-.4.8-.2l1.2.7c.3.2.4.5.3.8l-.4 1c.7 1.3 1.7 2.3 3 3l1-.4c.3-.1.6 0 .8.3l.7 1.2c.2.3.1.6-.2.8-.6.4-1.3.5-2.1.2-2.5-.9-4.8-3.2-5.7-5.7-.3-.8-.2-1.5.2-2.1z"/>',
 "viber": '<path d="M11.6 3.4c-5.1 0-8.3 2.7-8.3 7.4 0 2.4 1.1 4.2 3 5.4l-.7 3.6 4.1-1.8c.6.1 1.2.1 1.9.1 5.1 0 8.4-2.6 8.4-7.3 0-4.7-3.3-7.4-8.4-7.4z"/><path d="m8.7 9 .9-.5 1.3 1.8-.6.8c.5 1 1.3 1.8 2.3 2.3l.8-.6 1.8 1.3-.5.9c-.2.5-.8.7-1.4.5-2.4-.8-4.6-3-5.4-5.4-.2-.6.1-1.2.8-1.1z"/><path d="M13.2 7.1a3.6 3.6 0 0 1 3.5 3.5M13.3 5.2a5.4 5.4 0 0 1 5.3 5.3"/>',
 "pin": '<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "close": '<path d="M6 6l12 12M18 6 6 18"/>',
 "id": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="11" r="2.2"/><path d="M5.5 16c.6-1.5 1.7-2.2 3-2.2s2.4.7 3 2.2M14 10h4M14 13.5h3"/>',
 "cap": '<path d="m2.5 9 9.5-4.5L21.5 9 12 13.5z"/><path d="M6.5 11v4.2c1.4 1.4 3.4 2.1 5.5 2.1s4.1-.7 5.5-2.1V11M21.5 9v5"/>',
 "car": '<path d="M4 16.5v-4l1.8-4.6A2 2 0 0 1 7.7 6.6h8.6a2 2 0 0 1 1.9 1.3l1.8 4.6v4"/><path d="M3 12.5h18v4H3zM6 16.5V19M18 16.5V19"/><circle cx="7" cy="14.5" r=".6"/><circle cx="17" cy="14.5" r=".6"/>',
 "contract": '<path d="M6 3h8.5L19 7.5V21H6z"/><path d="M14 3v5h5M9 12h7M9 15.5h7M9 19h3.5"/>',
 "briefcase": '<rect x="3" y="7" width="18" height="12.5" rx="2"/><path d="M8.5 7V5.5A1.5 1.5 0 0 1 10 4h4a1.5 1.5 0 0 1 1.5 1.5V7M12 10.5v5M9.5 13h5"/>',
 "stamp": '<circle cx="12" cy="10" r="6.5"/><circle cx="12" cy="10" r="4"/><path d="M5 20.5h14M8.5 16.5l-1 4M15.5 16.5l1 4"/>',
 "chevron": '<path d="m9 6 6 6-6 6"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
}

def icon(name, cls="icon"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'

def stamp(text, pid):
    """Decorative round seal — the court translator's stamp is the site's one signature element."""
    t = html.escape(text)
    return (f'<svg viewBox="0 0 200 200" aria-hidden="true" focusable="false">'
            f'<circle cx="100" cy="100" r="96" fill="none" stroke="currentColor" stroke-width="2"/>'
            f'<circle cx="100" cy="100" r="88" fill="none" stroke="currentColor" stroke-width="1"/>'
            f'<circle cx="100" cy="100" r="58" fill="none" stroke="currentColor" stroke-width="1.5"/>'
            f'<path id="{pid}" d="M100 100m-73 0a73 73 0 1 1 146 0a73 73 0 1 1-146 0" fill="none"/>'
            f'<text font-family="Manrope,Arial,sans-serif" font-size="12.5" font-weight="600" fill="currentColor">'
            f'<textPath href="#{pid}" startOffset="0" textLength="452" lengthAdjust="spacing">{t}</textPath></text>'
            f'<text x="100" y="117" text-anchor="middle" font-family="Cormorant Garamond,Georgia,serif" font-size="50" font-weight="600" fill="currentColor">SC</text>'
            f'</svg>')

# ---------------------------------------------------------------- copy
C = {
 "me": dict(
  skip="Preskoči na sadržaj", menu="Meni", menu_open="Otvori meni", lang_label="Izaberite jezik",
  role="Sudski tumač za njemački jezik", home="Početna",
  nav=[("usluge","Usluge"),("proces","Kako funkcioniše"),("o-meni","O meni"),("dostava","Preuzimanje"),("pitanja","Pitanja"),("kontakt","Kontakt")],
  call="Pozovite", stamp="SUDSKI TUMAČ ZA NJEMAČKI JEZIK  ·  CRNA GORA  ·  ",
  wa="https://wa.me/38267998199?text=Po%C5%A1tovanje%2C%20%C5%BEelim%20informacije%20o%20prevodu.",
  title="Sudski tumač za njemački jezik | Sead Crnovršanin",
  desc="Sudski tumač za njemački jezik u Crnoj Gori. Ovjereni prevodi dokumenata na njemački i sa njemačkog. Preuzimanje u Podgorici, Baru, Bijelom Polju i Rožajama.",
  og_locale="sr_ME",
  h1="Sudski tumač za njemački jezik",
  trust="Imenovan rješenjem ministra pravde Crne Gore (2022)",
  lead="Ovjereni prevodi dokumenata sa njemačkog i na njemački jezik.",
  places_short="Preuzimanje po dogovoru u Podgorici, Baru, Bijelom Polju i Rožajama",
  actions_title="Pozovite ili pošaljite poruku",
  mail_line="ili pišite na",
  mail_subject="Upit%20za%20prevod",
  services_h="Šta prevodim",
  services_p="Sa njemačkog na crnogorski, bosanski i srpski jezik i obratno. Cijena i rok dogovaraju se na upit.",
  services=[
   ("id","Lična dokumenta","Izvodi iz matičnih knjiga, uvjerenja i lična dokumentacija.",None),
   ("cap","Diplome i svjedočanstva","Diplome, svjedočanstva i potvrde o obrazovanju.",None),
   ("car","Saobraćajna dozvola i dokumenta za auto","Njemačka saobraćajna dozvola, dokumentacija za uvoz i prateće isprave.","Šta poslati za ponudu"),
   ("contract","Ugovori i pravna dokumenta","Ugovori, ovlašćenja, sudski i upravni dokumenti.",None),
   ("briefcase","Poslovna i medicinska dokumenta","Dokumentacija za firme i institucije, medicinski izvještaji i nalazi.",None),
  ],
  certified=("Ovjereni prevodi","Prevodi sa ovjerom sudskog tumača, kada je to potrebno. Navedite to prilikom upita."),
  steps_h="Kako do prevoda",
  steps=[("Pošaljite upit","Pozovite ili pišite: koji dokument, na koji jezik, do kada i da li je potrebna ovjera."),
         ("Dogovorimo detalje","Dobijate povratnu informaciju o cijeni, vremenu izrade i preuzimanju."),
         ("Preuzmite prevod","Prevod preuzimate prema dogovoru ili putem dostave, gdje je to moguće.")],
  about_h="O meni",
  about=['<strong>Sead Crnovršanin</strong> je diplomirani ekonomista i sudski tumač za njemački jezik, imenovan rješenjem ministra pravde Crne Gore broj <span class="nowrap">UPI-05-109/22-1418-1</span> od 26.12.2022.',
         'U svom radu usmjeren je na precizno prevođenje dokumentacije sa njemačkog i na njemački jezik, uz pažnju prema terminologiji, namjeni dokumenta i dogovorenim rokovima.'],
  source='Podaci o imenovanju i pružaocu usluge: <a href="/me/impressum.html">Impressum</a>',
  quote="Svaka riječ. Na svom mjestu.",
  delivery_h="Preuzimanje i dostava",
  cities=["Podgorica","Bar","Bijelo Polje","Rožaje"],
  delivery_p="Moguće je dogovoriti preuzimanje u navedenim gradovima, kao i kurirsku dostavu širom Crne Gore. Tačan način i vrijeme preuzimanja potvrđuju se prilikom dogovora.",
  faq_h="Česta pitanja",
  faq=[("Kako mogu zatražiti ponudu?","Pošaljite upit e-mailom ili telefonom, uz informaciju koji dokument treba prevesti, na koji jezik i u kom roku. Nemojte slati osjetljiva dokumenta bez potrebe."),
       ("Da li je moguća ovjera prevoda?","Za dokumenta kojima je potrebna ovjera sudskog tumača, naznačite tu potrebu prilikom upita kako biste dobili odgovarajuće informacije."),
       ("Od čega zavise cijena i rok?","Od vrste dokumenta, obima, složenosti, zahtjeva za ovjeru i dogovorenog roka. Tačne uslove dobijate po slanju upita."),
       ("Kako preuzimam gotov prevod?","Način preuzimanja, uključujući dostupne lokacije ili kurirsku dostavu, dogovarate direktno prije izrade.")],
  contact_h="Kontakt",
  contact_p="Pošaljite dokument i željeni rok. Dobićete informacije o prevodu, cijeni i načinu preuzimanja.",
  c_call="Pozovite", c_viber="Pošaljite Viber poruku", c_wa="Pišite na WhatsApp", c_mail="Pošaljite e-mail",
  viber_help="Viber ne otvara kontakt?", copy="Kopiraj broj", copied="Broj kopiran", manual="Kopirajte broj i pronađite kontakt u Viberu.",
  privacy_note="Sajt ne prikuplja niti čuva dokumente. Za upite koristite direktno e-mail ili aplikaciju za poruke.",
  legal=[("impressum.html","Impressum"),("datenschutz.html","Politika privatnosti")], settings="Podešavanja privatnosti",
  dock_label="Brzi kontakt",
  v=dict(
   title="Prevod saobraćajne dozvole i dokumenata za vozila | Sudski tumač",
   desc="Prevod saobraćajne dozvole i dokumentacije za automobil sa njemačkog i na njemački. Po potrebi ovjera sudskog tumača. Upit i ponuda: Sead Crnovršanin, Podgorica.",
   crumb="Dokumenta za vozila",
   h1="Prevod saobraćajne dozvole i dokumenata za vozila",
   lead="Kupujete ili prodajete vozilo, ili pripremate dokumentaciju za postupak u Crnoj Gori ili Njemačkoj? Sead Crnovršanin prevodi dokumenta za vozila sa njemačkog na crnogorski, bosanski i srpski jezik i obratno. Kada je potrebno, možete zatražiti i prevod sa ovjerom sudskog tumača.",
   mail_subject="Prevod%20saobra%C4%87ajne%20dozvole%20i%20dokumentacije%20za%20vozila",
   docs_h="Koja dokumenta možete poslati na provjeru?",
   docs_p="Najprije javite o kakvom dokumentu se radi i za koju instituciju je namijenjen. Česti upiti uključuju:",
   docs=["Saobraćajnu dozvolu i potvrdu o registraciji vozila.","Njemačku dokumentaciju o registraciji — Zulassungsbescheinigung Teil I ili Teil II (Fahrzeugschein / Fahrzeugbrief).","Kupoprodajni ugovor, račun i druga prateća dokumenta, kada je njihov prevod potreban."],
   how_h="Kako dobiti ponudu i dogovoriti prevod?",
   how=["Navedite sa kog jezika i na koji jezik treba prevod, koju vrstu dokumenta imate i gdje ćete ga koristiti.","Pošaljite čitljiv prikaz dokumenta samo ako je potreban za procjenu. Za saobraćajnu dozvolu mogu biti relevantne obje strane.","Navedite rok i da li nadležna institucija traži ovjeru. Dobićete informaciju o cijeni, roku i načinu preuzimanja."],
   cert_h="Da li je uvijek potrebna ovjera?",
   cert_p="Ne nužno. Zahtjevi zavise od postupka i ustanove kojoj predajete dokumentaciju. Prije naručivanja provjerite kod primaoca šta tačno prihvata: običan ili ovjeren prevod, original ili kopiju. Sudski tumač može prevesti i ovjeriti prevod u okviru svog ovlašćenja, ali ne odlučuje o prihvatanju dokumenta od strane institucije.",
   del_h="Preuzimanje i dostava",
   del_p="Preuzimanje je moguće dogovoriti u Podgorici, Baru, Bijelom Polju i Rožajama, uz mogućnost kurirske dostave širom Crne Gore. Detalji se potvrđuju prije izrade.",
   related="Sva dokumenta koja prevodim",
   contact_h="Pošaljite upit za dokumentaciju vozila",
   contact_p="Napišite vrstu dokumenta, jezički pravac, namjenu, potrebu za ovjerom i željeni rok. Cijena i termin potvrđuju se nakon uvida u zahtjev.",
   manual="Kopirajte broj i pronađite kontakt u Viberu.",
   service_name="Prevod saobraćajne dozvole i dokumentacije za vozila",
   job="Sworn German-language translator",
  ),
 ),
 "de": dict(
  skip="Zum Inhalt springen", menu="Menü", menu_open="Menü öffnen", lang_label="Sprache wählen",
  role="Gerichts­dolmetscher für Deutsch", home="Startseite",
  nav=[("usluge","Leistungen"),("proces","Ablauf"),("o-meni","Über mich"),("dostava","Abholung"),("pitanja","Fragen"),("kontakt","Kontakt")],
  call="Anrufen", stamp="GERICHTSDOLMETSCHER FÜR DEUTSCH  ·  MONTENEGRO  ·  ",
  wa="https://wa.me/38267998199?text=Guten%20Tag%2C%20ich%20m%C3%B6chte%20eine%20%C3%9Cbersetzung%20anfragen.",
  title="Beglaubigte Übersetzungen Deutsch | Sead Crnovršanin",
  desc="Beglaubigte Übersetzungen Deutsch–Montenegrinisch in Montenegro. Dokumente, Urkunden und Zeugnisse. Abholung in Podgorica, Bar, Bijelo Polje und Rožaje.",
  og_locale="de_DE",
  h1="Gerichts­dolmetscher für Deutsch",
  trust="Bestellt durch Bescheid des Justizministers von Montenegro (2022)",
  lead="Beglaubigte Übersetzungen von Dokumenten aus dem Deutschen und ins Deutsche.",
  places_short="Abholung nach Vereinbarung in Podgorica, Bar, Bijelo Polje und Rožaje",
  actions_title="Anrufen oder Nachricht senden",
  mail_line="oder per E-Mail an",
  mail_subject="Anfrage%20zur%20%C3%9Cbersetzung",
  services_h="Was ich übersetze",
  services_p="Aus dem Deutschen ins Montenegrinische, Bosnische und Serbische und umgekehrt. Preis und Frist auf Anfrage.",
  services=[
   ("id","Persönliche Dokumente","Personenstandsurkunden, Bescheinigungen und persönliche Unterlagen.",None),
   ("cap","Zeugnisse und Diplome","Diplome, Zeugnisse und Ausbildungsnachweise.",None),
   ("car","Fahrzeugschein und Kfz-Dokumente","Deutsche Zulassungsdokumente, Kaufverträge und weitere Fahrzeugunterlagen.","Was für ein Angebot nötig ist"),
   ("contract","Verträge und Rechtsdokumente","Verträge, Vollmachten sowie Gerichts- und Verwaltungsunterlagen.",None),
   ("briefcase","Geschäftliche und medizinische Unterlagen","Unterlagen für Unternehmen und Institutionen, Befunde und Berichte.",None),
  ],
  certified=("Beglaubigte Übersetzungen","Übersetzungen mit Beglaubigung durch einen ermächtigten Übersetzer, sofern erforderlich. Bitte bei der Anfrage angeben."),
  steps_h="In drei Schritten zur Übersetzung",
  steps=[("Anfrage senden","Rufen Sie an oder schreiben Sie: welches Dokument, welche Sprachrichtung, welche Frist und ob eine Beglaubigung nötig ist."),
         ("Details abstimmen","Sie erhalten Informationen zu Preis, Bearbeitungszeit und Abholung."),
         ("Übersetzung erhalten","Sie erhalten Ihre Übersetzung nach Vereinbarung oder per Versand, sofern möglich.")],
  about_h="Über mich",
  about=['<strong>Sead Crnovršanin</strong> ist Diplom-Ökonom und Gerichtsdolmetscher für Deutsch, bestellt durch Bescheid des Justizministers von Montenegro Nr. <span class="nowrap">UPI-05-109/22-1418-1</span> vom 26.12.2022.',
         'Sein Schwerpunkt liegt auf präzisen Dokumentenübersetzungen aus dem Deutschen und ins Deutsche, mit besonderer Sorgfalt bei Terminologie, Verwendungszweck und vereinbarten Fristen.'],
  source='Angaben zur Bestellung und zum Anbieter: <a href="/de/impressum.html">Impressum</a>',
  quote="Jedes Wort. Am richtigen Platz.",
  delivery_h="Abholung und Versand",
  cities=["Podgorica","Bar","Bijelo Polje","Rožaje"],
  delivery_p="Die Abholung kann in den genannten Städten vereinbart werden. Ein Kurierdienst innerhalb Montenegros ist ebenfalls möglich. Ort und Zeitpunkt werden individuell abgestimmt.",
  faq_h="Häufige Fragen",
  faq=[("Wie erhalte ich ein Angebot?","Kontaktieren Sie uns per E-Mail oder Telefon und teilen Sie uns Dokumentenart, Sprachrichtung und gewünschte Frist mit. Senden Sie sensible Unterlagen nur, wenn dies erforderlich ist."),
       ("Sind beglaubigte Übersetzungen möglich?","Wenn Sie eine beglaubigte Übersetzung benötigen, geben Sie dies bei Ihrer Anfrage an, damit die Anforderungen geklärt werden können."),
       ("Wovon hängen Preis und Dauer ab?","Von Art, Umfang und Schwierigkeit des Dokuments sowie Beglaubigung und gewünschter Frist. Konkrete Konditionen erhalten Sie auf Anfrage."),
       ("Wie erhalte ich meine Übersetzung?","Abholort oder Kurierzustellung werden vor der Bearbeitung individuell vereinbart.")],
  contact_h="Kontakt",
  contact_p="Beschreiben Sie Ihr Dokument und den gewünschten Termin. Sie erhalten Informationen zu Übersetzung, Preis und Abholung.",
  c_call="Anrufen", c_viber="Viber-Nachricht senden", c_wa="WhatsApp-Nachricht senden", c_mail="E-Mail schreiben",
  viber_help="Viber öffnet den Kontakt nicht?", copy="Nummer kopieren", copied="Nummer kopiert", manual="Nummer kopieren und den Kontakt in Viber suchen.",
  privacy_note="Diese Website speichert keine Dokumente. Für Anfragen nutzen Sie bitte E-Mail oder einen Messenger.",
  legal=[("impressum.html","Impressum"),("datenschutz.html","Datenschutzhinweise")], settings="Datenschutzeinstellungen",
  dock_label="Schnellkontakt",
  v=dict(
   title="Fahrzeugschein übersetzen | Beglaubigte Kfz-Übersetzung Montenegro",
   desc="Übersetzung von Fahrzeugschein, Fahrzeugbrief und Kfz-Unterlagen Deutsch–Montenegrinisch. Bei Bedarf beglaubigt. Sead Crnovršanin, Podgorica.",
   crumb="Fahrzeugdokumente",
   h1="Fahrzeugschein und Fahrzeugdokumente übersetzen",
   lead="Sie benötigen eine Übersetzung für ein Fahrzeuggeschäft oder ein behördliches Verfahren in Montenegro oder Deutschland? Sead Crnovršanin übersetzt Fahrzeugunterlagen aus dem Deutschen ins Montenegrinische, Bosnische oder Serbische und umgekehrt. Wenn erforderlich, kann eine beglaubigte Übersetzung angefragt werden.",
   mail_subject="%C3%9Cbersetzung%20von%20Fahrzeugschein%20und%20Fahrzeugdokumenten",
   docs_h="Welche Unterlagen können Sie anfragen?",
   docs_p="Teilen Sie bitte mit, um welche Dokumente es geht und bei welcher Stelle Sie diese vorlegen möchten. Häufige Beispiele:",
   docs=["Fahrzeugschein und sonstige Zulassungs- oder Registrierungsdokumente.","Zulassungsbescheinigung Teil I und Teil II (Fahrzeugschein / Fahrzeugbrief).","Kaufvertrag, Rechnung oder weitere Fahrzeugunterlagen, sofern deren Übersetzung erforderlich ist."],
   how_h="Wie erhalten Sie ein Angebot?",
   how=["Nennen Sie Ausgangs- und Zielsprache, Art des Dokuments und den Verwendungszweck.","Schicken Sie gut lesbare Unterlagen nur, wenn diese für eine Einschätzung benötigt werden. Bei Zulassungsdokumenten können beide Seiten relevant sein.","Geben Sie Frist und gegebenenfalls die Anforderung einer Beglaubigung an. Preis, Bearbeitungszeit und Übergabe werden individuell vereinbart."],
   cert_h="Ist eine Beglaubigung immer erforderlich?",
   cert_p="Nicht unbedingt. Die Anforderungen unterscheiden sich je nach Verfahren und empfangender Behörde. Klären Sie bitte vorab, ob eine einfache oder beglaubigte Übersetzung benötigt wird und ob Originale oder Kopien vorzulegen sind. Der Übersetzer kann die Übersetzung im Rahmen seiner Befugnis beglaubigen, entscheidet aber nicht über die Anerkennung durch die Behörde.",
   del_h="Abholung und Versand",
   del_p="Abholung nach Vereinbarung in Podgorica, Bar, Bijelo Polje und Rožaje. Kurierzustellung innerhalb Montenegros ist nach Absprache möglich. Einzelheiten werden vor Auftragserteilung bestätigt.",
   related="Alle Dokumente, die ich übersetze",
   contact_h="Anfrage zu Fahrzeugdokumenten senden",
   contact_p="Nennen Sie Dokumentenart, Sprachrichtung, Verwendungszweck, Beglaubigungsbedarf und Frist. Sie erhalten anschließend ein individuelles Angebot.",
   manual="Kopieren Sie die Nummer und suchen Sie den Kontakt in Viber.",
   service_name="Übersetzung von Fahrzeugschein und Fahrzeugdokumenten",
   job="Sworn German-language translator",
  ),
 ),
}

# ---------------------------------------------------------------- carried-over content
def read(path):
    return path.read_text(encoding="utf-8")

def existing_consent(path):
    m = re.search(r'<div class="privacy-consent"[^>]*>.*?<div class="privacy-actions">.*?</div></div>', read(path), re.S)
    if not m:
        raise SystemExit(f"Consent block not found in {path}")
    block = m.group(0).replace(' lang="me"', ' lang="sr-Latn-ME"')
    if 'role="region"' not in block:
        block = block.replace("data-privacy-consent", 'data-privacy-consent role="region"', 1)
    return block

def existing_legal(path):
    s = read(path)
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    main = re.search(r"<main[^>]*>(.*?)</main>", s, re.S).group(1).strip()
    if 'class="legal-draft"' in main:
        raise SystemExit(f"{path} contains a legal draft banner; refusing to rebuild")
    return title, main

# ---------------------------------------------------------------- shared fragments
def alternates(lang, slug):
    url = lambda l: f"{BASE}/{l}/{slug}"
    out = [f'<link rel="canonical" href="{url(lang)}">']
    for l in ("me", "de"):
        out.append(f'<link rel="alternate" hreflang="{HREFLANG[l]}" href="{url(l)}">')
    out.append(f'<link rel="alternate" hreflang="x-default" href="{url("me")}">')
    return "\n".join(out)

def head(lang, title, desc, slug, robots, jsonld=None, og=True):
    c = C[lang]
    parts = [
        "<!doctype html>",
        f'<html lang="{HREFLANG[lang]}">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
        '<meta name="theme-color" content="#14293f">',
        '<meta name="format-detection" content="telephone=no">',
        f"<title>{title}</title>",
    ]
    if desc:
        parts.append(f'<meta name="description" content="{html.escape(desc, quote=True)}">')
    parts.append(f'<meta name="robots" content="{robots}">')
    if robots.startswith("index"):
        parts.append(alternates(lang, slug))
    if og:
        parts += [
            '<meta property="og:type" content="website">',
            '<meta property="og:site_name" content="Sead Crnovršanin">',
            f'<meta property="og:title" content="{html.escape(title, quote=True)}">',
            f'<meta property="og:description" content="{html.escape(desc, quote=True)}">',
            f'<meta property="og:url" content="{BASE}/{lang}/{slug}">',
            f'<meta property="og:locale" content="{c["og_locale"]}">',
            '<meta name="twitter:card" content="summary">',
        ]
    parts += [
        '<link rel="icon" type="image/svg+xml" href="/favicon.svg">',
        '<link rel="preload" href="/assets/fonts/manrope-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>',
        '<link rel="preload" href="/assets/fonts/cormorant-garamond-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>',
        f'<link rel="stylesheet" href="/assets/site.css?v={ASSET_V}">',
        "<script>document.documentElement.className+=' js'</script>",
    ]
    if jsonld:
        parts.append('<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False, separators=(",", ":")) + "</script>")
    parts.append("</head>")
    return "\n".join(parts)

def header(lang, slug, on_home):
    c = C[lang]
    other = "de" if lang == "me" else "me"
    prefix = "" if on_home else f"/{lang}/"
    lang_items = []
    for l in ("me", "de"):
        cur = ' aria-current="page"' if l == lang else ""
        lang_items.append(f'<li><a href="/{l}/{slug}" hreflang="{HREFLANG[l]}" lang="{HREFLANG[l]}"{cur}>{l.upper()}</a></li>')
    nav = "".join(f'<a href="{prefix}#{i}">{t}</a>' for i, t in c["nav"])
    return f'''<a class="skip-link" href="#main">{c["skip"]}</a>
<div class="topbar"><div class="wrap">
<div class="topbar-left"><a class="topbar-phone" href="{PHONE_HREF}" data-contact="phone">{icon("phone")}<span>{PHONE}</span></a><a class="topbar-mail" href="mailto:{MAIL}" data-contact="email">{icon("mail")}<span>{MAIL}</span></a></div>
<nav aria-label="{c["lang_label"]}"><ul class="lang">{"".join(lang_items)}</ul></nav>
</div></div>
<header class="masthead"><div class="wrap">
<a class="brand" href="/{lang}/"><span class="brand-seal" aria-hidden="true">SC</span><span class="brand-text"><span class="brand-name">Sead Crnovršanin</span><span class="brand-role">{c["role"]}</span></span></a>
<button class="nav-toggle" type="button" aria-controls="nav" aria-expanded="false" aria-label="{c["menu_open"]}">{icon("menu","icon icon-open")}{icon("close","icon icon-close")}<span class="nav-toggle-label">{c["menu"]}</span></button>
<nav id="nav" class="site-nav" aria-label="{c["menu"]}">{nav}<a class="btn btn-call nav-call" href="{PHONE_HREF}" data-contact="phone">{icon("phone")}{c["call"]} {PHONE}</a></nav>
<a class="btn btn-call header-call" href="{PHONE_HREF}" data-contact="phone">{icon("phone")}{c["call"]}</a>
</div></header>'''

def hero_actions(lang, mail_subject, extra_attr=""):
    c = C[lang]
    return f'''<div class="hero-actions" data-dock-after data-title="{c["actions_title"]}"{extra_attr}>
<a class="btn btn-call" href="{PHONE_HREF}" data-contact="phone">{icon("phone")}<span>{c["call"]} <span class="btn-number">{PHONE}</span></span></a>
<a class="btn btn-ghost" href="{VIBER_HREF}" data-contact="viber" aria-label="{c["c_viber"]}"><span class="brand-dot viber">{icon("viber")}</span>Viber</a>
<a class="btn btn-ghost" href="{c["wa"]}" data-contact="whatsapp" target="_blank" rel="noopener noreferrer" aria-label="{c["c_wa"]}"><span class="brand-dot whatsapp">{icon("whatsapp")}</span>WhatsApp</a>
<a class="hero-mail" href="mailto:{MAIL}?subject={mail_subject}" data-contact="email">{icon("mail")}<span>{c["mail_line"]} {MAIL}</span></a>
</div>'''

def contact_section(lang, heading, text, mail_subject, manual):
    c = C[lang]
    return f'''<section class="section contact" id="kontakt" aria-labelledby="kontakt-h"><div class="wrap">
<div class="section-head"><h2 id="kontakt-h">{heading}</h2><p>{text}</p></div>
<div>
<div class="contact-list">
<a class="contact-card primary" href="{PHONE_HREF}" data-contact="phone"><span class="card-icon">{icon("phone")}</span><span class="card-text"><span class="card-action">{c["c_call"]}</span><span class="card-value">{PHONE}</span></span></a>
<a class="contact-card" href="{VIBER_HREF}" data-contact="viber"><span class="brand-dot viber">{icon("viber")}</span><span class="card-text"><span class="card-action">{c["c_viber"]}</span><span class="card-value">{PHONE}</span></span></a>
<a class="contact-card" href="{c["wa"]}" data-contact="whatsapp" target="_blank" rel="noopener noreferrer"><span class="brand-dot whatsapp">{icon("whatsapp")}</span><span class="card-text"><span class="card-action">{c["c_wa"]}</span><span class="card-value">{PHONE}</span></span></a>
<a class="contact-card" href="mailto:{MAIL}?subject={mail_subject}" data-contact="email"><span class="card-icon soft">{icon("mail")}</span><span class="card-text"><span class="card-action">{c["c_mail"]}</span><span class="card-value">{MAIL}</span></span></a>
</div>
<p class="viber-help"><span>{c["viber_help"]}</span><button type="button" class="viber-copy-button" data-copied="{c["copied"]}" data-manual="{manual}">{c["copy"]}</button><span class="viber-copy-feedback" role="status" aria-live="polite"></span></p>
<p class="contact-privacy">{c["privacy_note"]}</p>
</div>
</div></section>'''

def dock(lang):
    c = C[lang]
    return f'''<nav class="dock" data-dock aria-label="{c["dock_label"]}" aria-hidden="true" inert>
<a class="dock-call" href="{PHONE_HREF}" data-contact="phone">{icon("phone")}{c["call"]}</a>
<a href="{VIBER_HREF}" data-contact="viber" aria-label="{c["c_viber"]}"><span class="brand-dot viber">{icon("viber")}</span>Viber</a>
<a href="{c["wa"]}" data-contact="whatsapp" target="_blank" rel="noopener noreferrer" aria-label="{c["c_wa"]}"><span class="brand-dot whatsapp">{icon("whatsapp")}</span>WhatsApp</a>
</nav>'''

def footer(lang):
    c = C[lang]
    legal = "".join(f'<li><a href="/{lang}/{f}">{t}</a></li>' for f, t in c["legal"])
    return f'''<footer class="site-footer"><div class="wrap">
<div class="footer-brand">Sead Crnovršanin<span>{c["role"]}</span></div>
<ul class="footer-contact"><li><a href="{PHONE_HREF}" data-contact="phone">{PHONE}</a></li><li><a href="mailto:{MAIL}" data-contact="email">{MAIL}</a></li></ul>
<ul class="footer-legal">{legal}<li><a href="#" data-privacy-settings>{c["settings"]}</a></li></ul>
<p class="footer-copy">© <span id="year">2026</span> Sead Crnovršanin</p>
</div></footer>'''

def tail(consent):
    return f'{consent}\n<script defer src="/assets/site.js?v={ASSET_V}"></script>\n</body>\n</html>\n'

# ---------------------------------------------------------------- pages
def home(lang):
    c = C[lang]
    url = f"{BASE}/{lang}/"
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": f"{BASE}/#website", "url": f"{BASE}/", "name": "Sead Crnovršanin | German Translations", "inLanguage": ["sr-Latn-ME", "de"]},
        {"@type": "Person", "@id": f"{BASE}/#translator", "name": "Sead Crnovršanin", "jobTitle": c["role"].replace("\u00ad", ""), "telephone": "+38267998199", "email": MAIL, "url": url},
        {"@type": "Service", "@id": f"{url}#service", "name": c["title"].split(" | ")[0], "description": c["lead"], "provider": {"@id": f"{BASE}/#translator"}, "areaServed": {"@type": "Country", "name": "Montenegro"}, "availableLanguage": ["German", "Montenegrin"]},
        {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": c["title"], "description": c["desc"], "inLanguage": HREFLANG[lang], "isPartOf": {"@id": f"{BASE}/#website"}, "about": {"@id": f"{url}#service"}},
    ]}
    path = ROOT / lang / "index.html"
    consent = existing_consent(path)
    vehicle = f"/{lang}/prevod-saobracajne-dozvole.html"
    services = []
    for ic, t, d, link in c["services"]:
        more = f'<a class="service-link" href="{vehicle}">{link}{icon("chevron")}</a>' if link else ""
        services.append(f'<li class="service"><span class="service-icon">{icon(ic)}</span><div class="service-body"><h3>{t}</h3><p>{d}</p>{more}</div></li>')
    ct, cd = c["certified"]
    services.append(f'<li class="service service-certified"><span class="service-icon">{icon("stamp")}</span><div class="service-body"><h3>{ct}</h3><p>{cd}</p></div></li>')
    steps = "".join(f'<li class="step"><h3>{t}</h3><p>{d}</p></li>' for t, d in c["steps"])
    faq = "".join(f'<details><summary>{q}{icon("plus")}</summary><p>{a}</p></details>' for q, a in c["faq"])
    cities = "".join(f'<li>{icon("pin")}{x}</li>' for x in c["cities"])
    about = "".join(f"<p>{p}</p>" for p in c["about"])
    body = f'''<body>
{header(lang, "", True)}
<main id="main">
<section class="hero" aria-labelledby="hero-h"><div class="wrap">
<div class="hero-stamp">{stamp(c["stamp"], "stamp-hero")}</div>
<div class="hero-text">
<p class="hero-name">{icon("stamp")}<span>{c["trust"]}</span></p>
<h1 id="hero-h">{c["h1"]}</h1>
<p class="hero-lead">{c["lead"]}</p>
<p class="hero-places">{icon("pin")}<span>{c["places_short"]}</span></p>
</div>
{hero_actions(lang, c["mail_subject"])}
</div></section>
<section class="section" id="usluge" aria-labelledby="usluge-h"><div class="wrap">
<div class="section-head"><h2 id="usluge-h">{c["services_h"]}</h2><p>{c["services_p"]}</p></div>
<ul class="services">{"".join(services)}</ul>
</div></section>
<section class="section section-alt" id="proces" aria-labelledby="proces-h"><div class="wrap">
<div class="section-head"><h2 id="proces-h">{c["steps_h"]}</h2></div>
<ol class="steps">{steps}</ol>
</div></section>
<section class="section" id="o-meni" aria-labelledby="o-meni-h"><div class="wrap about">
<div class="about-seal">{stamp(c["stamp"], "stamp-about")}</div>
<div class="about-copy"><h2 id="o-meni-h">{c["about_h"]}</h2>{about}<p class="source-note">{c["source"]}</p><blockquote class="about-quote" lang="{HREFLANG[lang]}">{c["quote"]}</blockquote></div>
</div></section>
<section class="section section-alt" id="dostava" aria-labelledby="dostava-h"><div class="wrap">
<div class="section-head"><h2 id="dostava-h">{c["delivery_h"]}</h2></div>
<ul class="places">{cities}</ul>
<p class="delivery-text">{c["delivery_p"]}</p>
</div></section>
<section class="section" id="pitanja" aria-labelledby="pitanja-h"><div class="wrap">
<div class="section-head"><h2 id="pitanja-h">{c["faq_h"]}</h2></div>
<div class="faq">{faq}</div>
</div></section>
{contact_section(lang, c["contact_h"], c["contact_p"], c["mail_subject"], c["manual"])}
</main>
{footer(lang)}
{dock(lang)}
'''
    path.write_text(head(lang, c["title"], c["desc"], "", "index,follow,max-image-preview:large", jsonld) + "\n" + body + tail(consent), encoding="utf-8")

def vehicle(lang):
    c = C[lang]; v = c["v"]
    slug = "prevod-saobracajne-dozvole.html"
    url = f"{BASE}/{lang}/{slug}"
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": v["title"], "description": v["desc"], "inLanguage": HREFLANG[lang], "isPartOf": {"@id": f"{BASE}/#website"}},
        {"@type": "Service", "@id": f"{url}#service", "name": v["service_name"], "serviceType": "Translation of vehicle registration documents",
         "provider": {"@type": "Person", "name": "Sead Crnovršanin", "jobTitle": v["job"], "telephone": "+38267998199"},
         "areaServed": {"@type": "Country", "name": "Montenegro"}, "availableLanguage": ["German", "Montenegrin", "Bosnian", "Serbian"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": c["home"], "item": f"{BASE}/{lang}/"},
            {"@type": "ListItem", "position": 2, "name": v["service_name"], "item": url}]},
    ]}
    path = ROOT / lang / slug
    consent = existing_consent(path)
    docs = "".join(f"<li>{d}</li>" for d in v["docs"])
    how = "".join(f"<li>{d}</li>" for d in v["how"])
    body = f'''<body class="detail-page">
{header(lang, slug, False)}
<main id="main">
<section class="page-hero" aria-labelledby="page-h"><div class="wrap">
<ol class="breadcrumb"><li><a href="/{lang}/">{c["home"]}</a></li><li aria-current="page">{v["crumb"]}</li></ol>
<h1 id="page-h">{v["h1"]}</h1>
<p class="hero-lead">{v["lead"]}</p>
{hero_actions(lang, v["mail_subject"])}
</div></section>
<div class="wrap detail">
<section class="detail-block"><h2>{v["docs_h"]}</h2><p>{v["docs_p"]}</p><ul class="check-list">{docs}</ul></section>
<section class="detail-block"><h2>{v["how_h"]}</h2><ol class="detail-steps">{how}</ol></section>
<section class="detail-block"><h2>{v["cert_h"]}</h2><p>{v["cert_p"]}</p></section>
<section class="detail-block"><h2>{v["del_h"]}</h2><p>{v["del_p"]}</p></section>
<a class="related detail-block wide" href="/{lang}/#usluge">{v["related"]}{icon("chevron")}</a>
</div>
{contact_section(lang, v["contact_h"], v["contact_p"], v["mail_subject"], v["manual"])}
</main>
{footer(lang)}
{dock(lang)}
'''
    path.write_text(head(lang, v["title"], v["desc"], slug, "index,follow,max-image-preview:large", jsonld) + "\n" + body + tail(consent), encoding="utf-8")

def legal(lang, slug):
    path = ROOT / lang / slug
    title, main = existing_legal(path)
    consent = existing_consent(path)
    body = f'''<body class="legal-page">
{header(lang, slug, False)}
<main class="legal-main" id="main">
{main}
</main>
{footer(lang)}
'''
    path.write_text(head(lang, title, None, slug, "noindex,follow", og=False) + "\n" + body + tail(consent), encoding="utf-8")

def not_found():
    """/404.html — served for missing pages and for the retired /en/ URLs (HTTP 410 on ALL-INKL)."""
    page = f'''<!doctype html>
<html lang="sr-Latn-ME">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#14293f">
<meta name="robots" content="noindex,follow">
<title>Stranica ne postoji · Seite nicht gefunden | Sead Crnovršanin</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/assets/site.css?v={ASSET_V}">
</head>
<body class="legal-page">
<header class="masthead"><div class="wrap">
<a class="brand" href="/me/"><span class="brand-seal" aria-hidden="true">SC</span><span class="brand-text"><span class="brand-name">Sead Crnovršanin</span><span class="brand-role">{C["me"]["role"]}</span></span></a>
</div></header>
<main class="legal-main" id="main">
<h1>Stranica ne postoji</h1>
<p class="legal-intro">Tražena stranica je uklonjena ili je adresa pogrešna.</p>
<p lang="de" class="legal-intro">Diese Seite existiert nicht mehr oder die Adresse ist falsch.</p>
<div class="hero-actions notfound-actions">
<a class="btn btn-ink" href="/me/" hreflang="sr-Latn-ME">Početna (ME)</a>
<a class="btn btn-light" href="/de/" hreflang="de" lang="de">Startseite (DE)</a>
<a class="btn btn-call" href="{PHONE_HREF}" data-contact="phone">{icon("phone")}<span>{C["me"]["call"]} <span class="btn-number">{PHONE}</span></span></a>
</div>
</main>
</body>
</html>
'''
    (ROOT / "404.html").write_text(page, encoding="utf-8")

if __name__ == "__main__":
    for lang in ("me", "de"):
        home(lang)
        vehicle(lang)
        legal(lang, "impressum.html")
        legal(lang, "datenschutz.html")
    not_found()
    print("Built /me and /de pages and /404.html.")
