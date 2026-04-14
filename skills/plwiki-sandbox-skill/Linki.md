# Źródła dotyczące edytowania Wikipedii

## Szablony

- https://pl.wikipedia.org/wiki/Szablon:Legenda
- https://pl.wikipedia.org/wiki/Szablon:Biblia
- https://pl.wikipedia.org/wiki/Szablon:Odn
- https://meta.wikimedia.org/wiki/WMDE_Technical_Wishes/Sub-referencing/pl
- https://pl.wikipedia.org/wiki/Szablon:Cytuj
- `{{Biblia}}`: preferowany na plwiki do odwołań do konkretnych fragmentów Pisma Świętego.
- `{{Odn}}`: historycznie do skróconych odwołań; przy nowych pracach sprawdzaj, czy lepsze nie będą natywne podprzypisy Cite (`<ref name="..." details="..." />`), bo wzorzec `{{Odn}}` jest wycofywany tam, gdzie `details=` działa.
- https://pl.wikipedia.org/wiki/Szablon:Cytuj_pismo
- https://pl.wikipedia.org/wiki/Szablon:Cytuj_ksi%C4%85%C5%BCk%C4%99
- https://pl.wikipedia.org/wiki/Szablon:Cytuj_stron%C4%99
- https://pl.wikipedia.org/wiki/Szablon:Link-interwiki - do czytelnego linkowania odpowiedników w innych wiki/projektach, gdy zwykły link wewnętrzny nie wystarcza.
- https://pl.wikipedia.org/wiki/Wikipedia:Weryfikowalno%C5%9B%C4%87
- https://pl.wikipedia.org/wiki/Wikipedia:Bibliografia
- https://pl.wikipedia.org/wiki/Wikipedia:Opis_zmian - przydatne do krótkich, hasłowych, wiki-stylowych opisów edycji.
- https://pl.wikipedia.org/wiki/Pomoc:Przypisy
- https://pl.wikipedia.org/wiki/Pomoc:Znaczniki - przydatne, gdy trzeba oznaczyć fragment/problem lokalnym znacznikiem zamiast improwizować opis w tekście lub komentarzu.
- https://pl.wikibooks.org/wiki/Szablon:Oprogramowanie_infobox

## Reguły robocze


- Natywne podprzypisy Cite: pełne źródło definiuj raz w `<references>` jako `<ref name="ŹródłoRok">...</ref>`, w tekście używaj `<ref name="ŹródłoRok" />` bez numeru strony i `<ref name="ŹródłoRok" details="s. ..." />` dla miejsc szczegółowych. Nie duplikuj pełnej definicji tego samego `name` w treści.
- Gdy trzeba zostawić techniczne oznaczenie problemu lub tymczasowy znacznik porządkowy w wikikodzie, najpierw sprawdź `Pomoc:Znaczniki`, zamiast zgadywać lokalną składnię.
- Przy artykułach o oprogramowaniu na plwiki sprawdzaj najpierw dokumentację `{{Oprogramowanie infobox}}` na Wikibooks.
- Przy cytatach i odwołaniach do konkretnych miejsc Pisma Świętego na plwiki preferuj `{{Biblia}}` zamiast gołych linków do zewnętrznych serwisów biblijnych.
- W tym repo po każdej sensownej zmianie rób od razu `git add` + `git commit` + `git push`, bo praca toczy się równolegle na kilku komputerach.
- Używaj polskich nazw parametrów dokładnie jak w tym szablonie, np. `pierwsze wydanie`, `wersja stabilna`, `platforma sprzętowa`, `system operacyjny`, `język programowania`, `commons`, `www`.
- Nie przenoś bezmyślnie wariantów typu `Infobox oprogramowanie` z innymi nazwami pól; dla plwiki trzeba dopasować się do lokalnej składni.

- Wayback / archive workflow: public `web.archive.org/save/...` i CDX z tego hosta potrafią zwracać `connection refused`, `429` i `520`, więc nie traktuj braku archiwum jako dowodu, że snapshot nie istnieje. Najpierw sprawdź CDX/Availability, wpisuj tylko potwierdzone `archiwum=` URL-e, a dla batch save preferuj prostego Pythona zamiast złożonych bashowych pętli.
- Internet Archive SavePageNow ma tryb z autoryzacją przez API credentials (`SAVEPAGENOW_ACCESS_KEY`, `SAVEPAGENOW_SECRET_KEY`). Jeśli Adam poda takie dane, warto używać auth flow / helpera zamiast gołych anonimowych requestów.

- Internet Archive SavePageNow ma tryb z autoryzacją przez API credentials (`SAVEPAGENOW_ACCESS_KEY`, `SAVEPAGENOW_SECRET_KEY`). Jeśli Adam poda takie dane, warto używać auth flow / helpera zamiast gołych anonimowych requestów.
- Stan praktyczny z 2026-03-27: credentials były widoczne w env, ale ten host nie miał zainstalowanego wrappera `savepagenow` ani nawet `pip`, więc auth workflow początkowo zatrzymał się na braku lokalnego narzędzia. Rozwiązanie, które zadziałało: Adam utworzył venv (`~/.venvs/savepagenow`) i zainstalował tam `savepagenow`; potem auth batch przez `~/.venvs/savepagenow/bin/python` zaczął działać z tymi samymi env varami.
- Potwierdzony działający workflow Wayback dla plwiki: (1) wyciągnij z artykułu tylko refy bez `archiwum=`, (2) uruchom auth capture przez `savepagenow.capture_or_cache(..., authenticate=True)`, (3) zapisuj wyniki do JSON-a pomocniczego (np. `wayback-auth-results.json`), (4) wstawiaj do artykułu wyłącznie potwierdzone `archiwum=` i `zarchiwizowano=` na podstawie realnego archive URL, (5) commituj razem z artykułem. Na artykule Claude ta ścieżka dała 36 potwierdzonych archiwów w commicie `7617194`.
