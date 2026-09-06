# Sprint 7 — Testy automatyczne i materiały portfolio

## Cel

Dodać powtarzalne testy najważniejszej logiki oraz przygotować pierwszą prezentację działania aplikacji w repozytorium.

## Ustalenia

- Testy automatyczne wykonujemy biblioteką pytest.
- Testy tworzą osobną, tymczasową bazę SQLite i nie korzystają z pliku `data/expenses.db`.
- Testujemy logikę warstwy bazy danych, a nie wygląd interfejsu Streamlit.
- README pokazuje rzeczywiste zrzuty ekranu aplikacji.
- Pełne MVP zostanie wydane dopiero po dodaniu edycji i usuwania wydatków.

## Zakres

- Instalacja pytest i aktualizacja `requirements.txt`.
- Izolowanie testów przez tymczasową zmianę `DATABASE_PATH` za pomocą fixture pytest i `monkeypatch`.
- Testy dodawania i odczytu wydatków, filtrów, budżetów, podsumowań oraz danych wykresu.
- Dodanie do README opisu funkcji, technologii, uruchamiania i testów.
- Dodanie trzech zrzutów ekranu aplikacji.

## Zadania

- [x] Zainstalować pytest w `.venv` i zapisać zależności.
- [x] Odizolować testy od prawdziwej bazy przez fixture, `tmp_path` i `monkeypatch`.
- [x] Utworzyć zestaw pięciu testów bazy danych.
- [x] Uruchomić testy i poprawić ewentualne błędy (`5 passed`).
- [x] Uzupełnić README o opis projektu, uruchamianie i testy.
- [x] Wykonać i dodać trzy zrzuty ekranu.
- [x] Uzupełnić dokumentację.
- [x] Utworzyć commit, tag `v0.7.0` i GitHub Release.

## Kryteria ukończenia

- Polecenie uruchamiające pytest kończy się wynikiem `5 passed`.
- Testy nie odczytują ani nie zmieniają pliku `data/expenses.db`.
- README opisuje aktualne funkcje i sposób uruchomienia projektu.
- README zawiera trzy czytelne zrzuty rzeczywistej aplikacji.
- Repozytorium ma release `v0.7.0`.
