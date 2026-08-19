# Sprint 2 — Formularz i tymczasowa lista wydatków

## Cel

Pozwolić użytkownikowi dodać wydatek przez formularz i zobaczyć go na liście w działającej aplikacji.

## Ustalenia

- Waluta: polski złoty (zł).
- Kategorie: Jedzenie, Transport, Rachunki, Rozrywka, Zdrowie, Inne.
- Pola formularza: kwota, kategoria, data i opcjonalny opis.
- Wydatki są przechowywane tylko w pamięci aktualnej sesji przeglądarki.
- Trwały zapis w SQLite jest zakresem Sprintu 3.

## Zadania

- [x] Utworzyć listę wydatków w `st.session_state`.
- [x] Zbudować formularz dodawania wydatku.
- [x] Sprawdzić poprawność kwoty.
- [x] Dodać wydatek do listy po wysłaniu formularza.
- [x] Wyświetlić komunikat powodzenia i tymczasową listę wydatków.
- [x] Ręcznie sprawdzić dodawanie kilku wydatków.
- [x] Uzupełnić README i dokumentację.
- [ ] Utworzyć commit, tag `v0.2.0` i GitHub Release.

## Kryteria ukończenia

- Nie można dodać wydatku o wartości zero lub mniejszej.
- Każdy poprawny wydatek pojawia się na liście w tej samej sesji.
- Na liście są widoczne kwota, kategoria, data i opis.
- Po ponownym uruchomieniu aplikacji lista może być pusta — to świadome ograniczenie tej wersji.
