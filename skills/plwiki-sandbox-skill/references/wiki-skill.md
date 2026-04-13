# wiki-skill.md (skill copy)

Core reminder for this repo:

- `SAVEPAGENOW_ACCESS_KEY` i `SAVEPAGENOW_SECRET_KEY` służą do autoryzowanych zapisów w Wayback przez `savepagenow`.
- Preferuj workflow: najpierw zebrać URL-e bez `archiwum=`, potem `savepagenow.capture_or_cache(..., authenticate=True)`, potem dopisać `archiwum=` i `zarchiwizowano=`.
- Dodatkowe, lokalne operacyjne notatki prowadź też w `wiki-skill.md` w repo artykułów (`/home/ubuntu/.openclaw/plwiki-sandbox/wiki-skill.md`).
- Uwaga o `Cytuj książkę`: ten szablon nie obsługuje `archiwum` ani `zarchiwizowano`.
  Archiwalny URL wpisuję wprost jako `url=` i dodaję tylko `data dostępu=...`.
- Przy większych passach cytowań nie ufam samemu lokalnemu wrażeniu: przed pushem robię realny `action=parse` na dokładnym szkicu i traktuję wynik parsera plwiki jako ostateczną bramkę jakości.
- W praktyce dla importowanych cytowań z enwiki wracają trzy bezpieczne mapowania: w `{{Cytuj pismo}}` `tom -> wolumin`, dla pierwszego autora `imię1/nazwisko1 -> imię/nazwisko`, a redaktorów w `{{Cytuj książkę}}` zapisuję jako `inni=... (red.)`.
