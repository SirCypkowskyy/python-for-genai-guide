# 1. Filozofia i Podstawy: Zrozumienie "Dlaczego" w Pythonie

> [!TIP]
> Zrozumienie fundamentalnych różnic w filozofii projektowej między Pythonem a językami, które znasz, jest kluczem do szybkiego opanowania nowego narzędzia. Ta sekcja wyjaśnia, dlaczego pewne mechanizmy w Pythonie działają inaczej i jak wpływa to na codzienną pracę.

-----

## Polecane zasoby podstawowe

Poniższe materiały są absolutnie najlepszym punktem startowym dla osób zaczynających swoją przygodę z Pythonem. Co ważne, są one **całkowicie darmowe**.

#### Dokumentacja oficjalna
- **Python.org Tutorial**: https://docs.python.org/3/tutorial/index.html - Kompleksowy tutorial zaprojektowany dla doświadczonych programistów, zawiera 16 rozdziałów od podstaw po biblioteki standardowe. Istnieje też wersja w języku polskim: https://docs.python.org/pl/3/tutorial/index.html
- **Python for Beginners**: https://www.python.org/about/gettingstarted/ - Przewodnik startowy z listą tutoriali

#### Najlepsze kursy wideo
- **Corey Schafer**: https://www.youtube.com/@coreyms/ - Uznawany za najlepszy kanał Python na YouTube (1.28M subskrybentów), 140+ filmów o Python, Django, Flask
- **Programming with Mosh**: https://www.youtube.com/@programmingwithmosh/ - Profesjonalnie produkowane kursy z naciskiem na web development
- **Real Python**: https://realpython.com/start-here/ - Kompleksowa platforma z tutorialami, kursami wideo i quizami

#### Materiały porównawcze
- **Python vs C++ Comparison**: https://www.bitdegree.org/tutorials/python-vs-c-plus-plus - Szczegółowe porównanie z perspektywy programisty C++
- **Google's Python Class**: https://developers.google.com/edu/python - Darmowy kurs dla programistów z doświadczeniem

-----

## Kluczowe Różnice Filozoficzne

Przejście z C++ czy C# na Pythona to przede wszystkim zmiana sposobu myślenia. C++ optymalizuje czas wykonania przez maszynę, dając programiście pełną kontrolę. Python optymalizuje czas pracy dewelopera, stawiając na czytelność i szybkość tworzenia oprogramowania.

---

### Język Interpretowany vs. Kompilowany: Prawda leży pośrodku

Określenie Pythona jako języka "interpretowanego" jest uproszczeniem. W rzeczywistości standardowa implementacja (CPython) najpierw **kompiluje** kod źródłowy `.py` do formy pośredniej zwanej **bytecode** i zapisuje go w plikach `.pyc`. Ten bytecode jest następnie wykonywany przez **Maszynę Wirtualną Pythona (PVM)**.

* **Proces ten jest analogiczny do kompilacji C# do CIL (Common Intermediate Language) i wykonywania go przez CLR (.NET Runtime)**.
* Pliki `.pyc` są tworzone automatycznie, aby przyspieszyć ładowanie modułów przy kolejnych uruchomieniach.
* Główna różnica polega na tym, że cały proces jest ukryty i dzieje się w locie, co zapewnia błyskawiczny cykl deweloperski (edytuj -> uruchom) bez widocznego etapu kompilacji. Możemy też "na żywo" uruchamiać kod w interpreterze Python, co jest bardzo przydatne podczas debugowania.
* Konsekwencją jest to, że błędy typów są wykrywane dopiero w momencie wykonania danej linii kodu, a nie na etapie budowania projektu.

---

### Zarządzanie Pamięcią: Komfort i Bezpieczeństwo

To jedna z największych zmian podnoszących komfort pracy. W Pythonie zapominasz o manualnym zarządzaniu pamięcią – nie ma tu wskaźników, `new`/`delete` ani `malloc`/`free`.

* Główny mechanizm to **zliczanie referencji (reference counting)**. Każdy obiekt w pamięci ma licznik, który śledzi, ile zmiennych (nazw) na niego wskazuje. Gdy licznik spada do zera, obiekt jest usuwany.
* Dodatkowo **Garbage Collector (GC)** posiada mechanizmy do wykrywania i usuwania cyklicznych odwołań, z którymi sam licznik referencji by sobie nie poradził.
* Dla dewelopera oznacza to koniec zmartwień o wycieki pamięci (`memory leaks`) czy wiszące wskaźniki (`dangling pointers`), co eliminuje całą klasę trudnych błędów.
* Ceną za tę wygodę jest pewien narzut wydajnościowy i mniejsza kontrola nad układem danych w pamięci.

---

### Model Parametrów: "Pass-by-Object-Reference"

Python nie używa ani klasycznego "przekazywania przez wartość", ani "przekazywania przez referencję". Stosuje model, który najtrafniej określa się jako **"pass-by-object-reference"** lub "pass-by-assignment".

Zachowanie zależy od tego, czy przekazywany obiekt jest **mutowalny** (np. `list`, `dict`), czy **niemutowalny** (np. `int`, `str`, `tuple`).

#### Przykład z obiektem mutowalnym (efekt jak `pass-by-reference`):

Gdy modyfikujesz obiekt mutowalny wewnątrz funkcji, zmiany są widoczne na zewnątrz, ponieważ zarówno zewnętrzna, jak i wewnętrzna zmienna wskazują na ten sam obiekt w pamięci.

```python
def modify_list(my_list: list):
    # Modyfikujemy ORYGINALNY obiekt w miejscu
    my_list.append(4)

data = [1, 2, 3]
print(f"Przed wywołaniem: {data}") # -> [1, 2, 3]
modify_list(data)
print(f"Po wywołaniu:    {data}") # -> [1, 2, 3, 4]
```

#### Przykład z obiektem niemutowalnym (efekt jak `pass-by-value`):

Próba "modyfikacji" obiektu niemutowalnego (np. przez `+ 1`) w rzeczywistości tworzy **nowy obiekt**. Lokalna zmienna wewnątrz funkcji zaczyna wskazywać na ten nowy obiekt, ale oryginalna zmienna na zewnątrz pozostaje nietknięta.

```python
def reassign_number(my_number: int):
    # my_number = my_number + 1 tworzy NOWY obiekt int
    # i przypisuje go do lokalnej nazwy my_number
    my_number += 1

num = 10
print(f"Przed wywołaniem: {num}") # -> 10
reassign_number(num)
print(f"Po wywołaniu:    {num}") # -> 10
```

-----

## System Typów w Praktyce

### Dynamiczne Typowanie vs. `auto` w C++

W Pythonie typ jest powiązany z obiektem, a nie ze zmienną. Zmienna jest tylko etykietą, którą można w każdej chwili "przekleić" na inny obiekt, nawet innego typu.

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

## Podstawowe Struktury Danych: Odpowiedniki z C++ i C#

Twoja znajomość kontenerów z biblioteki STL (Standard Template Library) oraz .NET (C#) jest w pełni transferowalna. Python oferuje wbudowane, niezwykle wydajne i elastyczne odpowiedniki.

| Typ w Pythonie | Odpowiednik w C++ | Odpowiednik w C# | Kluczowe Cechy i Różnice |
| :--- | :--- | :--- | :--- |
| `list` | `std::vector` | `List<T>` | Dynamiczna, mutowalna tablica mogąca przechowywać elementy **dowolnych typów**. Pozwala na szybkie dodawanie/usuwanie elementów na końcu. Bardzo uniwersalna, wykorzystywana niemal wszędzie. |
| `tuple` | `std::pair` / `std::tuple` | `Tuple<T1, T2,...>` / `ValueTuple<T1, T2,...>` | **Niemutowalna** (niezmienna) sekwencja dowolnych obiektów. Idealna do zwracania wielu wartości z funkcji lub jako klucz w słowniku. |
| `dict` | `std::map` / `std::unordered_map` | `Dictionary<TKey, TValue>` | Słownik (hash table) – klucz-wartość, bardzo szybki dostęp (O(1)), klucze mogą być dowolnego niemutowalnego typu. Od Pythona 3.7 zachowuje kolejność wstawiania. |
| `set` | `std::set` / `std::unordered_set` | `HashSet<T>` | Mutowalny zbiór **unikalnych** elementów, nieuporządkowany. Bardzo szybkie operacje na zbiorach (suma, przecięcie, różnica). |
| `str` | `std::string` | `string` | **Niemutowalny** łańcuch znaków Unicode. Każda operacja "modyfikująca" tworzy nowy obiekt. Bardzo bogaty zestaw metod do przetwarzania tekstu. |

## Programowanie obiektowe

### Wielodziedziczenie i MRO (Method Resolution Order)
Python wspiera **wielodziedziczenie** z inteligentnym algorytmem MRO (ang. *"Method Resolution Order"*), który rozwiązuje konflikty metodami.

```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):  # Wielodziedziczenie (ang. *"Multiple Inheritance"*)
    pass

d = D()
d.method()  # Wypisze "B method" - MRO: D -> B -> C -> A
```

### Klasy abstrakcyjne z modułem abc
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
```
