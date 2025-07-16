# 4. Web Development i API: Tworzenie Usług w Pythonie

> [!INFO]
> Twoje doświadczenie w tworzeniu aplikacji webowych jest bezcenne w świecie Pythona. Koncepcje takie jak cykl życia żądania i odpowiedzi (`request`/`response`), routing, middleware czy komunikacja z bazą danych są uniwersalne. Python oferuje dojrzały i zróżnicowany ekosystem frameworków, które pozwalają te koncepcje efektywnie implementować.

## Wybór Frameworka: Znajdź Narzędzie Odpowiednie do Zadania

Python posiada trzy główne frameworki webowe, które różnią się filozofią, zakresem i najlepszymi przypadkami użycia. Wybór zależy od skali projektu, wymagań dotyczących wydajności i preferowanego stylu pracy.

---

### [Flask](https://flask.palletsprojects.com/en/stable/): Minimalistyczny i Elastyczny Mikro-framework 🧱

[Flask](https://flask.palletsprojects.com/en/stable/) kieruje się filozofią "zrób to sam". Dostarcza solidny, ale minimalistyczny rdzeń, który zajmuje się routingiem i obsługą żądań, a wszystkie dodatkowe funkcjonalności, takie jak obsługa bazy danych czy walidacja formularzy, pozostawia deweloperowi do wyboru i integracji za pomocą zewnętrznych bibliotek.

* **Filozofia**: Minimalizm i elastyczność. Dostajesz podstawowe narzędzia, a resztę budujesz sam.
* **Wydajność**: Działa w oparciu o synchroniczny standard **WSGI**, co czyni go wolniejszym od FastAPI w zadaniach wymagających dużej liczby operacji I/O.
* **ORM**: Brak wbudowanego. Najczęściej używany z [**SQLAlchemy**](https://www.sqlalchemy.org/), potężną, niezależną biblioteką ORM.
* **Najlepszy do...**: Małych i średnich projektów, prototypów oraz aplikacji, gdzie kluczowa jest pełna kontrola nad doborem komponentów i elastyczność architektury.

```python
from flask import Flask, jsonify

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Definicja endpointu (trasy)
@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})
```

-----

### [FastAPI](https://fastapi.tiangolo.com/): Nowoczesne, Wysokowydajne API 🚀

[FastAPI](https://fastapi.tiangolo.com/) to nowoczesny framework, który szturmem zdobył popularność dzięki swojej niewiarygodnej wydajności i fantastycznemu doświadczeniu deweloperskiemu. Został zbudowany od podstaw z myślą o tworzeniu API.

  * **Filozofia**: "API first", wydajność i łatwość tworzenia.
  * **Wydajność**: Ekstremalnie wysoka, porównywalna z NodeJS czy Go. Jest to zasługa działania w oparciu o nowoczesny, **asynchroniczny standard ASGI**.
  * **Kluczowe Funkcje**:
      * **Wbudowana walidacja danych**: Wykorzystuje Pydantic i wskazówki typów (`type hints`) do automatycznej walidacji przychodzących żądań i serializacji odpowiedzi.
      * **Automatyczna dokumentacja**: Na podstawie kodu i typów automatycznie generuje interaktywną dokumentację API (w standardach OpenAPI i JSON Schema), dostępną pod adresami `/docs` (Swagger UI) i `/redoc`.
  * **ORM**: Brak wbudowanego, podobnie jak Flask, najczęściej integrowany z [**SQLAlchemy**](https://www.sqlalchemy.org/).
  * **Najlepszy do...**: **Nowoczesnych API (REST, GraphQL), aplikacji wymagających najwyższej wydajności, mikrousług** i projektów, gdzie bezpieczeństwo typów i dobra dokumentacja są priorytetem.

```python
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

app = FastAPI()

@app.post("/users/")
async def create_user(user: User):
    # FastAPI automatycznie zwaliduje dane przychodzące
    # i zwróci błąd 422, jeśli nie pasują do modelu User
    return {"user_created": user.name}
```

-----

### [Django](https://www.djangoproject.com/): Framework "Batteries-Included" 🔋

[Django](https://www.djangoproject.com/) to dojrzały, potężny framework, który podąża za filozofią "wszystko w zestawie". Dostarcza gotowe, zintegrowane rozwiązania dla większości problemów, z jakimi spotykasz się podczas tworzenia dużych aplikacji webowych.

  * **Filozofia**: Kompletny, zintegrowany zestaw narzędzi.
  * **Wydajność**: Głównie synchroniczny (WSGI), z rosnącym wsparciem dla operacji asynchronicznych.
  * **Kluczowe Funkcje**:
      * **Wbudowany, potężny ORM**: Jedna z głównych zalet Django, głęboko zintegrowana z resztą frameworka.
      * **Wbudowany panel administracyjny**: Django potrafi automatycznie wygenerować w pełni funkcjonalny panel admina na podstawie zdefiniowanych modeli bazy danych, co drastycznie przyspiesza development.
      * **Gotowe komponenty**: Posiada wbudowane systemy do autentykacji, formularzy, routingu i cachingu.
  * **Krzywa uczenia**: Wyższa niż w przypadku mikro-frameworków ze względu na dużą liczbę koncepcji do opanowania na starcie.
  * **Najlepszy do...**: Dużych, złożonych aplikacji, systemów CMS, projektów z napiętymi terminami, gdzie gotowe i sprawdzone komponenty pozwalają szybko budować solidne fundamenty.

-----

## Komunikacja HTTP i Serwery Aplikacji

### Komunikacja z Innymi Usługami: [requests](https://requests.readthedocs.io/en/latest/) i [httpx](https://www.python-httpx.org/)

  * [**requests**](https://requests.readthedocs.io/en/latest/): To legendarna, niezwykle prosta w użyciu biblioteka do wykonywania **synchronicznych** zapytań HTTP. Przez lata była de facto standardem.
  * [**httpx**](https://www.python-httpx.org/): To nowoczesny następca [requests](https://requests.readthedocs.io/en/latest/), który oferuje niemal identyczne, przyjazne API, ale dodatkowo wspiera **asynchroniczność (`async`/`await`)** oraz protokół **HTTP/2**. To czyni go domyślnym wyborem dla nowoczesnych aplikacji, zwłaszcza tych budowanych w oparciu o FastAPI.

### Serwery Aplikacji: Uruchamianie w Produkcji

Aplikacje webowe w Pythonie potrzebują serwera aplikacji, który tłumaczy zapytania HTTP na format zrozumiały dla frameworka. Istnieją dwa standardy tej komunikacji:

  * **WSGI (Web Server Gateway Interface)**: Tradycyjny, **synchroniczny** standard, używany przez Flask i Django. Najpopularniejszym, produkcyjnym serwerem WSGI jest [**Gunicorn**](https://gunicorn.org/).
  * **ASGI (Asynchronous Server Gateway Interface)**: Nowoczesny, **asynchroniczny** standard, który jest sercem FastAPI. Najszybszym i najczęściej używanym serwerem ASGI jest [**Uvicorn**](https://www.uvicorn.org/).

W praktyce, na produkcji często używa się Gunicorna do zarządzania procesami roboczymi (workerami) Uvicorna, aby połączyć solidne zarządzanie procesami z wysoką wydajnością operacji I/O.