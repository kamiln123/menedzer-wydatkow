# Menedżer wydatków

Aplikacja webowa do prostego zapisywania wydatków, śledzenia budżetu i przeglądania miesięcznych statystyk.

Projekt powstaje jako portfolio i praktyczny powrót do języka Python. Rozwijamy go iteracyjnie: najpierw sprawnie działająca, niewielka wersja, potem kolejne usprawnienia.

## Status

Sprint 1 został opublikowany jako release `v0.1.0`, a Sprint 2 — formularz oraz tymczasowa lista wydatków — jako release `v0.2.0`.

Kolejny etap: trwały zapis wydatków w lokalnej bazie SQLite.

## Planowany stos technologiczny

- Python 3.12+
- Streamlit — prosty interfejs webowy
- SQLite — lokalna baza danych
- SQLAlchemy — komunikacja z bazą danych
- pandas i Plotly — analizy oraz wykresy
- pytest — testy automatyczne

## Dokumentacja

- [Plan projektu](docs/plan-projektu.md)
- [Dziennik decyzji](docs/decyzje.md)
- [Sprinty i wersje](docs/sprinty-i-wersje.md)

## Uruchamianie (po przygotowaniu środowiska)

```powershell
.\.venv\Scripts\Activate.ps1
python -m streamlit run app.py
```

Po uruchomieniu aplikacja będzie dostępna w przeglądarce, zwykle pod adresem `http://localhost:8501`.
