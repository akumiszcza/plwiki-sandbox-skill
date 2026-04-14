# wiki-skill.md (skill copy)

Core reminder for this repo:

- `SAVEPAGENOW_ACCESS_KEY` i `SAVEPAGENOW_SECRET_KEY` służą do autoryzowanych zapisów w Wayback przez `savepagenow`.
- Preferuj workflow: najpierw zebrać URL-e bez `archiwum=`, potem `savepagenow.capture_or_cache(..., authenticate=True)`, potem dopisać `archiwum=` i `zarchiwizowano=`.
- Dodatkowe, lokalne operacyjne notatki prowadź też w `wiki-skill.md` w repo artykułów (`/home/ubuntu/.openclaw/plwiki-sandbox/wiki-skill.md`).
- Uwaga o `Cytuj książkę`: ten szablon nie obsługuje `archiwum` ani `zarchiwizowano`.
  Archiwalny URL wpisuję wprost jako `url=` i dodaję tylko `data dostępu=...`.
- Przy większych passach cytowań nie ufam samemu lokalnemu wrażeniu: przed pushem robię realny `action=parse` na dokładnym szkicu i traktuję wynik parsera plwiki jako ostateczną bramkę jakości.
- W praktyce dla importowanych cytowań z enwiki wracają trzy bezpieczne mapowania: w `{{Cytuj pismo}}` `tom -> wolumin`, dla pierwszego autora `imię1/nazwisko1 -> imię/nazwisko`, a redaktorów w `{{Cytuj książkę}}` zapisuję jako `inni=... (red.)`.
- Dla obcojęzycznych terminów w tekście używam poprawnej składni `Szablon:Ang`, czyli `{{ang.|...}}` z kropką. Błędne `{{ang|...}}` może w preview renderować się jak czerwony `Szablon:Ang`.
- Przy haśle o rosnącym bloku czasu utrwalam ostrożność merytoryczną w leadzie: nie sugeruję automatycznie, że growing block z definicji zakłada czterowymiarową ontologię czasoprzestrzeni; jeśli trzeba, doprecyzowuję to wprost i opieram na źródle typu SEP.
- Jeżeli Adam każe zachować wszystkie przypisy, nie rozwiązuję redakcji przez usuwanie istniejących refów, tylko przez poprawę treści, bibliografii i metadanych.
- Dla opisów zmian na plwiki przy tłumaczeniu i dokładaniu źródeł dobrze działa krótki styl rzeczownikowy, np. `enwiki + polskie źródła`; pomocniczy punkt odniesienia: `https://pl.wikipedia.org/wiki/Wikipedia:Opis_zmian`.
- Po publikacji live kolejny mikro-pass zaczynam od świeżego raw z live do lokalnego `PL.mediawiki`, nawet jeśli repo było przed chwilą zsynchronizowane.
