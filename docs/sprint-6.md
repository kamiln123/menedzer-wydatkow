# Sprint 6 — Wykres kategorii i walidacja

## Cel

Pokazać użytkownikowi strukturę wydatków według kategorii oraz dopracować sposób obsługi opisu wydatku.

## Ustalenia

- Wykres będzie wykonany biblioteką Plotly, używając modułu `plotly.express`.
- Będzie to wykres słupkowy sum wydatków według kategorii.
- Wykres reaguje tylko na filtr miesiąca, tak jak podsumowanie budżetu.
- Filtr kategorii nadal wpływa tylko na tabelę wydatków.
- Przed zapisem opis zostanie oczyszczony metodą `.strip()`.
- Opis może mieć maksymalnie 200 znaków; dłuższy wpis pokaże komunikat błędu i nie zostanie zapisany.

## Zakres

- Instalacja Plotly w aktywnym środowisku `.venv` i aktualizacja `requirements.txt`.
- Funkcja bazy danych zwracająca sumę wydatków dla każdej kategorii, opcjonalnie dla miesiąca.
- Wykres słupkowy w głównym obszarze aplikacji.
- Komunikat informacyjny, jeśli nie ma danych do pokazania na wykresie.
- Walidacja długości i oczyszczanie opisu wydatku.

## Poza zakresem

- Wykresy budżetu, trendów dziennych i porównań miesięcy.
- Eksport wykresów lub danych.
- Tworzenie własnych kategorii.

## Zadania

- [x] Zainstalować Plotly w `.venv` i zapisać zależności.
- [x] Dodać funkcję agregującą kwoty według kategorii.
- [x] Sprawdzić funkcję poleceniem w terminalu.
- [x] Wyświetlić wykres Plotly dla miesiąca lub wszystkich miesięcy.
- [x] Obsłużyć brak danych dla wykresu.
- [x] Oczyścić opis metodą `.strip()`.
- [x] Odrzucać opis dłuższy niż 200 znaków.
- [x] Ręcznie przetestować wykres i walidację.
- [x] Uzupełnić dokumentację.
- [ ] Utworzyć commit, tag `v0.6.0` i GitHub Release.

## Kryteria ukończenia

- Wykres poprawnie pokazuje sumy kategorii dla wybranego miesiąca.
- W widoku „Wszystkie” wykres agreguje wszystkie miesiące.
- Zmiana filtra kategorii nie zmienia danych wykresu.
- Brak wydatków daje czytelny komunikat zamiast pustego wykresu.
- Opis po zapisie nie ma niepotrzebnych spacji na początku ani końcu i nie przekracza 200 znaków.
