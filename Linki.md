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
- Gdy trzeba zostawić techniczne oznaczenie problemu lub tymczasowy znacznik porządkowy w wikikodzie, najpierw sprawdź `Pomoc:Znaczniki`, zamiast zgadywać lokalną składnię.
- `archiwum=` musi prowadzić do prawdziwego archiwum (np. Wayback), nie do permalinku, share URL ani linku z parametrami śledzącymi.
- Dla artykułów z filozofii czasu nie używaj `[[Kategoria:Filozofia czasu]]`, bo jest czerwona; praktyczny zestaw startowy to `[[Kategoria:Filozofia czasu i przestrzeni]]`, a gdy zakres hasła tego wymaga, także `[[Kategoria:Czas]]`.
- Po zaciągnięciu live rawa z opublikowanej strony najpierw zachowaj ten stan jako checkpoint synchronizacji. Jeśli live rozwinęło nazwy przypisów do definicji w `<references>...</references>`, nie cofaj tego od razu automatycznie.
- Jeśli Adam po publikacji prosi już tylko o archiwa albo drobny cleanup, rozdziel to na dwa checkpointy: najpierw sync live raw + commit/push stanu zsynchronizowanego, dopiero potem właściwy pass archiwizacyjny lub porządkowy.
- Jeśli dla danego hasła repo zawiera `roadmap.md`, traktuj go jako aktywną instrukcję pracy i rób kolejne rundy bez pytania, dopóki są realne poprawki.
- W końcowym parser preview akceptowalne są tylko świadomie pozostawione czerwone linki z `{{link-interwiki}}`; każdy inny redlink wymaga poprawki albo odlinkowania.
- Gdy trzeba jawnie oznaczyć status dostępu źródła (`otwarty`, `zamknięty`, `częściowy`), najpierw sprawdź realną landing page albo działający full text, potem preferuj konwersję tego refu do `{{Cytuj}}` z `dostęp=`. `{{Otwarty dostęp}}` / `{{Paywall}}` zostaw jako fallback.
- Nie zakładaj, że mniej oczywiste pola z `Szablon:Cytuj` działają identycznie w `{{Cytuj pismo}}` i `{{Cytuj książkę}}`; pola takie jak `dostęp=` potwierdzaj parser preview exact draftu.
- Przy konwersji przypisu do `{{Cytuj}}` pamiętaj też o stronach: używaj `s=`, nie `strony=`. To częsty błąd i na plwiki potrafi kończyć się kategorią `Szablon cytuj do sprawdzenia`.
- Przy auth workflow Wayback nie zakładaj gotowości tylko dlatego, że istnieje `~/.venvs/savepagenow/bin/python` i w env są klucze. Przed większym retry sprawdź też wprost `python -c "import savepagenow"`; jeśli import nie działa albo endpointy dają tylko mieszankę `403` / `503` / `520`, traktuj brak wyniku jako brak potwierdzenia, nie jako dowód braku snapshotu.

## Linki do rozbudowy
- Pomoc:Ilustrowanie — składnia obrazków, podpisów, pozycjonowania i miniaturek
- Pomoc:Znaczniki — lokalne znaczniki i oznaczenia problemów, gdy trzeba coś otagować zamiast opisywać ręcznie.
- Szablon:Legenda — legenda kolorów w podpisach map i grafik
