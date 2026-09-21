# Sprint 8 — Edycja i usuwanie wydatków

## Cel

Pozwolić użytkownikowi poprawić istniejący wydatek albo bezpiecznie usunąć go z bazy danych.

## Ustalenia

- Sekcja „Zarządzaj wydatkiem” znajdzie się pod tabelą zapisanych wydatków.
- Lista wyboru zawiera tylko wydatki widoczne po zastosowaniu filtrów.
- Formularz edycji jest wypełniany aktualnymi danymi wybranego rekordu.
- Edycja korzysta z tych samych reguł walidacji co dodawanie.
- Przyciski zapisu i usuwania znajdują się obok siebie w formularzu zarządzania.
- Usunięcie wymaga dodatkowego potwierdzenia przyciskiem „Tak, usuń” albo rezygnacji przyciskiem „Anuluj”.
- Po zmianie aplikacja odświeża podsumowanie, wykres, filtry i tabelę.

## Zakres

- Testy aktualizacji i usuwania rekordu.
- Funkcje `update_expense` oraz `delete_expense` w warstwie bazy danych.
- Wybór wydatku z czytelną etykietą zawierającą datę, kategorię i kwotę.
- Formularz edycji kwoty, kategorii, daty i opisu.
- Bezpieczne usuwanie z potwierdzeniem.
- Komunikaty powodzenia i walidacji.

## Poza zakresem

- Cofanie usunięcia.
- Masowa edycja lub usuwanie wielu rekordów.
- Historia zmian wydatku.

## Zadania

- [x] Napisać test aktualizacji wydatku.
- [x] Napisać test usuwania wydatku.
- [x] Dodać funkcję aktualizującą rekord w SQLite.
- [x] Dodać funkcję usuwającą rekord w SQLite.
- [x] Dodać wybór widocznego wydatku w interfejsie.
- [x] Dodać formularz edycji z walidacją.
- [x] Dodać usuwanie wymagające potwierdzenia.
- [x] Automatycznie odświeżać aplikację po zmianie.
- [x] Uruchomić testy automatyczne — 7 testów zakończonych powodzeniem.
- [x] Ręcznie przetestować edycję i usuwanie.
- [x] Uzupełnić dokumentację.
- [x] Utworzyć commit, tag `v0.8.0` i GitHub Release.

## Kryteria ukończenia

- Edycja zmienia istniejący rekord i nie tworzy duplikatu.
- Usunięty rekord znika z bazy, tabeli, podsumowania i wykresu.
- Nie można zapisać niepoprawnej kwoty ani zbyt długiego opisu.
- Nie można usunąć rekordu bez potwierdzenia.
- Wszystkie testy automatyczne przechodzą.
- Repozytorium ma release `v0.8.0`.
