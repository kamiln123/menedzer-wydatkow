# Sprint 9 — Finalizacja MVP

## Cel

Zamknąć projekt jako spójną, sprawdzoną i gotową do prezentacji wersję `v1.0.0`.

## Ustalenia

- Nie dodajemy nowych funkcji biznesowych poza poprawkami wykrytymi podczas audytu.
- Aplikacja pozostaje lokalna i korzysta z SQLite; publiczne wdrożenie jest poza MVP.
- GitHub Actions uruchamia testy automatycznie po zmianach w `main` i w pull requestach.
- Końcowa dokumentacja opisuje rzeczywisty stan projektu, a nie planowane funkcje.
- README otrzyma aktualny zrzut ekranu sekcji zarządzania wydatkiem.
- Projekt jest udostępniany na licencji MIT.

## Zakres

- Poprawienie pełnego odświeżania danych po dodaniu wydatku.
- Uporządkowanie kodu i plików ignorowanych przez Git.
- Dodanie workflow CI dla Pythona 3.13 i pytest.
- Ponowne uruchomienie wszystkich testów oraz test startu aplikacji.
- Kontrola spójności README, dokumentacji sprintów, tagów i release.
- Dodanie aktualnego zrzutu ekranu edycji i usuwania.
- Uzupełnienie prezentacji repozytorium na GitHubie.
- Dodanie pliku licencji MIT.

## Poza zakresem

- Publiczne wdrożenie aplikacji.
- Logowanie i obsługa wielu użytkowników.
- Zewnętrzna lub chmurowa baza danych.
- Import danych bankowych i nowe raporty.

## Zadania

- [x] Naprawić odświeżanie podsumowania, wykresu i filtrów po dodaniu wydatku.
- [x] Dodać katalogi techniczne pytest do `.gitignore`.
- [x] Dodać workflow GitHub Actions uruchamiający testy.
- [ ] Potwierdzić poprawne wykonanie workflow na GitHubie.
- [x] Uruchomić wszystkie testy lokalne — 7 testów zakończonych powodzeniem.
- [ ] Wykonać test startu aplikacji i pełny test ręczny MVP.
- [ ] Dodać zrzut ekranu sekcji zarządzania wydatkiem.
- [ ] Uzupełnić README i sprawdzić wszystkie odnośniki.
- [ ] Uzupełnić tematy repozytorium na GitHubie.
- [x] Dodać licencję MIT dla właściciela praw Kamil Napora.
- [ ] Wykonać końcowy audyt kodu, zależności, danych i dokumentacji.
- [ ] Utworzyć commit, tag `v1.0.0` i GitHub Release.

## Kryteria ukończenia

- Wszystkie elementy przyjętego zakresu MVP działają i są udokumentowane.
- Testy lokalne oraz GitHub Actions kończą się powodzeniem.
- Po każdej zmianie danych podsumowanie, wykres, filtry i tabela są aktualne.
- Repozytorium nie zawiera lokalnej bazy, środowiska `.venv`, cache ani sekretów.
- README pozwala uruchomić projekt od zera i prezentuje aktualny interfejs.
- GitHub zawiera czytelną historię wersji oraz release `v1.0.0`.
