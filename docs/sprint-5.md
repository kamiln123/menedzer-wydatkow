# Sprint 5 — Miesięczny budżet i podsumowanie

## Cel

Pozwolić użytkownikowi ustawić budżet dla miesiąca oraz zobaczyć kwotę wydatków, budżet i pozostałą kwotę.

## Ustalenia

- Budżety są zapisywane w osobnej tabeli SQLite `budgets`.
- Jeden miesiąc może mieć tylko jeden budżet; zapis nowej wartości aktualizuje istniejącą.
- Kwota budżetu jest przechowywana jako liczba całkowita groszy.
- Po wybraniu konkretnego miesiąca podsumowanie dotyczy tego miesiąca.
- Po wybraniu „Wszystkie” podsumowanie agreguje wszystkie wydatki oraz wszystkie ustawione budżety.
- Miesiąc bez ustawionego budżetu ma wartość `0 zł`; aplikacja pokaże ostrzeżenie o takim miesiącu.
- Filtr kategorii wpływa tylko na tabelę. Podsumowanie budżetu uwzględnia wszystkie kategorie.

## Zakres

- Formularz ustawienia lub aktualizacji budżetu wybranego miesiąca.
- Podsumowanie: wydano, budżet i pozostało.
- Obsługa przekroczonego budżetu.
- Ostrzeżenie o miesiącach bez budżetu w widoku „Wszystkie”.

## Poza zakresem

- Budżety osobno dla kategorii.
- Wykresy wydatków i budżetu.
- Edycja lub usuwanie wydatków.

## Zadania

- [x] Utworzyć tabelę `budgets`.
- [x] Dodać zapis i odczyt budżetów.
- [x] Dodać formularz ustawienia budżetu.
- [x] Obliczać sumę wydatków niezależnie od filtra kategorii.
- [x] Wyświetlić trzy wartości podsumowania.
- [x] Obsłużyć przekroczony lub nieustawiony budżet.
- [x] Ręcznie przetestować podsumowanie pojedynczego miesiąca i wszystkich miesięcy.
- [x] Uzupełnić dokumentację.
- [x] Utworzyć commit, tag `v0.5.0` i GitHub Release.

## Kryteria ukończenia

- Budżet pozostaje dostępny po ponownym uruchomieniu aplikacji.
- Ponowny zapis budżetu tego samego miesiąca aktualizuje jego wartość.
- Podsumowanie pojedynczego miesiąca jest poprawne.
- Widok „Wszystkie” poprawnie agreguje wydatki i budżety.
