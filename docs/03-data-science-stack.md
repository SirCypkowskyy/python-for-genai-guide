# 3. Stos Technologiczny Data Science: Praca z Danymi w Praktyce

> [!NOTE]
> Python jest de facto standardem w świecie Data Science. Jego siła tkwi w dojrzałym ekosystemie bibliotek, które sprawiają, że złożone operacje na danych, analiza statystyczna i wizualizacja stają się intuicyjne i wydajne. Twoje dotychczasowe doświadczenie, szczególnie w SQL, da Ci ogromną przewagę w opanowaniu tych narzędzi.

---

## 🐼 [Pandas](https://pandas.pydata.org/): "SQL na sterydach w Pythonie"

[**Pandas**](https://pandas.pydata.org/) to absolutnie fundamentalna biblioteka do analizy i manipulacji danymi w Pythonie. Jeżeli Twoim głównym narzędziem do pracy z danymi był do tej pory SQL, poczujesz się tu jak w domu, ale z dodatkowymi "supermocami". Główną strukturą danych w Pandas jest **`DataFrame`**, który można traktować jak programowalną, trzymaną w pamięci tabelę SQL.

Operacje, które znasz z codziennej pracy z bazami danych – `SELECT`, `WHERE`, `GROUP BY`, `JOIN` – mają swoje bezpośrednie, ekspresyjne odpowiedniki w metodach Pandas.

### Podstawowe Operacje na DataFrame

Oto jak typowe zadania analityczne przekładają się na kod Pandas:

* **Wczytywanie danych (`SELECT * FROM ...`)**: Pandas potrafi wczytywać dane z wielu formatów, najczęściej z plików CSV, Excel, czy bezpośrednio z bazy danych SQL.
    ```python
    import pandas as pd

    # Wczytanie danych z pliku CSV do obiektu DataFrame
    # Jest to odpowiednik załadowania tabeli do pamięci
    df = pd.read_csv('data.csv')
    ```

* **Filtrowanie (`WHERE`)**: Możesz filtrować wiersze w DataFrame używając intuicyjnej składni, która przypomina operacje wektorowe.
    ```python
    # Wybierz wiersze, gdzie wiek (age) jest większy niż 25
    filtered_df = df[df['age'] > 25]
    ```

* **Grupowanie (`GROUP BY`)**: Agregacja danych to jedna z najmocniejszych stron Pandas. Metoda `.groupby()` jest niezwykle elastyczna.
    ```python
    # Oblicz średnią pensję (salary) dla każdego działu (department)
    avg_salary_by_dept = df.groupby('department')['salary'].mean()
    ```

* **Łączenie danych (`JOIN`)**: Pandas oferuje funkcję `pd.merge()`, która pozwala na wykonywanie wszystkich typów złączeń znanych z SQL (`LEFT`, `RIGHT`, `INNER`, `OUTER`).
    ```python
    # Wykonaj lewe złączenie (left join) na podstawie kolumny 'id'
    merged_df = pd.merge(df1, df2, on='id', how='left')
    ```

### Przykład Porównawczy: SQL vs Pandas

Wyobraź sobie, że chcesz wykonać następujące zapytanie analityczne w SQL.

**Zapytanie SQL:**
```sql
SELECT
    region,
    SUM(revenue) as total_revenue
FROM
    sales
WHERE
    revenue > 1000
GROUP BY
    region
ORDER BY
    total_revenue DESC;
```

**Odpowiednik w Pandas:**
Ten sam rezultat można osiągnąć w Pandas za pomocą czytelnego łańcucha operacji, który jest nie tylko wydajny, ale i łatwy do debugowania.

```python
import pandas as pd

# Wczytanie danych (analogiczne do FROM sales)
df = pd.read_csv('sales.csv')

# Łańcuch operacji, który krok po kroku transformuje dane
result = (
    df[df['revenue'] > 1000]  # Krok 1: Analogia do klauzuli WHERE
    .groupby('region')        # Krok 2: Analogia do GROUP BY
    .agg(total_revenue=('revenue', 'sum')) # Krok 3: Analogia do SUM(...) z aliasem
    .sort_values(by='total_revenue', ascending=False) # Krok 4: Analogia do ORDER BY
)

print(result)
```

Pandas doskonale integruje się z całym ekosystemem Pythona, pozwalając płynnie przechodzić od analizy danych do ich wizualizacji czy wykorzystania w modelach machine learning.

-----

## 🔢 [NumPy](https://numpy.org/): Fundament Obliczeń Naukowych

[**NumPy (Numerical Python)**](https://numpy.org/) to biblioteka, na której zbudowana jest praktycznie cała naukowa część ekosystemu Pythona, włączając w to Pandas. Jej rdzeń napisany jest w skompilowanych językach C i Fortran, co zapewnia ogromną wydajność operacji numerycznych, porównywalną z wyspecjalizowanymi bibliotekami do algebry liniowej jak [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) czy [LAPACK](https://en.wikipedia.org/wiki/LAPACK).

  * Głównym obiektem w NumPy jest `ndarray` – potężna, wielowymiarowa tablica przechowująca dane **jednego typu**.
  * Kluczową ideą pracy z NumPy jest **wektoryzacja** – wykonywanie operacji na całych tablicach zamiast na pojedynczych elementach w pętlach, co jest znacznie szybsze.

-----

## ✅ [Pydantic](https://docs.pydantic.dev/): Gwarancja Jakości Danych w Runtime

Dla dewelopera przyzwyczajonego do statycznego typowania, [**Pydantic**](https://docs.pydantic.dev/) jest jak powiew świeżego powietrza. Wprowadza porządek i bezpieczeństwo typów do dynamicznego świata Pythona. Jest to nowoczesna biblioteka służąca do **walidacji danych i zarządzania ustawieniami** przy użyciu standardowych wskazówek typów (`type hints`).

Definiujesz schemat danych jako klasę dziedziczącą po `BaseModel`, a Pydantic automatycznie:

1.  Sparsuje dane wejściowe (np. z JSON).
2.  Zwaliduje je pod kątem zdefiniowanych typów i ograniczeń.
3.  Przekonwertuje na poprawnie otypowany obiekt Pythona.
4.  W razie niezgodności rzuci czytelne, szczegółowe błędy.

<!-- end list -->

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    email: EmailStr # Pydantic ma wbudowane typy specjalne, np. do walidacji e-maili

# Pydantic automatycznie skonwertuje string "30" na int
# i zweryfikuje poprawność adresu email.
user_data = {"name": "John Doe", "age": "30", "email": "john.doe@example.com"}
user = User.model_validate(user_data)

print(user.age) # -> 30 (już jako int)
```

Pydantic jest absolutnie kluczowym narzędziem przy budowie solidnych API (jest sercem **FastAPI**) oraz niezawodnych pipeline'ów przetwarzania danych.

-----

## 📈 [Wizualizacja Danych](https://matplotlib.org/): Opowiadanie Historii

Surowe liczby rzadko kiedy opowiadają całą historię. Ekosystem Pythona oferuje bogaty zestaw narzędzi do wizualizacji, które pomogą Ci zrozumieć dane i zaprezentować wyniki.

  * [**Matplotlib**](https://matplotlib.org/): To podstawowa, niskopoziomowa biblioteka do tworzenia wykresów, stanowiąca fundament dla wielu innych narzędzi. Daje Ci pełną, granularną kontrolę nad każdym aspektem wykresu, ale przez to bywa "gadatliwa" (wymaga więcej kodu do osiągnięcia prostego efektu). Można ją traktować jak "C++ świata wizualizacji" lub odpowiednik `pyplot` z MATLABa.

  * [**Seaborn**](https://seaborn.pydata.org/): To wysokopoziomowe API zbudowane na bazie Matplotlib. Jego celem jest tworzenie estetycznych i informatywnych **wykresów statystycznych** przy użyciu znacznie mniejszej ilości kodu. Jest idealny do szybkiej eksploracji danych.

  * [**Plotly**](https://plotly.com/python/): Jeśli potrzebujesz **interaktywnych wizualizacji**, Plotly jest najlepszym wyborem. Pozwala tworzyć wykresy, na których użytkownik może przesuwać widok, powiększać, czy wyświetlać dodatkowe informacje po najechaniu myszką, przez wykorzystanie interfejsu webowego. To czyni go idealnym narzędziem do budowy dashboardów i aplikacji webowych.
