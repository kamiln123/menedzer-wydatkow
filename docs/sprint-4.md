# Sprint 4 — Tabela i filtrowanie wydatków

## Cel

Zastąpić tekstową listę wydatków czytelną tabelą oraz umożliwić ograniczanie widocznych danych do wybranej kategorii i miesiąca.

## Zakres

- Wyświetlanie wydatków w tabeli z kolumnami: data, kategoria, opis i kwota.
- Filtrowanie po kategorii, z opcją „Wszystkie”.
- Filtrowanie po miesiącu, z opcją „Wszystkie”.
- Filtry umieszczone w panelu bocznym aplikacji.
- Komunikat, gdy żaden wydatek nie pasuje do wybranych filtrów.
- Liczba widocznych wyników.

## Potwierdzone decyzje

- Używamy `st.dataframe` do wyświetlania tabeli.
- Filtry są umieszczone w panelu bocznym.
- Dostępne miesiące są pobierane z bazy; obok nich dostępna jest opcja „Wszystkie”.

## Poza zakresem

- Edycja i usuwanie wydatków.
- Budżet miesięczny i wykresy.
- Logowanie użytkownika.

## Zadania

- [x] Wybrać sposób prezentacji tabeli.
- [x] Pobrać dostępne miesiące i kategorie z bazy.
- [x] Dodać kontrolki filtrów do panelu bocznego.
- [x] Zmienić zapytanie SQL tak, aby uwzględniało aktywne filtry.
- [x] Przekształcić dane z bazy do formatu tabeli interfejsu.
- [x] Wyświetlić liczbę dopasowanych wydatków lub komunikat o braku wyników.
- [x] Ręcznie przetestować kombinacje filtrów.
- [x] Uzupełnić dokumentację.
- [ ] Utworzyć commit, tag `v0.4.0` i GitHub Release.
