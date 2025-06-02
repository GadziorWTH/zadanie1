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
