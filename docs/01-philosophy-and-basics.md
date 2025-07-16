# 1. Filozofia i Podstawy: Zrozumienie "Dlaczego" w Pythonie

> [!TIP]
> Zrozumienie fundamentalnych różnic w filozofii projektowej między Pythonem a językami, które znasz, jest kluczem do szybkiego opanowania nowego narzędzia. Ta sekcja wyjaśnia, dlaczego pewne mechanizmy w Pythonie działają inaczej i jak wpływa to na codzienną pracę.

---

## Kluczowe Różnice Filozoficzne

Przejście z C++ czy C# na Pythona to przede wszystkim zmiana sposobu myślenia. C++ optymalizuje czas wykonania przez maszynę, dając programiście pełną kontrolę. Python optymalizuje czas pracy dewelopera, stawiając na czytelność i szybkość tworzenia oprogramowania.

### Język Interpretowany vs. Kompilowany: Prawda leży pośrodku

Określenie Pythona jako języka "interpretowanego" jest uproszczeniem. W rzeczywistości standardowa implementacja (CPython) najpierw **kompiluje** kod źródłowy `.py` do formy pośredniej zwanej **bytecode** i zapisuje go w plikach `.pyc`. Ten bytecode jest następnie wykonywany przez **Maszynę Wirtualną Pythona (PVM)**.

* **Proces ten jest analogiczny do kompilacji C# do CIL (Common Intermediate Language) i wykonywania go przez CLR (.NET Runtime)**.
* Pliki `.pyc` są tworzone automatycznie, aby przyspieszyć ładowanie modułów przy kolejnych uruchomieniach.
* Główna różnica polega na tym, że cały proces jest ukryty i dzieje się w locie, co zapewnia błyskawiczny cykl deweloperski (edytuj -> uruchom) bez widocznego etapu kompilacji. Możemy też "na żywo" uruchamiać kod w interpreterze Python, co jest bardzo przydatne podczas debugowania.
* Konsekwencją jest to, że błędy typów są wykrywane dopiero w momencie wykonania danej linii kodu, a nie na etapie budowania projektu.

### Zarządzanie Pamięcią: Komfort i Bezpieczeństwo

To jedna z największych zmian podnoszących komfort pracy. W Pythonie zapominasz o manualnym zarządzaniu pamięcią – nie ma tu wskaźników, `new`/`delete` ani `malloc`/`free`.

* Główny mechanizm to **zliczanie referencji (reference counting)**. Każdy obiekt w pamięci ma licznik, który śledzi, ile zmiennych (nazw) na niego wskazuje. Gdy licznik spada do zera, obiekt jest usuwany.
* Dodatkowo **Garbage Collector (GC)** posiada mechanizmy do wykrywania i usuwania cyklicznych odwołań, z którymi sam licznik referencji by sobie nie poradził.
* Dla dewelopera oznacza to koniec zmartwień o wycieki pamięci (`memory leaks`) czy wiszące wskaźniki (`dangling pointers`), co eliminuje całą klasę trudnych błędów.
* Ceną za tę wygodę jest pewien narzut wydajnościowy i mniejsza kontrola nad układem danych w pamięci.

### Znaczące Wcięcia (Indentation): Koniec z Nawiasami Klamrowymi

Python używa wcięć (standardowo 4 spacje) do definiowania bloków kodu. To jedna z najbardziej charakterystycznych cech. Zastępuje to nawiasy klamrowe `{}` znane z C++/C#.

```python
# C++/C#
# if (wiek > 18) {
#     printf("Pełnoletni");
#     // inne operacje
# }

# Python
wiek = 18
if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    print("Nie jesteś jeszcze pełnoletni.")
```

**Zalety**: Wymusza czysty i spójny styl kodu w całym ekosystemie.
**Wady**: Początkowo może być źródłem błędów (`IndentationError`), zwłaszcza przy kopiowaniu kodu. Dobre IDE (jak VS Code czy PyCharm) rozwiązuje ten problem.

### Model Parametrów: "Pass-by-Object-Reference"

Python nie używa ani klasycznego "przekazywania przez wartość", ani "przekazywania przez referencję". Stosuje model, który najtrafniej określa się jako **"pass-by-object-reference"** lub "pass-by-assignment".

Zachowanie zależy od tego, czy przekazywany obiekt jest **mutowalny** (np. `list`, `dict`), czy **niemutowalny** (np. `int`, `str`, `tuple`).

#### Przykład z obiektem mutowalnym (efekt jak `pass-by-reference`):

Gdy modyfikujesz obiekt mutowalny wewnątrz funkcji, zmiany są widoczne na zewnątrz, ponieważ zarówno zewnętrzna, jak i wewnętrzna zmienna wskazują na ten sam obiekt w pamięci.

```python
def modify_list(my_list: list):
    # Modyfikujemy ORYGINALNY obiekt w miejscu
    my_list.append(4)
    print(f"  Wewnątrz funkcji, id: {id(my_list)}")

data = [1, 2, 3]
print(f"Przed wywołaniem: {data}, id: {id(data)}")
modify_list(data)
print(f"Po wywołaniu:    {data}, id: {id(data)}") # -> [1, 2, 3, 4]
```

#### Przykład z obiektem niemutowalnym (efekt jak `pass-by-value`):

Próba "modyfikacji" obiektu niemutowalnego (np. przez `+ 1`) w rzeczywistości tworzy **nowy obiekt**. Lokalna zmienna wewnątrz funkcji zaczyna wskazywać na ten nowy obiekt, ale oryginalna zmienna na zewnątrz pozostaje nietknięta.

```python
def reassign_number(my_number: int):
    # my_number = my_number + 1 tworzy NOWY obiekt int
    # i przypisuje go do lokalnej nazwy my_number
    my_number += 1
    print(f"  Wewnątrz funkcji, id: {id(my_number)}")


num = 10
print(f"Przed wywołaniem: {num}, id: {id(num)}")
reassign_number(num)
print(f"Po wywołaniu:    {num}, id: {id(num)}") # -> 10
```

-----

## System Typów w Praktyce

### Dynamiczne Typowanie vs. `auto` w C++

W Pythonie typ jest powiązany z obiektem, a nie ze zmienną. Zmienna jest tylko "pojemnikiem" lub etykietą, którą można w każdej chwili "przekleić" na inny obiekt, nawet innego typu. **W przeciwieństwie do większości innych języków programowania, w Pythonie nie musimy deklarować typu zmiennej**.

```python
# Python
x = 10          # x jest teraz etykietą dla obiektu typu int
x = "hello"     # teraz x jest etykietą dla obiektu typu str
x = [1, 2, 3]   # a teraz dla obiektu typu list
```

Porównanie do `auto` w C++ jest pomocne, ale z kluczową różnicą: `auto` w C++ dedukuje typ w czasie kompilacji i ten typ staje się stały dla danej zmiennej. W Pythonie typ jest sprawdzany dynamicznie w czasie wykonania.

### Wskazówki Typów (`Type Hints`)

> [!TIP]
> Dla dewelopera przyzwyczajonego do języków typowanych statycznie, używanie **type hints** jest **zdecydowanie rekomendowane**.

Python pozwala na dodawanie opcjonalnych wskazówek typów, które nie wpływają na wykonanie kodu (interpreter je ignoruje), ale są nieocenione dla narzędzi do statycznej analizy (jak `mypy`, czy rekomendowany przeze mnie `pyright`), edytorów kodu (lepsze autouzupełnianie) i czytelności.

```python
def calculate_price(quantity: int, price: float) -> float:
    return quantity * price
```

-----

## Podstawowe Struktury Danych: Odpowiedniki z C++ i C\#

Twoja znajomość kontenerów z biblioteki STL (Standard Template Library) oraz .NET (C\#) jest w pełni transferowalna. Python oferuje wbudowane, niezwykle wydajne i elastyczne odpowiedniki.

| Typ w Pythonie | Odpowiednik w C++ | Odpowiednik w C\# | Kluczowe Cechy i Różnice |
| :--- | :--- | :--- | :--- |
| `list` | `std::vector` | `List<T>` | Dynamiczna, **mutowalna** tablica mogąca przechowywać elementy **dowolnych typów**. Pozwala na szybkie dodawanie/usuwanie elementów na końcu (`append`, `pop`). Bardzo uniwersalna, wykorzystywana niemal wszędzie. |
| `tuple` | `std::pair` / `std::tuple` | `Tuple<T1, T2,...>` / `ValueTuple<T1, T2,...>` | **Niemutowalna** (niezmienna) sekwencja dowolnych obiektów. Idealna do zwracania wielu wartości z funkcji lub jako klucz w słowniku. Zajmuje mniej pamięci niż lista. |
| `dict` | `std::map` / `std::unordered_map` | `Dictionary<TKey, TValue>` | Słownik (mapa hashowana) – klucz-wartość, bardzo szybki dostęp (uśredniony O(1)). Klucze muszą być typu niemutowalnego. Od Pythona 3.7 zachowuje kolejność wstawiania. |
| `set` | `std::set` / `std::unordered_set` | `HashSet<T>` | **Mutowalny** zbiór **unikalnych**, niemutowalnych elementów. Nieuporządkowany. Oferuje bardzo szybkie operacje teoriomnogościowe (suma `|`, iloczyn `&`, różnica `-`). |
| `str` | `std::string` | `string` | **Niemutowalny** łańcuch znaków Unicode. Każda operacja "modyfikująca" (np. konkatenacja) tworzy nowy obiekt. Posiada bogaty zestaw metod do przetwarzania tekstu. |

-----

## Programowanie Obiektowe

### `__init__` i `self`

W Pythonie konstruktor to specjalna metoda `__init__`. Pierwszy argument każdej metody instancji to, z konwencji, `self`. Jest to jawny odpowiednik wskaźnika `this` z C++ czy C#.

```python
class KontoBankowe:
    # Metoda __init__ to konstruktor
    def __init__(self, wlasciciel: str, saldo_poczatkowe: float = 0.0):
        # self odnosi się do konkretnej instancji
        self.wlasciciel = wlasciciel
        self.saldo = saldo_poczatkowe

    def wplata(self, kwota: float):
        self.saldo += kwota
        print(f"Wpłacono {kwota}. Nowe saldo: {self.saldo}")
```

### Wielodziedziczenie i MRO (Method Resolution Order)

Python wspiera **wielodziedziczenie** z inteligentnym algorytmem MRO (ang. *"Method Resolution Order"*), który rozwiązuje konflikty, określając jednoznaczną kolejność przeszukiwania klas bazowych w poszukiwaniu metody.

```python
class Pracownik:
    def __init__(self, pensja):
        self.pensja = pensja
    
    def info_praca(self):
        return f"Zarabiam {self.pensja} PLN miesięcznie."

class Student:
    def __init__(self, kierunek):
        self.kierunek = kierunek
    
    def info_studia(self):
        return f"Studiuję kierunek {self.kierunek}."

class StudentPracujacy(Student, Pracownik):  # Wielodziedziczenie
    def __init__(self, imie, kierunek, pensja):
        Student.__init__(self, kierunek)
        Pracownik.__init__(self, pensja)
        self.imie = imie
    
    def przedstaw_sie(self):
        return f"Jestem {self.imie}. {self.info_studia()} {self.info_praca()}"
```

### Enkapsulacja: Konwencja zamiast Wymuszenia

Python nie ma słów kluczowych `public`, `private` czy `protected`. Zamiast tego stosuje konwencje nazewnicze:

  * `_atrybut`: Traktowany jako "chroniony". Deweloperzy wiedzą, że nie powinni go używać poza klasą lub jej podklasami.
  * `__atrybut`: Traktowany jako "prywatny". Python stosuje tzw. **name mangling**, zmieniając nazwę na `_NazwaKlasy__atrybut`, co utrudnia przypadkowy dostęp.

<!-- end list -->

```python
class KontoBankowe:
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel  # publiczny
        self._historia = []  # chroniony
        self.__saldo = saldo  # prywatny

    def sprawdz_saldo(self):
        # Dostęp do prywatnego atrybutu wewnątrz klasy
        return self.__saldo
```

### Klasy Abstrakcyjne z modułem `abc`

Python implementuje klasy abstrakcyjne za pomocą modułu `abc`, który pozwala definiować metody, które *muszą* być zaimplementowane przez klasy pochodne. Zapobiega to tworzeniu instancji klas, które nie są w pełni zdefiniowane.

```python
from abc import ABC, abstractmethod

class InstrumentFinansowy(ABC):
    def __init__(self, nazwa, wartosc):
        self.nazwa = nazwa
        self.wartosc = wartosc

    @abstractmethod
    def oblicz_ryzyko(self):
        pass

class Akcja(InstrumentFinansowy):
    def oblicz_ryzyko(self):
        return "Wysokie"
```

-----

## Praca z Plikami

### Podstawowe Operacje na Plikach i Menedżer Kontekstu `with`

Blok `with` to zalecany sposób pracy z plikami w Pythonie, który zapewnia automatyczne zamykanie plików nawet w przypadku wystąpienia błędów.

```python
# Zapis do pliku (nadpisuje istniejący plik)
with open("wyniki.txt", "w", encoding="utf-8") as plik:
    plik.write("To jest przykładowy tekst.\n")
    plik.write("To jest druga linia tekstu.")

# Odczyt pliku
with open("wyniki.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        print(linia.strip()) # strip() usuwa białe znaki, jak '\n'
```

Tryby otwarcia pliku: `r` (odczyt), `w` (zapis), `a` (dopisywanie), `+` (np. `r+` do odczytu i zapisu), `b` (tryb binarny).

### Praca z Plikami CSV

Moduł `csv` ułatwia pracę z plikami Comma-Separated Values, automatycznie obsługując separatory i cudzysłowy. `DictReader` i `DictWriter` pozwalają na pracę z wierszami jako słownikami.

```python
import csv

# Zapis do CSV za pomocą DictWriter
with open("dane.csv", "w", encoding="utf-8", newline='') as plik:
    naglowki = ["imie", "nazwisko", "wiek"]
    pisarz = csv.DictWriter(plik, fieldnames=naglowki)
    pisarz.writeheader()
    pisarz.writerow({"imie": "Jan", "nazwisko": "Kowalski", "wiek": "35"})

# Odczyt z CSV za pomocą DictReader
with open("dane.csv", "r", encoding="utf-8") as plik:
    czytnik = csv.DictReader(plik)
    for wiersz in czytnik:
        print(wiersz['imie'], wiersz['nazwisko'])
```

### Praca z Plikami JSON

Python posiada wbudowaną bibliotekę `json` do serializacji i deserializacji danych w tym popularnym formacie.

```python
import json

dane_python = {'imie': 'Anna', 'wiek': 28, 'hobby': ['sport', 'książki']}

# Zapis do pliku JSON
with open('dane.json', 'w', encoding='utf-8') as f:
    json.dump(dane_python, f, ensure_ascii=False, indent=2)

# Odczyt z pliku JSON
with open('dane.json', 'r', encoding='utf-8') as f:
    wczytane_dane = json.load(f)
    print(wczytane_dane['hobby'])
```

-----

## Obsługa Błędów i Debugowanie

### Obsługa Wyjątków: `try...except`

Blok `try...except` pozwala na elegancką obsługę błędów, które mogą wystąpić w trakcie działania programu, zapobiegając jego awarii.

```python
try:
    wiek_tekst = input("Podaj swój wiek: ")
    wiek = int(wiek_tekst)
    print(f"Za 10 lat będziesz miał {wiek + 10} lat.")
except ValueError:
    print("Błąd: Wprowadzona wartość nie jest poprawną liczbą.")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
finally:
    print("Ten blok wykona się zawsze, na koniec.")
```

**Najczęstsze wyjątki**: `FileNotFoundError`, `PermissionError`, `TypeError`, `ValueError`, `NameError`, `IndexError`, `KeyError`.

### Debugowanie

Debugowanie to proces znajdowania i naprawiania błędów.

  * **Prosta technika**: Używanie `print()` do śledzenia wartości zmiennych w różnych punktach programu.
  * **Analiza śladu błędu (traceback)**: Python w razie błędu wyświetla ślad, który należy czytać od dołu do góry, aby zlokalizować linię i typ błędu.
  * **Debuggery**: Zaawansowane narzędzia (wbudowane w IDE jak PyCharm, VS Code lub `pdb` w terminalu) pozwalają na zatrzymywanie wykonania programu, inspekcję zmiennych i śledzenie krok po kroku.

-----

## Wprowadzenie do Ekosystemu Pythona

Python to nie tylko język, ale potężny ekosystem bibliotek do różnorodnych zastosowań.

### Analiza Danych z `pandas`

Pandas to kluczowa biblioteka do manipulacji i analizy danych. Jej podstawowe struktury to `Series` (jednowymiarowa) i `DataFrame` (dwuwymiarowa, jak tabela).

```python
import pandas as pd

# Tworzenie DataFrame
data = {'Kraj': ['Polska', 'Niemcy', 'Francja'], 'PKB (mld USD)': [674, 4223, 3049]}
df = pd.DataFrame(data)

# Podstawowe operacje
print(df.describe())  # Statystyki opisowe
print(df[df['PKB (mld USD)'] > 1000]) # Filtrowanie
```

### Wizualizacja Danych z `matplotlib` i `plotly`

  * **Matplotlib**: Standardowa biblioteka do tworzenia statycznych wykresów wysokiej jakości.
  * **Plotly**: Służy do tworzenia interaktywnych wykresów, idealnych do aplikacji webowych i dashboardów.

<!-- end list -->

```python
import matplotlib.pyplot as plt

df.plot(kind='bar', x='Kraj', y='PKB (mld USD)', title='PKB w wybranych krajach')
plt.ylabel('mld USD')
plt.show()
```

### Tworzenie Aplikacji Webowych z `Flask` i `Django`

  * **Flask**: Mikro-framework, elastyczny i prosty, idealny do małych projektów i API.
  * **Django**: "Baterie w zestawie", kompleksowy framework do budowy dużych, skalowalnych aplikacji webowych.

### Tworzenie Gier z `pygame`

Pygame to popularna biblioteka do tworzenia gier 2D, która obsługuje grafikę, dźwięk i obsługę zdarzeń.

### Uczenie Maszynowe

  * **Scikit-learn**: Podstawowa biblioteka do klasycznego uczenia maszynowego (klasyfikacja, regresja, klasteryzacja).
  * **Keras / TensorFlow / PyTorch**: Zaawansowane frameworki do budowy i trenowania głębokich sieci neuronowych.
  * **LangChain**: Framework ułatwiający tworzenie aplikacji opartych na dużych modelach językowych (LLM).