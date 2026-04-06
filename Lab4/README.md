Instrukcja uruchamiania aplikacji:
1. Lokalnie
  a) Zainstaluj zależności
      pip install -r requirements.txt
  b) Uruchom serwer
      uvicorn zadanie_4:app --host 0.0.0.0 --port 8000
  Aplikacja będzie dostępna pod adresem: **http://127.0.0.1:8000**

2. Za pomocą dockera
  a) Zbuduj obraz
      docker build -t ml-api .
  b) Uruchom kontener
      docker run -d -p 8000:8000 ml-api
  Aplikacja dostępna pod adresem: **http://127.0.0.1:8000**

3. Za pomocą docker compose
  a) Uruchom aplikację razem z Redis
      docker-compose up --build
  b) Zatrzymaj aplikację
      docker-compose down
  Aplikacja dostępna pod adresem: **http://127.0.0.1:8000**
  Redis dostępny na porcie: **6379**

Konfiguracja parametrów - zmienne środowiskowe
    Zmienne można ustawić:
      Lokalnie - przed uruchomieniem serwera
          environment:
            - REDIS_HOST=redis
            - REDIS_PORT=6379
      Docker - przez flagę -e
         docker run -d -p 8000:8000 -e REDIS_HOST=localhost ml-api    
      Docker Compose - w sekcji enviromment w pliku docker-compose.yml

Wymagane zasoby:
  Minimalne:
    CPU:  1 rdzeń
    RAM:  256 MB
    Dysk:  500 MB

  Zalecane:
    CPU:  2 rdzenie
    RAM:  512 MB
    Dysk:  1 GB

Endpointy API
  Metoda    Endpoint    Opis
  GET       /           Informacja o API
  GET       /health     Status aplikacji
  GET       /info       Informacje o modelu
  POST      /predict    Predykcja na podstawie parametru
