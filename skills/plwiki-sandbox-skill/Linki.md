# Linki.md — polska Wikipedia, zasady i skróty robocze

Ten plik jest głównie dla agenta.

Cel:
- zbierać przydatne oficjalne strony plwiki dotyczące edytowania, szablonów, zasad i formatowania
- dopisywać krótkie zasady robocze wynikające z tych stron
- traktować to jako podręczny zbiór "przepisów polskiej Wikipedii" do stosowania przy kolejnych artykułach

Zasady użycia:
- preferuj linki do oficjalnych stron plwiki (pomoc, szablony, zasady, dokumentacje)
- przy linku dopisz krótko, po co jest ważny
- można dopisywać krótkie reguły tekstowe, jeśli wynikają z praktyki lub z oficjalnych stron
- jeśli Adam dopisze tu nowe wskazówki, traktuj je jako ważne dla dalszej pracy

## Potwierdzone reguły robocze
- Przy ilustracjach na plwiki preferuj `right|thumb`, nie `miniatura|prawo`, bo ta druga forma potrafi psuć rozpoznanie podpisu.
- `{{Legenda}}` może działać wewnątrz podpisu obrazka, jeśli składnia `[[Plik:...|right|thumb|...]]` jest poprawna.
- Przy przypisach sprawdzaj nie tylko format, ale też czy źródło naprawdę wspiera daną tezę lub tabelę.
- `archiwum=` musi prowadzić do prawdziwego archiwum (np. Wayback), nie do permalinku, share URL ani linku z parametrami śledzącymi.
- Przy preview-fixach pod refy nie łataj tego ręcznie w kółko: uruchamiaj `scripts/check_ref_punctuation.py <plik>` i poprawiaj wszystkie zgłoszone miejsca typu `LEAKED_CITE`, `EMPTY_NAMED_REF`, `MISSING_PERIOD_AFTER_REF` i `MISSING_PERIOD_AT_LINE_END_AFTER_REF`.
- Wayback / archive workflow: public `web.archive.org/save/...` i CDX z tego hosta potrafią zwracać `connection refused`, `429` i `520`, więc nie traktuj braku archiwum jako dowodu, że snapshot nie istnieje. Najpierw sprawdź CDX/Availability, wpisuj tylko potwierdzone `archiwum=` URL-e, a dla batch save preferuj prostego Pythona zamiast złożonych bashowych pętli.
- Internet Archive SavePageNow ma tryb z autoryzacją przez API credentials (`SAVEPAGENOW_ACCESS_KEY`, `SAVEPAGENOW_SECRET_KEY`). Jeśli Adam poda takie dane, warto używać auth flow / helpera zamiast gołych anonimowych requestów.
- Stan praktyczny z 2026-03-27: credentials były widoczne w env, ale ten host nie miał zainstalowanego wrappera `savepagenow` ani nawet `pip`, więc auth workflow początkowo zatrzymał się na braku lokalnego narzędzia. Rozwiązanie, które zadziałało: Adam utworzył venv (`~/.venvs/savepagenow`) i zainstalował tam `savepagenow`; potem auth batch przez `~/.venvs/savepagenow/bin/python` zaczął działać z tymi samymi env varami.
- Potwierdzony działający workflow Wayback dla plwiki: (1) wyciągnij z artykułu tylko refy bez `archiwum=`, (2) uruchom auth capture przez `savepagenow.capture_or_cache(..., authenticate=True)`, (3) zapisuj wyniki do JSON-a pomocniczego (np. `wayback-auth-results.json`), (4) wstawiaj do artykułu wyłącznie potwierdzone `archiwum=` i `zarchiwizowano=` na podstawie realnego archive URL, (5) commituj razem z artykułem. Na artykule Claude ta ścieżka dała 36 potwierdzonych archiwów w commicie `7617194`.
- Przy cytatach i odwołaniach do konkretnych miejsc Pisma Świętego na plwiki preferuj `{{Biblia}}` zamiast gołych linków do zewnętrznych serwisów biblijnych.
- `{{Odn}}` stosuj do skróconych odwołań; pełny opis dawaj zwykle w bibliografii z `|odn=tak`, a w tekście używaj `{{odn|Autor|Rok|s=...}}`.
- W artykułowym repo `akumiszcza/plwiki-sandbox` po każdej sensownej zmianie rób od razu `git add` + `git commit` + `git push`, bo praca toczy się równolegle na kilku komputerach.
- Przed każdym działaniem związanym z tłumaczeniem lub cleanupem wiki rób `git pull --ff-only` w `/home/ubuntu/.openclaw/plwiki-sandbox`.

## Potwierdzone reguły robocze
- Przy artykułach o oprogramowaniu na plwiki sprawdzaj najpierw dokumentację `{{Oprogramowanie infobox}}` na Wikibooks: `https://pl.wikibooks.org/wiki/Szablon:Oprogramowanie_infobox`. Używaj polskich nazw parametrów dokładnie jak w szablonie, np. `pierwsze wydanie`, `wersja stabilna`, `platforma sprzętowa`, `system operacyjny`, `język programowania`, `commons`, `www`.
- Nie przenoś bezmyślnie enwiki-owych lub innych wariantów typu `Infobox oprogramowanie` z podkreśleniami i obcymi nazwami pól; dla plwiki trzeba dopasować się do lokalnego szablonu i jego składni.

## Szablony
- https://pl.wikipedia.org/wiki/Szablon:Biblia - preferowany na plwiki do odwołań do konkretnych fragmentów Pisma Świętego.
- https://pl.wikipedia.org/wiki/Szablon:Odn - do skróconych odwołań; pełny opis zwykle w bibliografii z `|odn=tak`.
- https://pl.wikipedia.org/wiki/Szablon:Cytuj
- https://pl.wikipedia.org/wiki/Szablon:Cytuj_pismo
- https://pl.wikipedia.org/wiki/Szablon:Cytuj_książkę
- https://pl.wikipedia.org/wiki/Szablon:Cytuj_stronę
- https://pl.wikipedia.org/wiki/Szablon:Legenda - przydatny do legend i opisów w podpisach grafik.

## Zasady i pomoc
- https://pl.wikipedia.org/wiki/Wikipedia:Weryfikowalność
- https://pl.wikipedia.org/wiki/Wikipedia:Bibliografia
- https://pl.wikipedia.org/wiki/Pomoc:Przypisy
- https://pl.wikibooks.org/wiki/Szablon:Oprogramowanie_infobox - dokumentacja infoboksu oprogramowania.

## Linki do rozbudowy
- Pomoc:Ilustrowanie — składnia obrazków, podpisów, pozycjonowania i miniaturek
- Szablon:Legenda — legenda kolorów w podpisach map i grafik
- Szablon:Oprogramowanie infobox (Wikibooks) — dokumentacja infoboksu dla artykułów o programach komputerowych na plwiki
