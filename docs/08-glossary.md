# 8. Słowniczek Pojęć

> [!NOTE]
> Ten słowniczek to Twoja podręczna encyklopedia terminów, które napotkasz w ekosystemie Pythona. Został podzielony na kategorie tematyczne, aby ułatwić nawigację. Używaj go, aby szybko sprawdzić nieznane pojęcia i ugruntować swoją wiedzę.

> [!TIP]
> Hasła pogrubione w innych rozdziałach odsyłają tutaj — kliknij, by sprawdzić definicję. Wiele haseł zawiera linki do oficjalnej dokumentacji, gdzie znajdziesz szczegóły i przykłady.

---

## Podstawowe pojęcia Python

**ASGI (Asynchronous Server Gateway Interface)**
: Nowoczesny, asynchroniczny standard komunikacji między serwerem a aplikacją webową w Pythonie. Jest następcą WSGI i został zaprojektowany do obsługi dużej liczby jednoczesnych połączeń I/O, co jest kluczowe dla aplikacji czasu rzeczywistego, WebSockets i wysokowydajnych API. Używany przez frameworki takie jak FastAPI.

**Astral**
: Firma stojąca za nowoczesnym, napisanym w Rust toolingiem dla Pythona: [`uv`](https://docs.astral.sh/uv/), [`Ruff`](https://docs.astral.sh/ruff/) i [`ty`](https://github.com/astral-sh/ty). Od marca 2026 jest częścią OpenAI, jednak jej narzędzia pozostają otwartoźródłowe (licencja MIT).

**Batteries-Included**
: Filozofia projektowania frameworków (np. Django), która polega na dostarczaniu wbudowanych, zintegrowanych rozwiązań dla większości typowych problemów, takich jak ORM, panel admina, autentykacja czy system szablonów.

**Bytecode**
: Pośrednia, niezależna od platformy forma kodu, na którą kompilowany jest kod źródłowy Pythona (.py). Nie jest to kod maszynowy, ale zestaw instrukcji dla Maszyny Wirtualnej Pythona (PVM), która go interpretuje i wykonuje. Pliki z bytecodem mają rozszerzenie `.pyc`.

**Context Manager**
: Obiekt, który zarządza zasobami poprzez zdefiniowanie metod `__enter__` i `__exit__`. Używany jest z instrukcją `with`, co gwarantuje, że zasób (np. plik, połączenie sieciowe) zostanie poprawnie zwolniony, nawet jeśli w bloku `with` wystąpi błąd. Najczęstszy przykład to `with open('file.txt') as f:`.

**Decorator**
: Funkcja, która przyjmuje inną funkcję jako argument, dodaje do niej pewną funkcjonalność, i zwraca zmodyfikowaną funkcję, nie zmieniając jej oryginalnego kodu. Składnia z `@` jest tzw. "cukrem składniowym". Przykłady to `@staticmethod`, `@property` czy dekoratory we frameworkach webowych (`@app.route('/')`).

**Duck Typing**
: Filozofia programowania, która nie skupia się na jawnym typie obiektu, ale na jego metodach i właściwościach. Jej nazwa pochodzi od powiedzenia: "If it walks like a duck and quacks like a duck, it must be a duck". W praktyce oznacza to, że funkcja będzie próbowała wywołać na obiekcie potrzebne metody, nie sprawdzając, czy jest on instancją konkretnej klasy.

**Formatter**
: Narzędzie automatycznie przepisujące kod źródłowy do jednego, kanonicznego stylu (np. spójne wcięcia, długość linii, cudzysłowy). Eliminuje dyskusje o stylu w code review. W ekosystemie Pythona tę rolę pełnią m.in. [`Ruff`](https://docs.astral.sh/ruff/) oraz [`black`](https://github.com/psf/black).

**GIL (Global Interpreter Lock)**
: Mechanizm w standardowym buildzie CPythona, który pozwala tylko jednemu wątkowi na wykonywanie bytecodu Pythona w danym momencie w ramach jednego procesu. Upraszcza zarządzanie pamięcią i zapobiega konfliktom, ale ogranicza rzeczywistą równoległość w programach wielowątkowych, które są mocno obciążone obliczeniami CPU. Powyższy opis dotyczy standardowego buildu CPythona z GIL - od Pythona 3.13/3.14 istnieje oficjalnie wspierany build **free-threaded** (no-GIL), w którym to ograniczenie nie obowiązuje (zob. rozdział 01).

**Generator**
: Specjalny typ iteratora, zdefiniowany jako funkcja używająca słowa kluczowego `yield`. Generatory produkują wartości "na żądanie", jedna po drugiej, zamiast tworzyć od razu całą kolekcję w pamięci. Jest to niezwykle wydajne pamięciowo przy pracy z dużymi zbiorami danych.

**Immutable (Niemutowalny)**
: Typ obiektu, którego stanu nie można zmienić po jego utworzeniu. Każda operacja, która wygląda jak modyfikacja, w rzeczywistości tworzy nowy obiekt w pamięci. Przykłady to `int`, `float`, `str`, `tuple`.

**Interpreter**
: Program, który wykonuje kod Python linia po linii, bez wcześniejszego etapu kompilacji do kodu maszynowego. W przypadku CPythona, interpreter w rzeczywistości wykonuje bytecode.

**Linter**
: Narzędzie do statycznej analizy kodu, które bez uruchamiania programu wykrywa potencjalne błędy, niebezpieczne wzorce i odstępstwa od konwencji. W ekosystemie Pythona popularne lintery to [`Ruff`](https://docs.astral.sh/ruff/), [`flake8`](https://flake8.pycqa.org/) i [`pylint`](https://pylint.readthedocs.io/).

**List Comprehension**
: Zwięzły, czytelny i "pythonowy" sposób tworzenia list na podstawie istniejących sekwencji. Jest to często bardziej wydajna i preferowana alternatywa dla pętli `for` z metodą `.append()`. Przykład: `squares = [x**2 for x in range(10)]`.

**Lockfile**
: Plik (np. `uv.lock`, `poetry.lock`) zamrażający dokładne, rozwiązane wersje wszystkich zależności projektu - bezpośrednich i pośrednich. Gwarantuje reprodukowalne buildy: każdy programista i serwer CI instaluje identyczny zestaw pakietów.

**MRO (Method Resolution Order)**
: Algorytm określający kolejność, w jakiej Python przeszukuje hierarchię klas bazowych w poszukiwaniu metody do wywołania. Jest to kluczowe przy wielodziedziczeniu, gdzie rozwiązuje potencjalne konflikty (jak "problem diamentowy") w sposób deterministyczny.

**Mutable (Mutowalny)**
: Typ obiektu, którego stan można zmienić w miejscu (ang. *in-place*) po jego utworzeniu. Zmiany dokonane na obiekcie w jednym miejscu kodu będą widoczne we wszystkich innych miejscach, gdzie istnieją referencje do tego obiektu. Przykłady to `list`, `dict`, `set`.

**PEP (Python Enhancement Proposal)**
: Dokument opisujący nowe funkcje, ulepszenia lub standardy w Pythonie. Najsłynniejszy to PEP 8 (konwencje stylu kodu).

**PEP 723**
: Standard pozwalający zadeklarować zależności i wymaganą wersję Pythona dla pojedynczego skryptu wewnątrz samego pliku (tzw. inline script metadata). Umożliwia uruchamianie samodzielnych skryptów z zależnościami bez tworzenia osobnego projektu - np. przez `uv run`.

**PVM (Python Virtual Machine)**
: Program, który jest sercem interpretera Pythona. Jego zadaniem jest wczytanie skompilowanego bytecodu i wykonanie zawartych w nim instrukcji.

**Pythonic**
: Określenie kodu, który jest napisany zgodnie z idiomami, konwencjami i filozofią języka Python. Taki kod jest zazwyczaj zwięzły, czytelny i wykorzystuje wbudowane mechanizmy języka (np. list comprehensions, context managers) zamiast implementować je w sposób znany z innych języków (np. pętle w stylu C).

**REPL (Read-Eval-Print Loop)**
: Interaktywne środowisko do eksperymentowania z kodem Python, gdzie można wpisywać polecenia i natychmiast widzieć wyniki.

**[Ruff](https://docs.astral.sh/ruff/)**
: Ultraszybki linter i formatter Pythona stworzony przez firmę Astral i napisany w Rust. Łączy w jednym narzędziu funkcje, które wcześniej zapewniały `black`, `isort`, `flake8` i `pylint`, działając przy tym o rzędy wielkości szybciej.

**Type Checker**
: Narzędzie sprawdzające spójność typów (na podstawie type hints) przed uruchomieniem programu, wychwytujące błędy, które inaczej ujawniłyby się dopiero w czasie wykonania. Przykłady to [`mypy`](https://mypy.readthedocs.io/), [`pyright`](https://github.com/microsoft/pyright) oraz `ty`.

**Type Hint (Wskazówka Typu)**
: Opcjonalna adnotacja w kodzie Pythona, która określa oczekiwany typ zmiennej, parametru funkcji lub wartości zwracanej. Interpreter Pythona ignoruje te wskazówki w czasie wykonania, ale są one używane przez narzędzia do analizy statycznej (np. `mypy`) i IDE w celu wczesnego wykrywania błędów i poprawy podpowiedzi.

**Virtual Environment (Środowisko Wirtualne)**
: Izolowane środowisko Pythona, które posiada własną instalację interpretera oraz niezależny zestaw pakietów. Pozwala to na unikanie konfliktów zależności między różnymi projektami na jednym komputerze.

**WSGI (Web Server Gateway Interface)**
: Tradycyjny, synchroniczny standard komunikacji między serwerem a aplikacją webową w Pythonie. Używany przez frameworki takie jak Django i Flask.

**[pre-commit](https://pre-commit.com/)**
: Framework uruchamiający zestaw automatycznych kontroli (np. lint, formatowanie, wykrywanie sekretów) jako tzw. git hooki - przed każdym commitem. Zapewnia, że do repozytorium trafia wyłącznie kod spełniający przyjęte standardy.

**[ty](https://github.com/astral-sh/ty)**
: Szybki type checker Pythona tworzony przez firmę Astral i napisany w Rust. Od grudnia 2025 dostępny w fazie beta.

**[uv](https://docs.astral.sh/uv/)**
: Ultraszybki, zunifikowany menedżer projektów, pakietów i wersji Pythona stworzony przez firmę Astral i napisany w Rust. Zastępuje w jednym narzędziu funkcje `pip`, `venv`, `pyenv`, `pipx` oraz `poetry`.

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

**Accuracy (Dokładność)**
: Miara skuteczności klasyfikatora, określająca jaki procent wszystkich predykcji był poprawny. Wzór: (TP + TN) / (TP + TN + FP + FN).

**Backpropagation (Propagacja wsteczna)**
: Główny algorytm używany do trenowania sztucznych sieci neuronowych. Polega na obliczaniu gradientu funkcji błędu względem wag sieci, a następnie propagowaniu tego błędu "wstecz" przez sieć, aby zaktualizować wagi.

**Batch**
: Porcja (podzbiór) danych treningowych przetwarzana w jednej iteracji algorytmu optymalizacyjnego. Użycie batchy zamiast całego zbioru danych na raz jest bardziej wydajne obliczeniowo i pamięciowo.

**Cross-validation (Walidacja krzyżowa)**
: Technika oceny zdolności generalizacji modelu ML, która polega na wielokrotnym podziale danych na zbiór treningowy i walidacyjny, a następnie uśrednieniu wyników. Pomaga uzyskać bardziej wiarygodną ocenę modelu i zapobiegać overfittingowi.

**EDA (Exploratory Data Analysis / Eksploracyjna Analiza Danych)**
: Proces wstępnego badania i wizualizacji danych w celu zrozumienia ich struktury, wykrycia anomalii i sformułowania hipotez.

**Ensemble Learning (Uczenie zespołowe)**
: Technika, która polega na kombinowaniu predykcji wielu modeli uczenia maszynowego (tzw. "słabych uczniów") w celu uzyskania lepszych i bardziej stabilnych wyników, niż mógłby osiągnąć pojedynczy model. Przykładami są lasy losowe i gradient boosting.

**Epoch (Epoka)**
: Jeden pełny cykl przejścia algorytmu trenującego przez cały zbiór danych treningowych.

**F1 Score (Miara F1)**
: Miara jakości klasyfikatora będąca średnią harmoniczną precyzji i czułości (recall). Pozwala ocenić model, gdy ważna jest równowaga między precyzją a czułością, szczególnie przy niezbalansowanych danych.

**Hyperparameter (Hiperparametr)**
: Parametr konfiguracyjny modelu, którego wartość jest ustawiana przed rozpoczęciem procesu treningu (np. szybkość uczenia, liczba drzew w lesie losowym). Hiperparametry nie są uczone na podstawie danych, w przeciwieństwie do parametrów (wag) modelu.

**One-hot Encoding**
: Technika przekształcania zmiennych kategorycznych na wektor binarny, gdzie każda kategoria jest reprezentowana przez osobną kolumnę.

**Overfitting (Przeuczenie)**
: Zjawisko, w którym model uczenia maszynowego "zapamiętuje" dane treningowe, włączając w to ich szum i przypadkowe fluktuacje, zamiast uczyć się ogólnych wzorców. Taki model ma doskonałe wyniki na danych treningowych, ale bardzo słabe na nowych, niewidzianych wcześniej danych.

**Precision / Recall (Precyzja / Czułość)**
: Miary jakości klasyfikatora, szczególnie istotne przy niezbalansowanych zbiorach danych. Precyzja to odsetek trafnych predykcji pozytywnych, czułość to odsetek wykrytych wszystkich rzeczywistych pozytywów.

**ROC Curve (Krzywa ROC)**
: Wykres ilustrujący zależność między czułością a specyficznością klasyfikatora binarnego.

**Regularization (Regularyzacja)**
: Technika zapobiegająca przeuczeniu modelu poprzez dodanie kary za zbyt duże wartości wag (np. L1, L2).

**Supervised Learning (Uczenie nadzorowane)**
: Paradygmat uczenia maszynowego, w którym model uczy się na podstawie danych zawierających zarówno cechy wejściowe, jak i pożądane etykiety wyjściowe (np. klasyfikacja obrazów, regresja cen mieszkań).

**Unsupervised Learning (Uczenie nienadzorowane)**
: Paradygmat uczenia maszynowego, w którym model uczy się na podstawie danych, które nie posiadają etykiet. Celem jest odkrycie ukrytej struktury w danych (np. klasteryzacja, redukcja wymiarowości).

---

## Generative AI

**Agent**
: W kontekście GenAI, autonomiczny system, który wykorzystuje LLM do rozumowania, planowania i używania zewnętrznych narzędzi w celu osiągnięcia złożonego celu, wykraczającego poza prostą odpowiedź na pytanie.

**Agentic AI / Agentic Workflow**
: Systemy, w których LLM nie udziela jednorazowej odpowiedzi, lecz planuje i wykonuje wieloetapowe zadania - używając narzędzi w iteracyjnej pętli rozumowania, samodzielnie oceniając wyniki i korygując kolejne kroki.

**Chain of Thought (Łańcuch myśli)**
: Technika promptowania, która polega na instruowaniu LLM, aby myślał "krok po kroku" i wypisywał swój proces rozumowania przed podaniem ostatecznej odpowiedzi. Znacząco poprawia to wyniki modelu w zadaniach wymagających złożonej logiki.

**Constrained Generation**
: Ogólna technika ograniczania outputu LLM regułami formalnymi (np. gramatyką bezkontekstową, CFG), która gwarantuje, że wygenerowany tekst jest składniowo poprawny. Bardziej ogólna niż Structured Outputs - pozwala wymusić dowolny język opisany gramatyką.

**Context Window**
: Maksymalna ilość tekstu (mierzona w tokenach), którą model LLM może przetworzyć jednocześnie w jednym zapytaniu i odpowiedzi. Jest to fundamentalne ograniczenie "pamięci" modelu.

**Embedding**
: Gęsta, numeryczna, wielowymiarowa reprezentacja (wektor) fragmentu danych (np. słowa, zdania, obrazu), która oddaje jego semantyczne znaczenie. Obiekty o podobnym znaczeniu mają podobne wektory embeddingowe w przestrzeni wektorowej.

**Embedding Model**
: Model, którego zadaniem jest zamiana tekstu (lub obrazu czy audio) na wektory embeddingowe. Stanowi fundament systemów RAG i wyszukiwania semantycznego. Aktualne przykłady to Gemini Embedding, Voyage 4, Cohere embed-v4 oraz BGE-M3.

**Fine-tuning**
: Proces dalszego trenowania wstępnie wytrenowanego modelu LLM na mniejszym, specjalistycznym zbiorze danych w celu dostosowania go do konkretnego zadania, dziedziny lub stylu odpowiedzi.

**Function Calling**
: Zdolność modelu LLM do decydowania, kiedy należy wywołać zewnętrzną funkcję (zdefiniowaną w kodzie) i z jakimi argumentami, a następnie zintegrowania wyniku tej funkcji z procesem generowania odpowiedzi. Umożliwia to integrację z zewnętrznymi API i narzędziami.

**Hallucination (Halucynacja)**
: Zjawisko, w którym LLM generuje informacje, które są fałszywe, bezsensowne lub nieoparte na dostarczonym kontekście, ale prezentuje je w sposób wiarygodny i faktograficzny.

**LLM (Large Language Model)**
: Duży model językowy; głęboka sieć neuronowa (zazwyczaj oparta na architekturze Transformer) wytrenowana na ogromnych zbiorach danych tekstowych w celu rozumienia i generowania języka naturalnego.

**[MCP](https://modelcontextprotocol.io/) (Model Context Protocol)**
: Otwarty standard wprowadzony przez Anthropic (listopad 2024), który w ujednolicony sposób łączy modele LLM i agentów z zewnętrznymi narzędziami oraz źródłami danych - bywa nazywany "USB-C dla AI". Został przyjęty m.in. przez OpenAI, Google i Microsoft, a w grudniu 2025 przekazany pod opiekę Linux Foundation.

**Mixture-of-Experts (MoE)**
: Architektura sieci neuronowej, w której dla każdego tokena aktywowany jest jedynie podzbiór parametrów (tzw. ekspertów), a nie cała sieć. Pozwala znacząco zwiększyć liczbę parametrów modelu przy umiarkowanym koszcie inferencji; standard dużych modeli (np. model 671B parametrów z 37B aktywnych).

**NL2SQL / Generative BI**
: Zamiana pytania zadanego w języku naturalnym na zapytanie SQL, jego wykonanie i przedstawienie odpowiedzi. Jedno z praktycznych zastosowań RAG w analityce danych - pozwala nietechnicznym użytkownikom odpytywać bazy danych.

**Orchestration Framework (Framework orkiestracyjny)**
: Biblioteka (np. [LangChain](https://www.langchain.com/), [LangGraph](https://www.langchain.com/langgraph), Haystack) służąca do budowania złożonych aplikacji AI poprzez łączenie wielu wywołań LLM, narzędzi i źródeł danych w spójne przepływy pracy (łańcuchy, grafy). LangGraph osiągnął wersję 1.0 pod koniec 2025 roku i stał się domyślnym runtime'em agentów w ekosystemie LangChain. Widoczny jest trend przechodzenia w stronę dedykowanych Agent SDK.

**Prompt Engineering**
: Sztuka i nauka projektowania efektywnych zapytań (promptów) do modeli LLM w celu uzyskania pożądanych, precyzyjnych i niezawodnych odpowiedzi.

**RAG (Retrieval-Augmented Generation)**
: Wzorzec architektoniczny, w którym odpowiedź LLM jest wzbogacana ("uziemiana") o informacje dynamicznie wyszukane z zewnętrznej, zaufanej bazy wiedzy. Ma to na celu zminimalizowanie halucynacji i umożliwienie modelowi korzystania z aktualnych lub prywatnych danych.

**Reasoning Model / Large Reasoning Model (LRM)**
: Modele trenowane (m.in. metodami uczenia ze wzmocnieniem) tak, by przed udzieleniem odpowiedzi "myślały" - generowały wewnętrzny łańcuch rozumowania, zużywając dodatkowe zasoby obliczeniowe na etapie inferencji. Przykłady to rodzina OpenAI o-series oraz DeepSeek-R1.

**Sovereign AI / On-premise AI**
: Model wdrożenia, w którym cały pipeline AI (modele, dane, inferencja) działa lokalnie, na infrastrukturze organizacji, a dane nie opuszczają firmy. Szczególnie istotny w sektorach regulowanych (finanse, ochrona zdrowia, administracja publiczna).

**Structured Outputs**
: Mechanizm wymuszający zgodność odpowiedzi LLM ze ściśle zdefiniowanym schematem (np. JSON Schema), co gwarantuje przewidywalny, parsowalny output. Należy go odróżnić od starszego "JSON Mode", który zapewniał jedynie poprawność składniową JSON-a, bez gwarancji zgodności ze schematem.

**Temperature (Temperatura)**
: Parametr sterujący "kreatywnością" generowanych odpowiedzi przez LLM – wyższa wartość daje bardziej zróżnicowane wyniki.

**Test-Time Compute / Inference-Time Scaling**
: Paradygmat poprawy jakości odpowiedzi modelu poprzez zwiększanie zasobów obliczeniowych na etapie inferencji (np. dłuższe rozumowanie, wielokrotne próbkowanie) zamiast skalowania samego rozmiaru modelu. Fundament działania modeli rozumujących.

**Token**
: Podstawowa jednostka tekstu, na której operują LLM-y. Może to być słowo, część słowa (np. "ing") lub znak interpunkcyjny. Koszt użycia API i rozmiar Context Window są mierzone w tokenach.

**Tool Use (Użycie Narzędzi)**
: Zdolność agenta AI do korzystania z zewnętrznych narzędzi (np. kalkulatora, wyszukiwarki, API, bazy danych) w celu wykonania zadania, którego nie potrafi zrealizować samodzielnie (np. obliczeń matematycznych).

**Transformer**
: Architektura sieci neuronowej, która zrewolucjonizowała przetwarzanie języka naturalnego i jest fundamentem dla większości nowoczesnych LLM-ów, takich jak GPT. Jej kluczowym mechanizmem jest *attention* (uwaga).

**Vector Database (Baza Wektorowa)**
: Specjalistyczna baza danych zoptymalizowana pod kątem przechowywania i szybkiego przeszukiwania wektorów (embeddingów) na podstawie podobieństwa semantycznego (np. za pomocą algorytmów ANN - Approximate Nearest Neighbor). Jest to kluczowy komponent systemów RAG.

**Zero-shot / Few-shot Learning**
: Zdolność modelu do rozwiązywania nowych zadań bez (zero-shot) lub z minimalną (few-shot) liczbą przykładów.

---

## Architektura i Dobre Praktyki

**12-factor App**
: Zbiór dwunastu zasad budowy aplikacji cloud-native (m.in. konfiguracja w zmiennych środowiskowych, bezstanowe procesy, jawne zależności), które ułatwiają skalowanie, wdrażanie i utrzymanie systemów.

**ADR (Architecture Decision Record)**
: Krótki dokument zapisujący pojedynczą decyzję architektoniczną - jej kontekst, podjęty wybór oraz konsekwencje. Tworzy historyczny ślad rozumowania zespołu.

**Anemic Domain Model**
: Antywzorzec, w którym obiekty domenowe przechowują wyłącznie dane (bez logiki), a cała logika biznesowa jest wypchnięta do osobnych "serwisów". Pozbawia model obiektowy jego głównej zalety.

**Big Ball of Mud**
: Antywzorzec opisujący system pozbawiony czytelnej struktury, w którym wszystko zależy od wszystkiego. Utrudnia rozwój, testowanie i utrzymanie kodu.

**Clean Architecture**
: Wzorzec warstwowy, w którym reguła zależności jest skierowana zawsze do wewnątrz - ku domenie. Warstwy zewnętrzne (UI, infrastruktura) zależą od wewnętrznych, ale nigdy odwrotnie.

**Conway's Law (Prawo Conwaya)**
: Obserwacja, że struktura projektowanego systemu odzwierciedla strukturę komunikacyjną organizacji, która go zbudowała.

**DDD (Domain-Driven Design)**
: Podejście projektowe stawiające model domeny biznesowej w centrum systemu, kładące nacisk na wspólny język (ubiquitous language) zespołu i ekspertów dziedzinowych.

**Hexagonal Architecture / Ports & Adapters**
: Wzorzec architektoniczny separujący logikę domenową od infrastruktury za pomocą portów (interfejsów definiowanych przez domenę) i adapterów (konkretnych implementacji, np. baza danych, API). Umożliwia łatwą wymianę i testowanie komponentów.

**Protocol (typing)**
: Mechanizm structural typing w Pythonie (PEP 544): zgodność typu z interfejsem jest sprawdzana po jego strukturze (zestawie metod i atrybutów), a nie po jawnym dziedziczeniu. Statyczny odpowiednik duck typingu.

**RBAC (Role-Based Access Control)**
: Model kontroli dostępu, w którym uprawnienia przypisuje się rolom, a role - użytkownikom. Upraszcza zarządzanie dostępem w większych systemach.

**Rich Domain Model**
: Model domenowy, w którym obiekty zawierają zarówno dane, jak i logikę biznesową operującą na tych danych. Przeciwieństwo Anemic Domain Model.

**Vertical Slice Architecture**
: Organizacja kodu w pionowe "plastry" funkcjonalności - każdy feature posiada własne modele, logikę i endpointy API, zamiast dzielić kod według warstw technicznych. Minimalizuje sprzężenie między funkcjami.

**model C4**
: Notacja do tworzenia diagramów architektury oprogramowania na czterech poziomach szczegółowości: Context (kontekst systemu), Container (kontenery), Component (komponenty) i Code (kod).
