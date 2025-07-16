# 2. Środowiska i Narzędzia: Profesjonalne Zarządzanie Projektem

> [!NOTE]
> Opanowanie narzędzi do zarządzania środowiskiem i zależnościami jest tak samo ważne, jak znajomość składni języka. W Pythonie, gdzie ekosystem bibliotek jest ogromny, izolacja zależności projektowych jest absolutnie kluczowa dla utrzymania porządku i zapewnienia reprodukowalności.

## Zarządzanie Środowiskami Wirtualnymi

> [!IMPORTANT]
> **Środowiska wirtualne to klucz do zarządzania zależnościami w projektach Python.** Każdy projekt powinien mieć swoje własne, izolowane środowisko z dedykowanym zestawem pakietów. Zapobiega to konfliktom wersji i tworzy przewidywalne środowisko uruchomieniowe.

---

### `venv` - Wbudowane Rozwiązanie Standardowe

`venv` to moduł dostarczany ze standardową biblioteką Pythona. Jest to najprostszy i najbardziej podstawowy sposób na tworzenie izolowanych środowisk.

**Typowy cykl pracy:**

1.  **Tworzenie środowiska** (np. w folderze o nazwie `myenv`):
    ```bash
    python -m venv <nazwa_środowiska, np. myenv>
    ```

2.  **Aktywacja środowiska:**
    ```bash
    # Windows (PowerShell/CMD)
    <nazwa_środowiska>\Scripts\activate

    # Linux / macOS
    source <nazwa_środowiska>/bin/activate
    ```

3.  **Instalacja pakietów** za pomocą menedżera `pip`:
    ```bash
    pip install pandas numpy
    ```

4.  **Zapisywanie zależności** do pliku `requirements.txt`:
    ```bash
    pip freeze > requirements.txt
    ```

> [!INFO]
> Plik `requirements.txt` jest standardowym sposobem na zarządzanie zależnościami w projektach Python. Jest to plik tekstowy, w którym zapisane są wszystkie zależności projektu, wraz z ich wersjami. Jest to przydatne, gdy chcemy zainstalować wszystkie zależności w jednym kroku, na przykład w środowisku produkcyjnym. Używamy wtedy instalatora `pip` z opcją `-r` (read from file), np. `pip install -r requirements.txt`.

---

### [Poetry](https://python-poetry.org/) - Nowoczesne Zarządzanie Zależnościami i Budowanie Projektu

> [!TIP]
> **Poetry to preferowane, nowoczesne rozwiązanie dla bibliotek i aplikacji produkcyjnych.** Automatycznie zarządza zależnościami, tworzy plik `pyproject.toml` (nowoczesny standard konfiguracji projektu) oraz `poetry.lock` (zapewniający deterministyczne instalacje), a także upraszcza publikowanie pakietów.

**Typowy cykl pracy:**

1.  **Tworzenie nowego projektu:**
    ```bash
    poetry new my-project
    cd my-project
    ```

2.  **Dodawanie zależności:** Poetry automatycznie doda je do pliku `pyproject.toml`.
    ```bash
    # Zależności produkcyjne
    poetry add pandas numpy

    # Zależności deweloperskie (np. do testowania i linterów)
    poetry add --dev pytest black
    ```

3.  **Instalacja zależności** z pliku `poetry.lock` (jeśli istnieje) lub `pyproject.toml`:
    ```bash
    poetry install
    ```

4.  **Uruchamianie skryptów** w wirtualnym środowisku zarządzanym przez Poetry:
    ```bash
    poetry run python your_script.py
    ```
    Lub aktywacja powłoki w tym środowisku:
    ```bash
    poetry shell
    ```

---

### [uv](https://docs.astral.sh/uv/) - Ultraszybki Menedżer Pakietów

`uv` to niezwykle szybki menedżer pakietów i instalator, napisany w języku Rust. Może być używany jako samodzielne narzędzie lub w połączeniu z innymi menedżerami. Jego główną zaletą jest ogromna wydajność – potrafi tworzyć środowiska i instalować pakiety **10-100x szybciej niż `pip` i `venv`**.

**Przykładowe użycie:**

```bash
# Instalacja uv
pip install uv

# Tworzenie środowiska wirtualnego (błyskawicznie)
uv venv

# Instalacja pakietów
uv pip install pandas numpy

# Synchronizacja środowiska z plikiem requirements.txt
uv pip sync requirements.txt
```

-----

## [Jupyter Notebooks](https://jupyter.org/) - Interaktywne Programowanie

> [!INFO]
> Jupyter Notebook to jedna z najpopularniejszych form pracy z Pythonem, szczególnie w data science, badaniach i nauczaniu. To interaktywne środowisko, gdzie kod, jego wyniki, wizualizacje i tekst (w formacie Markdown) współistnieją w jednym dokumencie (`.ipynb`).

Notebooki pozwalają na wykonywanie kodu w małych, niezależnych fragmentach (komórkach), co jest idealne do eksploracji danych i prototypowania algorytmów.

```python
# W notebooku każda komórka wykonuje się osobno

# Komórka 1: Import bibliotek
import pandas as pd
import matplotlib.pyplot as plt

# Komórka 2: Wczytanie i wyświetlenie danych
# Wynik (tabela) wyświetli się bezpośrednio pod komórką
data = pd.read_csv('sales.csv')
data.head()

# Komórka 3: Wygenerowanie i wyświetlenie wykresu
# Wykres pojawi się bezpośrednio pod komórką
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['revenue'])
plt.title('Przychody w czasie')
plt.show()
```

### Główne Środowiska Notebookowe:

  * **Jupyter Notebook / JupyterLab**: Klasyczne, uruchamiane lokalnie w przeglądarce.
  * **Google Colab**: Darmowe notebooki w chmurze z dostępem do GPU i TPU od Google.
  * **VS Code**: Doskonałe, wbudowane wsparcie dla plików `.ipynb`, łączące zalety IDE i notebooka.
  * **Platformy chmurowe**: Databricks, Kaggle, Deepnote oferują zaawansowane, zespołowe środowiska notebookowe.

> [\!WARNING]
> Notebooki mogą prowadzić do problemów z reprodukowalnością kodu, ponieważ kolejność wykonywania komórek ma znaczenie. Dla kodu produkcyjnego, który ma być uruchamiany automatycznie, preferowaną formą są standardowe pliki `.py`.
