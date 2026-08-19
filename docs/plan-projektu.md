# Plan projektu: Menedżer wydatków

## Cel

Stworzyć dopracowaną aplikację portfolio w Pythonie, która pozwala rejestrować prywatne wydatki, przeglądać je według kategorii i sprawdzać realizację miesięcznego budżetu.

Projekt ma jednocześnie odświeżyć podstawy Pythona i wprowadzić praktyczne elementy pracy programisty: strukturę projektu, bazę danych, testy, kontrolę wersji oraz dokumentację.

## Użytkownik

Pierwsza wersja jest przeznaczona dla jednej osoby korzystającej lokalnie z aplikacji. Nie zakładamy na początku logowania ani kont wielu użytkowników.

## Zakres wersji 1.0 (MVP)

MVP to najmniejsza kompletna wersja aplikacji, którą można uruchomić i zaprezentować.

- Dodawanie wydatku: kwota, data, kategoria, opis.
- Lista zapisanych wydatków z filtrowaniem po miesiącu i kategorii.
- Edycja oraz usuwanie wydatku.
- Domyślne kategorie, np. jedzenie, transport, rachunki, rozrywka i zdrowie.
- Ustawienie miesięcznego budżetu.
- Panel podsumowania: suma wydatków, dostępna kwota i udział kategorii.
- Wykres wydatków według kategorii.
- Trwały zapis danych w lokalnej bazie SQLite.
- Czytelne README z instrukcją instalacji i uruchomienia.

## Poza zakresem MVP

Te funkcje są wartościowe, ale zostawiamy je na później, aby projekt szybko stał się użyteczny.

- Logowanie i wielu użytkowników.
- Synchronizacja danych w chmurze.
- Import operacji bankowych CSV.
- Skanowanie paragonów.
- Wersja mobilna.
- Automatyczne klasyfikowanie wydatków przez AI.

## Etapy realizacji

1. **Przygotowanie projektu** — środowisko Python, zależności, podstawowa struktura i Git.
2. **Logika danych** — model wydatku, kategorie, baza SQLite i podstawowe operacje zapisu/odczytu.
3. **Interfejs** — formularz dodawania wydatku i tabela transakcji w Streamlit.
4. **Budżet oraz analityka** — limity miesięczne, podsumowania i wykresy.
5. **Jakość** — obsługa błędów, walidacja danych i testy logiki.
6. **Portfolio** — zrzuty ekranu, kompletne README, ewentualne wdrożenie publicznej wersji demonstracyjnej.

## Bieżący sprint

### Sprint 1 — Fundament aplikacji (`v0.1.0`)

**Cel:** przygotować środowisko i wyświetlić pierwszą stronę aplikacji w przeglądarce.

- [x] Utworzenie lokalnego repozytorium Git.
- [x] Utworzenie dokumentacji startowej.
- [x] Dodanie punktu startowego aplikacji `app.py`.
- [x] Dodanie listy zależności.
- [ ] Dodanie zasad ignorowania plików lokalnych (`.gitignore`).
- [x] Utworzenie wirtualnego środowiska Python (`.venv`).
- [x] Instalacja Streamlit.
- [x] Lokalne uruchomienie aplikacji.
- [x] Utworzenie lokalnego commitu, tagu `v0.1.0` i publikacja release na GitHubie.

### Sprint 2 — Formularz i tymczasowa lista (`v0.2.0`)

**Cel:** użytkownik dodaje wydatki w formularzu i widzi je do końca bieżącej sesji aplikacji.

Szczegółowy zakres: [Sprint 2 — Formularz i tymczasowa lista wydatków](sprint-2.md).

### Sprint 3 — Trwały zapis w SQLite (`v0.3.0`)

**Cel:** dane o wydatkach przetrwają ponowne uruchomienie aplikacji dzięki lokalnej bazie SQLite.

Szczegółowy zakres: [Sprint 3 — Trwały zapis w SQLite](sprint-3.md).

## Kryteria ukończenia MVP

- Aplikację da się uruchomić według instrukcji w README.
- Użytkownik może dodać, zobaczyć, poprawić i usunąć wydatek.
- Dane pozostają dostępne po ponownym uruchomieniu.
- Użytkownik widzi podsumowanie bieżącego miesiąca i wykres kategorii.
- Najważniejsza logika ma testy automatyczne.

## Plan nauki podczas projektu

| Obszar | Praktyka w projekcie |
| --- | --- |
| Python | funkcje, klasy, moduły, obsługa błędów, typowanie |
| Dane | SQLite, modele danych, zapytania i walidacja |
| Web | interfejs Streamlit, formularze, stan aplikacji |
| Jakość | Git, testy pytest, formatowanie i dokumentacja |

## Orientacyjny harmonogram

Przy nauce i pracy około 4–6 godzin tygodniowo: 3–5 tygodni do pełnego MVP. Przy 1–2 godzinach dziennie: około 10–14 dni. Samo minimalne, działające dodawanie i wyświetlanie wydatków możemy osiągnąć w pierwszym spotkaniu, zwykle w 2–4 godziny.
