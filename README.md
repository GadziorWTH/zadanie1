# GitHub Actions Pipeline

## Konfiguracja workflow

### 1. Sekrety
Dodaj w ustawieniach repozytorium GitHub:
- `DOCKERHUB_USERNAME` - nazwa użytkownika Docker Hub
- `DOCKERHUB_TOKEN` - token dostępu Docker Hub

### 2. Cache
- Cache przechowywany jest w publicznym repozytorium na Docker Hub
- Nazwa repozytorium cache: `<DOCKERHUB_USERNAME>/zad2-repo`

### 3. Test Trivy
- Sprawdza tylko luki `CRITICAL` i `HIGH`
- Ignoruje niezałatwione podatności (`ignore-unfixed: true`)
- Jeśli znajdzie krytyczne luki - blokuje pipeline

### Podatności w setuptools
Zignorowane podatności (CVE-2022-40897, CVE-2024-6345, CVE-2025-47273) dotyczą pakietu `setuptools` w wersji 58.1.0. Użyto pliku `.trivyignore` jako dodatkowej warstwy zabezpieczeń

### Uzasadnienie
- Podatności nie są eksploatowalne w kontekście naszej aplikacji(zad1)
- Aktualizacja setuptools rozwiązuje problem u źródła
- Plik ignorowania jest zabezpieczeniem na wypadek problemów z aktualizacją
