# Sprint 3 — Trwały zapis w SQLite

## Cel

Zastąpić tymczasową listę sesji lokalną bazą SQLite, aby wydatki pozostały dostępne po ponownym uruchomieniu aplikacji.

## Ustalenia

- Baza będzie lokalnym plikiem `data/expenses.db`.
- Folder `data/` jest ignorowany przez Git, więc dane użytkownika nie trafią do publicznego repozytorium.
- Użytkownik wpisuje i widzi kwoty w złotówkach, np. `25,50 zł`.
- Baza przechowuje kwotę jako liczbę całkowitą groszy, np. `2550` dla `25,50 zł`.
- Tabela `expenses` będzie zawierać: identyfikator, kwotę w groszach, kategorię, datę oraz opis.

## Zadania

- [x] Utworzyć moduł odpowiedzialny za bazę danych.
- [x] Automatycznie utworzyć folder `data/` i plik bazy.
- [x] Utworzyć tabelę `expenses`, jeżeli jeszcze nie istnieje.
- [x] Zapisywać poprawny wydatek w SQLite.
- [x] Odczytywać wydatki z SQLite i wyświetlać je w aplikacji.
- [x] Przeliczać kwotę między złotówkami interfejsu a groszami bazy.
- [x] Ręcznie sprawdzić trwałość danych po restarcie aplikacji.
- [x] Uzupełnić dokumentację.
- [x] Utworzyć commit, tag `v0.3.0` i GitHub Release.

## Kryteria ukończenia

- Po dodaniu wydatku pojawia się on na liście.
- Po zatrzymaniu i ponownym uruchomieniu aplikacji wydatek nadal jest widoczny.
- Wartość w tabeli bazy jest dodatnią liczbą całkowitą groszy.
- Użytkownik nadal widzi kwoty sformatowane jako złotówki.
