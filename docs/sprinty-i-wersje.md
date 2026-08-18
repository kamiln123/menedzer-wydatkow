# Sprinty i wersje GitHub

## Zasada pracy

Każdy sprint kończymy działającą, sprawdzoną wersją projektu. Wykonamy wtedy commit w Git, oznaczymy go tagiem w formacie `vX.Y.Z` i opublikujemy na GitHubie jako release z krótkim opisem zmian.

Numer wersji ma postać `vMAJOR.MINOR.PATCH`:

- **MAJOR** — duża, niekompatybilna zmiana (na tym projekcie prawdopodobnie niepotrzebna przed 1.0.0).
- **MINOR** — nowa zauważalna funkcja ukończona w sprincie.
- **PATCH** — mała poprawka błędu.

## Plan wersji MVP

| Sprint | Wersja | Rezultat |
| --- | --- | --- |
| 1 | `v0.1.0` | Aplikacja Streamlit uruchamia się lokalnie. |
| 2 | `v0.2.0` | Można dodać wydatek w formularzu. |
| 3 | `v0.3.0` | Wydatki są trwale zapisywane w SQLite. |
| 4 | `v0.4.0` | Jest lista wydatków oraz filtry. |
| 5 | `v0.5.0` | Działa budżet miesięczny i podsumowanie. |
| 6 | `v0.6.0` | Są wykresy oraz dopracowana walidacja. |
| 7 | `v1.0.0` | MVP ma testy, kompletne README i jest gotowe do pokazania w portfolio. |

## Informacje potrzebne przed pierwszym publikowaniem

Lokalne repozytorium Git jest gotowe, ale nie ma jeszcze adresu zdalnego repozytorium GitHub. Przed publikacją `v0.1.0` utworzymy puste repozytorium na Twoim koncie GitHub, najlepiej publiczne ze względu na portfolio, i połączymy je z tym folderem.
