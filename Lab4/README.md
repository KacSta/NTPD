Instrukcja uruchamiania aplikacji:
1. Lokalnie<br>
  a) Zainstaluj zależności<br>
      pip install -r requirements.txt<br><br>
  b) Uruchom serwer<br>
      uvicorn zadanie_4:app --host 0.0.0.0 --port 8000<br>
  Aplikacja będzie dostępna pod adresem: **http://127.0.0.1:8000**<br>

2. Za pomocą dockera<br>
  a) Zbuduj obraz<br>
      docker build -t ml-api .<br><br>
  b) Uruchom kontener<br>
      docker run -d -p 8000:8000 ml-api<br>
  Aplikacja dostępna pod adresem: **http://127.0.0.1:8000**<br>

3. Za pomocą docker compose<br>
  a) Uruchom aplikację razem z Redis<br>
      docker-compose up --build<br><br>
  b) Zatrzymaj aplikację<br>
      docker-compose down<br>
  Aplikacja dostępna pod adresem: **http://127.0.0.1:8000**<br>
  Redis dostępny na porcie: **6379**<br>

Konfiguracja parametrów - zmienne środowiskowe<br>
    Zmienne można ustawić:<br>
      **Lokalnie** - przed uruchomieniem serwera<br>
          environment:<br>
            - REDIS_HOST=redis<br>
            - REDIS_PORT=6379<br><br>
      **Docker** - przez flagę -e<br>
         docker run -d -p 8000:8000 -e REDIS_HOST=localhost ml-api<br><br>
      **Docker Compose** - w sekcji environment w pliku docker-compose.yml<br>

### Wymagane zasoby

* **Minimalne:**
    * CPU: 1 rdzeń
    * RAM: 1 GB
    * Dysk: 3 GB
* **Zalecane:**
    * CPU: 2 rdzenie
    * RAM: 2 GB
    * Dysk: 5 GB

### Endpointy API

| Metoda | Endpoint | Opis |
| :--- | :--- | :--- |
| **GET** | `/` | Informacja o API |
| **GET** | `/health` | Status aplikacji |
| **GET** | `/info` | Informacje o modelu |
| **POST** | `/predict` | Predykcja na podstawie parametru |
