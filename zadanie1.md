# Zadania 1

## Opis implementacji

### 1. Aplikacja
- Uzylem Flask + Gunicorn (WSGI).
- Mozna wyświetlając aktualną temperaturę za pomoca OpenWeatherMap API.
- Endpoint `/health` do sprawdzania statusu aplikacji.
- `API_KEY` – klucz API z OpenWeatherMap.

### 2. Dockerfile
- **Optymalizacje**:
  - Wieloetapowe budowanie (`builder` → finalny obraz).
  - Obraz bazowy: `python:3.9-alpine` (minimalny rozmiar).
  - Healthcheck z użyciem `curl`.
  - Oznaczenie autora zgodne ze standardem OCI.

### 3. Polecenia
```bash
# a) Budowanie obrazu
docker build -t weather-app .

# b) Uruchomienie kontenera
docker run -d -p 8080:8080 --name weather-app -e API_KEY=xxx weather-app

# c) Pobranie logów
docker logs weather-app

# d) Sprawdzenie warstw i rozmiaru
docker image inspect weather-app --format '{{.RootFS.Layers}}'
docker image ls | grep weather-app
