# 7. Słowniczek Pojęć

> [!NOTE]
> Ten słowniczek to Twoja podręczna encyklopedia terminów, które napotkasz w ekosystemie Pythona. Został podzielony na kategorie tematyczne, aby ułatwić nawigację. Używaj go, aby szybko sprawdzić nieznane pojęcia i ugruntować swoją wiedę.

---

## Podstawowe pojęcia Python

**ASGI (Asynchronous Server Gateway Interface)**
: Nowoczesny, asynchroniczny standard komunikacji między serwerem a aplikacją webową w Pythonie. Jest następcą WSGI i został zaprojektowany do obsługi dużej liczby jednoczesnych połączeń I/O, co jest kluczowe dla aplikacji czasu rzeczywistego, WebSockets i wysokowydajnych API. Używany przez frameworki takie jak FastAPI.

**Batteries-Included**
: Filozofia projektowania frameworków (np. Django), która polega na dostarczaniu wbudowanych, zintegrowanych rozwiązań dla większości typowych problemów, takich jak ORM, panel admina, autentykacja czy system szablonów.

**Bytecode**
: Pośrednia, niezależna od platformy forma kodu, na którą kompilowany jest kod źródłowy Pythona (.py). Nie jest to kod maszynowy, ale zestaw instrukcji dla Maszyny Wirtualnej Pythona (PVM), która go interpretuje i wykonuje. Pliki z bytecodem mają rozszerzenie `.pyc`.

**Context Manager**
: Obiekt, który zarządza zasobami poprzez zdefiniowanie metod `__enter__` i `__exit__`. Używany jest z instrukcją `with`, co gwarantuje, że zasób (np. plik, połączenie sieciowe) zostanie poprawnie zwolniony, nawet jeśli w bloku `with` wystąpi błąd. Najczęstszy przykład to `with open('file.txt') as f:`.

**Decorator**
: Funkcja, która przyjmuje inną funkcję jako argument, dodaje do niej pewną funkcjonalność, i zwraca zmodyfikowaną funkcję, nie zmieniając jej oryginalnego kodu. Składnia z `@` jest tzw. "cukrem składniowym". Przykłady to `@staticmethod`, `@property` czy dekoratory we frameworkach webowych (`@app.route('/'))`.

**Duck Typing**
: Filozofia programowania, która nie skupia się na jawnym typie obiektu, ale na jego metodach i właściwościach. Jej nazwa pochodzi od powiedzenia: "If it walks like a duck and quacks like a duck, it must be a duck". W praktyce oznacza to, że funkcja będzie próbowała wywołać na obiekcie potrzebne metody, nie sprawdzając, czy jest on instancją konkretnej klasy.

**GIL (Global Interpreter Lock)**
: Mechanizm w standardowej implementacji Pythona (CPython), który pozwala tylko jednemu wątkowi na wykonywanie bytecodu Pythona w danym momencie w ramach jednego procesu. Upraszcza zarządzanie pamięcią i zapobiega konfliktom, ale ogranicza rzeczywistą równoległość w programach wielowątkowych, które są mocno obciążone obliczeniami CPU.

**Generator**
: Specjalny typ iteratora, zdefiniowany jako funkcja używająca słowa kluczowego `yield`. Generatory produkują wartości "na żądanie", jedna po drugiej, zamiast tworzyć od razu całą kolekcję w pamięci. Jest to niezwykle wydajne pamięciowo przy pracy z dużymi zbiorami danych.

**Immutable (Niemutowalny)**
: Typ obiektu, którego stanu nie można zmienić po jego utworzeniu. Każda operacja, która wygląda jak modyfikacja, w rzeczywistości tworzy nowy obiekt w pamięci. Przykłady to `int`, `float`, `str`, `tuple`.

**Interpreter**
: Program, który wykonuje kod Python linia po linii, bez wcześniejszego etapu kompilacji do kodu maszynowego. W przypadku CPythona, interpreter w rzeczywistości wykonuje bytecode.

**List Comprehension**
: Zwięzły, czytelny i "pythonowy" sposób tworzenia list na podstawie istniejących sekwencji. Jest to często bardziej wydajna i preferowana alternatywa dla pętli `for` z metodą `.append()`. Przykład: `squares = [x**2 for x in range(10)]`.

**MRO (Method Resolution Order)**
: Algorytm określający kolejność, w jakiej Python przeszukuje hierarchię klas bazowych w poszukiwaniu metody do wywołania. Jest to kluczowe przy wielodziedziczeniu, gdzie rozwiązuje potencjalne konflikty (jak "problem diamentowy") w sposób deterministyczny.

**Mutable (Mutowalny)**
: Typ obiektu, którego stan można zmienić w miejscu (ang. *in-place*) po jego utworzeniu. Zmiany dokonane na obiekcie w jednym miejscu kodu będą widoczne we wszystkich innych miejscach, gdzie istnieją referencje do tego obiektu. Przykłady to `list`, `dict`, `set`.

**PVM (Python Virtual Machine)**
: Program, który jest sercem interpretera Pythona. Jego zadaniem jest wczytanie skompilowanego bytecodu i wykonanie zawartych w nim instrukcji.

**Pythonic**
: Określenie kodu, który jest napisany zgodnie z idiomami, konwencjami i filozofią języka Python. Taki kod jest zazwyczaj zwięzły, czytelny i wykorzystuje wbudowane mechanizmy języka (np. list comprehensions, context managers) zamiast implementować je w sposób znany z innych języków (np. pętle w stylu C).

**Type Hint (Wskazówka Typu)**
: Opcjonalna adnotacja w kodzie Pythona, która określa oczekiwany typ zmiennej, parametru funkcji lub wartości zwracanej. Interpreter Pythona ignoruje te wskazówki w czasie wykonania, ale są one używane przez narzędzia do analizy statycznej (np. `mypy`) i IDE w celu wczesnego wykrywania błędów i poprawy podpowiedzi.

**Virtual Environment (Środowisko Wirtualne)**
: Izolowane środowisko Pythona, które posiada własną instalację interpretera oraz niezależny zestaw pakietów. Pozwala to na unikanie konfliktów zależności między różnymi projektami na jednym komputerze.

**WSGI (Web Server Gateway Interface)**
: Tradycyjny, synchroniczny standard komunikacji między serwerem a aplikacją webową w Pythonie. Używany przez frameworki takie jak Django i Flask.

---

## Data Science

**DataFrame**
: Podstawowa, dwuwymiarowa, tabelaryczna struktura danych w bibliotece Pandas, składająca się z wierszy i kolumn. Można ją traktować jak tabelę w SQL lub arkusz kalkulacyjny.

**ETL (Extract, Transform, Load)**
: Proces przetwarzania danych składający się z trzech etapów: ekstrakcji danych ze źródła, transformacji ich do pożądanego formatu lub struktury, oraz załadowania do docelowego systemu (np. bazy danych, hurtowni danych).

**Feature Engineering**
: Proces tworzenia lub modyfikowania zmiennych (cech) z surowych danych w celu poprawy wydajności modeli uczenia maszynowego.

**NumPy Array**
: Podstawowa, wielowymiarowa struktura danych w bibliotece NumPy, służąca do wydajnych obliczeń numerycznych. Wszystkie elementy w `ndarray` muszą być tego samego typu.

**ORM (Object-Relational Mapper)**
: Biblioteka (np. Django ORM, SQLAlchemy), która mapuje obiekty w kodzie na tabele w relacyjnej bazie danych. Pozwala na interakcję z bazą za pomocą kodu Pythona (np. wywoływanie metod na obiektach) zamiast pisania surowych zapytań SQL.

**Series**
: Jednowymiarowa, oetykietowana tablica w bibliotece Pandas, zdolna do przechowywania danych dowolnego typu. Kolumny w DataFrame są obiektami typu Series.

**Vectorization (Wektoryzacja)**
: Technika wykonywania operacji na całych tablicach (wektorach, macierzach) jednocześnie, zamiast iterowania po pojedynczych elementach. Jest to klucz do wysokiej wydajności w bibliotekach takich jak NumPy i Pandas.

---

## Machine Learning

**Backpropagation (Propagacja wsteczna)**
: Główny algorytm używany do trenowania sztucznych sieci neuronowych. Polega na obliczaniu gradientu funkcji błędu względem wag sieci, a następnie propagowaniu tego błędu "wstecz" przez sieć, aby zaktualizować wagi.

**Batch**
: Porcja (podzbiór) danych treningowych przetwarzana w jednej iteracji algorytmu optymalizacyjnego. Użycie batchy zamiast całego zbioru danych na raz jest bardziej wydajne obliczeniowo i pamięciowo.

**Cross-validation (Walidacja krzyżowa)**
: Technika oceny zdolności generalizacji modelu ML, która polega na wielokrotnym podziale danych na zbiór treningowy i walidacyjny, a następnie uśrednieniu wyników. Pomaga uzyskać bardziej wiarygodną ocenę modelu i zapobiegać overfittingowi.

**Ensemble Learning (Uczenie zespołowe)**
: Technika, która polega na kombinowaniu predykcji wielu modeli uczenia maszynowego (tzw. "słabych uczniów") w celu uzyskania lepszych i bardziej stabilnych wyników, niż mógłby osiągnąć pojedynczy model. Przykładami są lasy losowe i gradient boosting.

**Epoch (Epoka)**
: Jeden pełny cykl przejścia algorytmu trenującego przez cały zbiór danych treningowych.

**Hyperparameter (Hiperparametr)**
: Parametr konfiguracyjny modelu, którego wartość jest ustawiana przed rozpoczęciem procesu treningu (np. szybkość uczenia, liczba drzew w lesie losowym). Hiperparametry nie są uczone na podstawie danych, w przeciwieństwie do parametrów (wag) modelu.

**Overfitting (Przeuczenie)**
: Zjawisko, w którym model uczenia maszynowego "zapamiętuje" dane treningowe, włączając w to ich szum i przypadkowe fluktuacje, zamiast uczyć się ogólnych wzorców. Taki model ma doskonałe wyniki na danych treningowych, ale bardzo słabe na nowych, niewidzianych wcześniej danych.

**Supervised Learning (Uczenie nadzorowane)**
: Paradygmat uczenia maszynowego, w którym model uczy się na podstawie danych zawierających zarówno cechy wejściowe, jak i pożądane etykiety wyjściowe (np. klasyfikacja obrazów, regresja cen mieszkań).

**Unsupervised Learning (Uczenie nienadzorowane)**
: Paradygmat uczenia maszynowego, w którym model uczy się na podstawie danych, które nie posiadają etykiet. Celem jest odkrycie ukrytej struktury w danych (np. klasteryzacja, redukcja wymiarowości).

---

## Generative AI

**Agent**
: W kontekście GenAI, autonomiczny system, który wykorzystuje LLM do rozumowania, planowania i używania zewnętrznych narzędzi w celu osiągnięcia złożonego celu, wykraczającego poza prostą odpowiedź na pytanie.

**Chain of Thought (Łańcuch myśli)**
: Technika promptowania, która polega na instruowaniu LLM, aby myślał "krok po kroku" i wypisywał swój proces rozumowania przed podaniem ostatecznej odpowiedzi. Znacząco poprawia to wyniki modelu w zadaniach wymagających złożonej logiki.

**Context Window**
: Maksymalna ilość tekstu (mierzona w tokenach), którą model LLM może przetworzyć jednocześnie w jednym zapytaniu i odpowiedzi. Jest to fundamentalne ograniczenie "pamięci" modelu.

**Embedding**
: Gęsta, numeryczna, wielowymiarowa reprezentacja (wektor) fragmentu danych (np. słowa, zdania, obrazu), która oddaje jego semantyczne znaczenie. Obiekty o podobnym znaczeniu mają podobne wektory embeddingowe w przestrzeni wektorowej.

**Fine-tuning**
: Proces dalszego trenowania wstępnie wytrenowanego modelu LLM na mniejszym, specjalistycznym zbiorze danych w celu dostosowania go do konkretnego zadania, dziedziny lub stylu odpowiedzi.

**Function Calling**
: Zdolność modelu LLM do decydowania, kiedy należy wywołać zewnętrzną funkcję (zdefiniowaną w kodzie) i z jakimi argumentami, a następnie zintegrowania wyniku tej funkcji z procesem generowania odpowiedzi. Umożliwia to integrację z zewnętrznymi API i narzędziami.

**Hallucination (Halucynacja)** / (alternatywnie) **Negatywna Halucynacja**
: Zjawisko, w którym LLM generuje informacje, które są fałszywe, bezsensowne lub nieoparte na dostarczonym kontekście, ale prezentuje je w sposób wiarygodny i faktograficzny.

**LLM (Large Language Model)**
: Duży model językowy; głęboka sieć neuronowa (zazwyczaj oparta na architekturze Transformer) wytrenowana na ogromnych zbiorach danych tekstowych w celu rozumienia i generowania języka naturalnego.

**Orchestration Framework (Framework orkiestracyjny)**
: Biblioteka (np. LangChain, Haystack) służąca do budowania złożonych aplikacji AI poprzez łączenie wielu wywołań LLM, narzędzi i źródeł danych w spójne przepływy pracy (łańcuchy, grafy).

**Prompt Engineering**
: Sztuka i nauka projektowania efektywnych zapytań (promptów) do modeli LLM w celu uzyskania pożądanych, precyzyjnych i niezawodnych odpowiedzi.

**RAG (Retrieval-Augmented Generation)**
: Wzorzec architektoniczny, w którym odpowiedź LLM jest wzbogacana ("uziemiana") o informacje dynamicznie wyszukane z zewnętrznej, zaufanej bazy wiedzy. Ma to na celu zminimalizowanie halucynacji i umożliwienie modelowi korzystania z aktualnych lub prywatnych danych.

**Token**
: Podstawowa jednostka tekstu, na której operują LLM-y. Może to być słowo, część słowa (np. "ing") lub znak interpunkcyjny. Koszt użycia API i rozmiar Context Window są mierzone w tokenach.

**Tool Use (Użycie Narzędzi)**
: Zdolność agenta AI do korzystania z zewnętrznych narzędzi (np. kalkulatora, wyszukiwarki, API, bazy danych) w celu wykonania zadania, którego nie potrafi zrealizować samodzielnie (np. obliczeń matematycznych).

**Transformer**
: Architektura sieci neuronowej, która zrewolucjonizowała przetwarzanie języka naturalnego i jest fundamentem dla większości nowoczesnych LLM-ów, takich jak GPT. Jej kluczowym mechanizmem jest *attention* (uwaga).

**Vector Database (Baza Wektorowa)**
: Specjalistyczna baza danych zoptymalizowana pod kątem przechowywania i szybkiego przeszukiwania wektorów (embeddingów) na podstawie podobieństwa semantycznego (np. za pomocą algorytmów ANN - Approximate Nearest Neighbor). Jest to kluczowy komponent systemów RAG.

**PEP (Python Enhancement Proposal)**
: Dokument opisujący nowe funkcje, ulepszenia lub standardy w Pythonie. Najsłynniejszy to PEP 8 (konwencje stylu kodu).

**REPL (Read-Eval-Print Loop)**
: Interaktywne środowisko do eksperymentowania z kodem Python, gdzie można wpisywać polecenia i natychmiast widzieć wyniki.

**EDA (Exploratory Data Analysis / Eksploracyjna Analiza Danych)**
: Proces wstępnego badania i wizualizacji danych w celu zrozumienia ich struktury, wykrycia anomalii i sformułowania hipotez.

**One-hot Encoding**
: Technika przekształcania zmiennych kategorycznych na wektor binarny, gdzie każda kategoria jest reprezentowana przez osobną kolumnę.

**ROC Curve (Krzywa ROC)**
: Wykres ilustrujący zależność między czułością a specyficznością klasyfikatora binarnego.

**Precision / Recall (Precyzja / Czułość)**
: Miary jakości klasyfikatora, szczególnie istotne przy niezbalansowanych zbiorach danych. Precyzja to odsetek trafnych predykcji pozytywnych, czułość to odsetek wykrytych wszystkich rzeczywistych pozytywów.

**Regularization (Regularyzacja)**
: Technika zapobiegająca przeuczeniu modelu poprzez dodanie kary za zbyt duże wartości wag (np. L1, L2).

**Zero-shot / Few-shot Learning**
: Zdolność modelu do rozwiązywania nowych zadań bez (zero-shot) lub z minimalną (few-shot) liczbą przykładów.

**Temperature (Temperatura)**
: Parametr sterujący "kreatywnością" generowanych odpowiedzi przez LLM – wyższa wartość daje bardziej zróżnicowane wyniki.

**F1 Score (Miara F1)**
: Miara jakości klasyfikatora będąca średnią harmoniczną precyzji i czułości (recall). Pozwala ocenić model, gdy ważna jest równowaga między precyzją a czułością, szczególnie przy niezbalansowanych danych.

**Accuracy (Dokładność)**
: Miara skuteczności klasyfikatora, określająca jaki procent wszystkich predykcji był poprawny. Wzór: (TP + TN) / (TP + TN + FP + FN).
