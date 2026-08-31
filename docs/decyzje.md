# Dziennik decyzji projektu

Ten plik zapisuje ważniejsze ustalenia oraz ich uzasadnienie. Dzięki temu dokumentacja odzwierciedla rozwój projektu, a nie tylko jego końcowy stan.

## 2026-08-17 — Wybór tematu

**Decyzja:** Tworzymy aplikację „Menedżer wydatków”.

**Uzasadnienie:** Temat jest wystarczająco praktyczny i atrakcyjny do portfolio, a jego zakres pozwala ćwiczyć Python, bazę danych, prosty interfejs webowy, wizualizację danych oraz testy.

## 2026-08-17 — Kierunek techniczny

**Decyzja:** Pierwszą wersję zbudujemy w Pythonie z interfejsem Streamlit i lokalną bazą SQLite.

**Uzasadnienie:** Streamlit pozwala szybko uzyskać estetyczną aplikację bez nauki osobnego frameworka frontendowego. SQLite nie wymaga instalowania serwera bazy danych, a jednocześnie daje doświadczenie z trwałym zapisem danych.

## 2026-08-17 — Strategia realizacji

**Decyzja:** Rozwijamy projekt od MVP, a funkcje bardziej zaawansowane planujemy jako kolejne etapy.

**Uzasadnienie:** Priorytetem jest ukończenie prezentowalnej wersji aplikacji oraz regularna praktyka programowania, nie maksymalna liczba funkcji.

## 2026-08-18 — Lokalne środowisko Python

**Decyzja:** Korzystamy z wirtualnego środowiska `.venv` umieszczonego w głównym folderze projektu.

**Uzasadnienie:** Biblioteki potrzebne przez aplikację są oddzielone od pozostałych projektów na komputerze. Ich wersje zapisujemy w `requirements.txt`, dzięki czemu środowisko można odtworzyć po pobraniu projektu z GitHuba.

## 2026-08-18 — Pierwsza wersja projektu

**Decyzja:** Sprint 1 został oznaczony tagiem `v0.1.0` i opublikowany jako GitHub Release.

**Uzasadnienie:** Każdy ukończony sprint ma mieć możliwą do odtworzenia, publiczną wersję. Tag wskazuje dokładny stan kodu, a release czytelnie opisuje postęp projektu w portfolio.

## 2026-08-19 — Druga wersja projektu

**Decyzja:** Sprint 2 został oznaczony tagiem `v0.2.0` i opublikowany jako GitHub Release.

**Uzasadnienie:** Wersja stanowi działający etap aplikacji: formularz, walidację i tymczasową listę wydatków. Kolejna wersja skupi się na trwałości danych, bez równoczesnego zwiększania zakresu interfejsu.

## 2026-08-19 — Format kwot w bazie danych

**Decyzja:** SQLite zapisuje kwoty jako całkowitą liczbę groszy, a interfejs pokazuje je w złotówkach.

**Uzasadnienie:** Liczby zmiennoprzecinkowe mogą niedokładnie reprezentować wartości dziesiętne. Zapis całkowity, np. `2550` zamiast `25,50`, pozwala bezpiecznie wykonywać późniejsze obliczenia budżetu i sum wydatków.

## 2026-08-19 — Trzecia wersja projektu

**Decyzja:** Sprint 3 został oznaczony tagiem `v0.3.0` i opublikowany jako GitHub Release.

**Uzasadnienie:** Wersja zapewnia trwałość danych: wydatki są zapisywane lokalnie, odczytywane po ponownym uruchomieniu i nie trafiają do repozytorium GitHub.

## 2026-08-21 — Filtry w Sprint 4

**Decyzja:** Wydatki będą prezentowane w `st.dataframe`, a filtry kategorii i miesiąca znajdą się w panelu bocznym. Opcje miesiąca pochodzą z danych zapisanych w SQLite.

**Uzasadnienie:** Tabela daje czytelny widok danych, panel boczny nie zmniejsza miejsca na wyniki, a dynamiczne opcje filtrów nie pokazują miesięcy bez zapisanych wydatków.

## 2026-08-21 — Czwarta wersja projektu

**Decyzja:** Sprint 4 został oznaczony tagiem `v0.4.0` i opublikowany jako GitHub Release.

**Uzasadnienie:** Wersja umożliwia wygodne przeglądanie danych: tabela, filtry oraz obsługa braku wyników działają na trwałych danych zapisanych w SQLite.

## 2026-08-21 — Zasady podsumowania budżetu

**Decyzja:** Podsumowanie budżetowe reaguje wyłącznie na filtr miesiąca. W widoku „Wszystkie” agreguje wszystkie wydatki i ustawione budżety, a filtr kategorii wpływa tylko na tabelę.

**Uzasadnienie:** Budżet jest limitem miesięcznym dla wszystkich wydatków. Porównywanie pełnego budżetu tylko z jedną kategorią prowadziłoby do mylących wniosków.

## 2026-08-31 — Budżety miesięczne w Sprint 5

**Decyzja:** Budżety zapisujemy w osobnej tabeli `budgets`, po jednym budżecie na miesiąc. Ponowny zapis dla tego samego miesiąca aktualizuje wcześniejszą wartość.

**Uzasadnienie:** Budżet jest innym rodzajem danych niż wydatek i nie powinien być przechowywany w tabeli `expenses`. Ograniczenie jednego budżetu na miesiąc upraszcza model danych, a aktualizacja pozwala użytkownikowi zmienić limit bez tworzenia duplikatów.

## 2026-08-31 — Piąta wersja projektu

**Decyzja:** Sprint 5 został oznaczony tagiem `v0.5.0` i opublikowany jako GitHub Release.

**Uzasadnienie:** Wersja zamyka etap budżetowania: użytkownik może trwale zapisać limit miesiąca i sprawdzić jego realizację w widoku pojedynczego miesiąca lub wszystkich danych.
