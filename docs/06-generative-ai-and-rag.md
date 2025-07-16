# 6. Aplikacje GenAI i RAG: Budowanie Inteligentnych Systemów

> [!NOTE]
> Generatywna Sztuczna Inteligencja (Generative AI) to najnowsza i najszybciej rozwijająca się gałąź ekosystemu Pythona. Jest to ewolucja poddziedziny Machine Learninu - NLP (ang. *Natural Language Processing*, czyli przetwarzanie języka naturalnego). Zrozumienie podstaw działania modeli językowych (LLM) oraz kluczowych wzorców architektonicznych, takich jak RAG, jest niezbędne do budowania nowoczesnych, rzetelnych i wartościowych aplikacji AI.

---

## 🧠 Czym są Duże Modele Językowe (LLM)?

W najprostszym ujęciu, duży model językowy (LLM) to głęboka sieć neuronowa (ang. *"Deep Neural Network"*) wytrenowana na ogromnych ilościach danych tekstowych (nazywanych *"datasetem"* czy *"corpusem"*). Jej podstawowym zadaniem jest **przewidywanie następnego słowa (a dokładniej: `tokenu`) w sekwencji**. Ta z pozoru prosta zdolność, przeskalowana do miliardów parametrów i terabajtów danych treningowych, prowadzi do wyłaniania się (ang. *emergence*) złożonych zachowań, takich jak odpowiadanie na pytania, tłumaczenie, streszczanie tekstów czy pisanie kodu.

### Polecane zasoby do głębszego zrozumienia

Aby efektywnie pracować z LLM, warto zrozumieć, co dzieje się "pod maską". Poniższe materiały są absolutnie najlepszym punktem startowym.

* **Teoria dla każdego (Intuicja wizualna)**: Jeśli chcesz zrozumieć, jak naprawdę działa deep learning i modele językowe AI, koniecznie zobacz serię [**3Blue1Brown o sieciach neuronowych**](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1\_67000Dx\_ZCJB-3pi). To jedne z najlepszych istniejących materiałów, które w sposób wizualny i przystępny tłumaczą podstawowe idee stojące za nowoczesnymi modelami AI i machine learningiem. Idealne na start, by zbudować intuicję i "poczuć" jak myśli sieć neuronowa oraz (dalej) modele językowe.
* **Wszystko w jednym wykładzie**: Wykład [***Andrieja Karpathy'ego* *"Intro to Large Language Models"***](https://www.youtube.com/watch?v=kCc8FmEb1nY) to jedno z lepszych wprowadzeń w temat, jakie istnieje. Karpathy, jako jeden z czołowych ekspertów w dziedzinie, w przystępny sposób wyjaśnia architekturę Transformerów, proces treningu i skalowania - wszystko w formie jednego, długiego i interaktywnego wykładu.
* **Bieżące nowości**: Świat GenAI zmienia się z tygodnia na tydzień. Kanał YouTube [**bycloud**](https://www.youtube.com/@bycloud) to doskonałe źródło podsumowań najnowszych prac badawczych i przełomowych modeli, prezentowanych w technicznym, ale zrozumiałym, atrakcyjnym wizualnie formacie.

---

## ✅ Mocne i Słabe Strony LLM-ów

Jako inżynier musisz traktować LLM jak każde inne narzędzie – ze świadomością jego zalet i ograniczeń. Myślenie o LLM jako o "magicznej czarnej skrzynce" prowadzi do frustracji i zawodnych aplikacji.

> [!IMPORTANT]
> **Niedeterministyczność LLM-ów: Kluczowe Wyzwanie dla Inżynierów**
> 
> W przeciwieństwie do tradycyjnych programów komputerowych, LLM-y są **niedeterministyczne** - oznacza to, że ten sam prompt może wygenerować różne odpowiedzi przy każdym wywołaniu, czy przy podaniu tego samego zbioru danych w innym formacie. Ta fundamentalna różnica ma ogromne konsekwencje dla budowy aplikacji produkcyjnych:
>
> **Dlaczego tak się dzieje?**
> - **Sampling podczas generowania**: LLM-y nie wybierają "najlepszego" następnego słowa, lecz **losują** z rozkładu prawdopodobieństwa wszystkich możliwych tokenów
> - **Parametr `temperature`**: Kontroluje "kreatywność" modelu - wyższa wartość (np. 0.8) zwiększa losowość, niższa (np. 0.1) czyni odpowiedzi bardziej przewidywalne, ale są mniej... kreatywne, innowacyjne - model stara się wtedy trzymać przytoczonego kontekstu nad własną wiedzą.
> - **Floating-point arithmetic**: Nawet przy identycznych parametrach, mikroskopijne różnice w obliczeniach mogą prowadzić do innych wyników
>
> **Praktyczne konsekwencje dla aplikacji:**
> - **Testowanie**: Nie możesz napisać prostego testu jednostkowego "input X → output Y", bo output może się różnić. Zautomatyzowane testy same w sobie muszą więc być kierowane przez rozwiązanie wspomagane modelem językowym, który analizuje odpowiedź i porównuje ją z oczekiwanym wynikiem.
> - **Reprodukowalność**: Debugowanie staje się trudniejsze - błąd może wystąpić raz na 10 prób
> - **Konsystentność UX**: Użytkownicy mogą być zdezorientowani różnymi odpowiedziami na identyczne pytania
>
> **Strategie radzenia sobie z niedeterministycznością:**
> - **Seed**: Niektóre API pozwalają ustawić `seed` dla większej powtarzalności (choć nie gwarantuje 100% identycznych wyników)
> - **Multiple sampling**: Wygeneruj kilka odpowiedzi i wybierz najlepszą lub znajdź wspólne elementy
> - **Structured outputs**: Użyj Pydantic/BAML do wymuszenia konkretnego formatu, co ogranicza przestrzeń możliwych odpowiedzi
> - **Prompt engineering**: Precyzyjne instrukcje i przykłady (few-shot learning) zwiększają spójność
> - **Post-processing**: Dodaj walidację i normalizację wygenerowanych odpowiedzi

| Obszar Zastosowań | Mocne Strony (w czym są dobre) | Słabe Strony / Ograniczenia (gdzie zawodzą) | Strategie Mitygacji (Jak sobie z tym radzić?) |
| :--- | :--- | :--- | :--- |
| **Analiza Danych Niestrukturalnych** | Doskonałe w rozumieniu i przetwarzaniu języka naturalnego: streszczanie tekstów, analiza sentymentu, kategoryzacja, odpowiadanie na pytania oparte na tekście. | Mogą gubić niuanse i kontekst w bardzo długich lub skomplikowanych dokumentach. | Precyzyjne promptowanie (np. Chain-of-Thought), przetwarzanie dokumentów fragmentami (map-reduce), fine-tuning na danych dziedzinowych. |
| **Wiedza i Fakty** | Posiadają ogromną, szeroką wiedzę ogólną zakodowaną w swoich parametrach podczas treningu. | **Halucynacje**: generowanie wiarygodnie brzmiących, ale fałszywych informacji. **Wiedza odcięta w czasie**: model nie zna wydarzeń po zakończeniu jego treningu. | **Retrieval-Augmented Generation (RAG)**, aby uziemić odpowiedzi w konkretnych, aktualnych źródłach danych. Integracja z zewnętrznymi API (np. wyszukiwarką). |
| **Rozumowanie i Obliczenia** | Potrafią radzić sobie z prostą logiką i podążać za instrukcjami krok po kroku. | **Bardzo słabe w matematyce** i złożonym, wieloetapowym rozumowaniu. Często popełniają błędy w prostych obliczeniach. | **Tool Use (Użycie Narzędzi)**: Nie proś LLM o liczenie. Daj mu dostęp do narzędzi, np. poproś, aby wygenerował i wykonał kod Pythona używający kalkulatora. |
| **Strukturyzacja Danych** | Potrafią generować dane w formatach strukturalnych, takich jak JSON czy XML, na podstawie tekstu. | **Niska niezawodność**: często generują niepoprawny składniowo JSON, pomijają pola, mylą typy danych, zwłaszcza przy złożonych schematach. | **Wymuszanie schematu odpowiedzi**: Użycie bibliotek takich jak **Pydantic** lub **BAML** do zdefiniowania ścisłego schematu wyjściowego i walidacji odpowiedzi modelu. |

---

## 📚 Czym jest RAG (Retrieval-Augmented Generation)?

**RAG** to obecnie najważniejszy wzorzec architektoniczny w budowie rzetelnych aplikacji opartych na LLM. W prostych słowach, RAG zmienia zadanie z "egzaminu z pamięci" na **"egzamin z otwartą książką"**.

Zamiast polegać wyłącznie na wiedzy "zamrożonej" w parametrach modelu, proces RAG wygląda następująco:

1.  **Retrieval (Wyszukanie)**: Gdy użytkownik zadaje pytanie, system najpierw przeszukuje zewnętrzną bazę wiedzy (np. Twoją firmową dokumentację, bazę produktów) w poszukiwaniu najbardziej relevantnych fragmentów informacji.
2.  **Augmentation (Wzbogacenie)**: Znalezione fragmenty są dołączane do oryginalnego zapytania użytkownika jako kontekst, tworząc nowy, wzbogacony prompt.
3.  **Generation (Generowanie)**: Ten wzbogacony prompt jest wysyłany do LLM, który ma teraz wszystkie potrzebne informacje, aby wygenerować precyzyjną, opartą na faktach odpowiedź.

**Dlaczego to jest kluczowe?** RAG bezpośrednio rozwiązuje dwa największe problemy LLM w zastosowaniach biznesowych: **halucynacje** i **nieaktualną wiedzę**. Model jest "uziemiony" (ang. *grounded*) w konkretnych, zaufanych danych.

---

## 📝 Prompt Engineering: Sztuka Rozmowy z LLM

**Prompt engineering** to praktyka projektowania i optymalizowania zapytań (promptów) do modeli językowych, aby uzyskać jak najlepsze, najbardziej spójne i użyteczne odpowiedzi. To kluczowa umiejętność każdego inżyniera GenAI – od jakości promptu zależy nie tylko trafność odpowiedzi, ale też bezpieczeństwo, powtarzalność i niezawodność całej aplikacji.

### Najważniejsze techniki promptowania

Poniżej znajdziesz najważniejsze techniki, które warto znać i stosować w praktyce (szczegółowe przykłady i omówienia znajdziesz na [Prompting Guide](https://www.promptingguide.ai/techniques)):

- **Zero-shot prompting** – po prostu zadajesz pytanie lub wydajesz polecenie bez dodatkowych przykładów.
- **Few-shot prompting** – podajesz kilka przykładów poprawnych odpowiedzi, aby model "nauczył się" wzorca.
- **Chain-of-Thought (CoT)** – prosisz model, by rozwiązywał zadanie krok po kroku, np. "Wyjaśnij swój tok rozumowania".
- **Role prompting** – nadajesz modelowi rolę (np. "Jesteś ekspertem od prawa podatkowego...").
- **Instruction-based prompting** – bardzo precyzyjne, jasne instrukcje, często z określeniem formatu odpowiedzi.
- **Reflexion/self-correction** – prosisz model, by sam ocenił i poprawił swoją odpowiedź.
- **Structured output prompting** – wymuszasz konkretny format odpowiedzi (np. JSON, tabela, lista punktów).

Więcej technik i praktycznych przykładów znajdziesz na stronie: [https://www.promptingguide.ai/techniques](https://www.promptingguide.ai/techniques)

### Dobre praktyki i typowe błędy

- Formułuj polecenia jasno, jednoznacznie i bez niedopowiedzeń.
- Unikaj zbyt ogólnych pytań – im bardziej szczegółowy prompt, tym lepsza odpowiedź.
- Testuj różne warianty promptów i porównuj wyniki.
- W przypadku złożonych zadań – dziel je na mniejsze kroki (dekompozycja problemu).
- Wymuszaj format odpowiedzi, jeśli to możliwe (np. "Zwróć wynik jako JSON z polami: ...").
- Używaj przykładów (few-shot), gdy zależy Ci na powtarzalności i spójności.

Typowe błędy:
- Zbyt ogólne lub nieprecyzyjne polecenia.
- Brak określenia formatu odpowiedzi.
- Zbyt długie prompty (model może "zgubić" kontekst).
- Brak testowania różnych wariantów.

### Narzędzia wspierające inżynierię promptów

- [**Instructor**](https://python.useinstructor.com/prompting/) – biblioteka do wymuszania struktury odpowiedzi LLM, bardzo podobna do BAML, ale oparta o [Pydantic](https://docs.pydantic.dev/latest/). Pozwala łatwo wymusić, by model zwracał dane w określonym schemacie (np. klasie Pydantic), co znacznie zwiększa niezawodność i bezpieczeństwo aplikacji.
* [**BAML (Basically a Made-up Language)**](https://docs.boundaryml.com/home): BAML to specjalistyczny język dziedzinowy (DSL, ang. *"Domain Specific Language"*) zaprojektowany do generowania **ustrukturyzowanych odpowiedzi z LLM** – z naciskiem na najlepsze doświadczenie deweloperskie. Pozwala budować niezawodnych agentów, chatboty z RAG, ekstrakcję danych z PDF i wiele więcej. BAML w znacznej części eliminuje typowe problemy pracy z promptami (brak type safety, konieczność ręcznego testowania, trudności z walidacją) i pozwala skupić się na logice biznesowej, a nie na walce z formatem odpowiedzi modelu.
- **Pydantic** – kluczowy komponent do walidacji i wymuszania schematów odpowiedzi w Pythonie.

**Więcej o Instructor i praktycznych przykładach znajdziesz tu:** [https://python.useinstructor.com/prompting/](https://python.useinstructor.com/prompting/)

---

## 🗄️ Bazy Wektorowe: Sercem nowoczesnych aplikacji GenAI i RAG

Bazy wektorowe to wyspecjalizowane systemy bazodanowe do przechowywania i szybkiego wyszukiwania tzw. wektorów osadzeń (*embeddings*), czyli liczbowych reprezentacji tekstu, obrazów czy innych danych. Są one niezbędne w architekturze RAG, gdzie umożliwiają błyskawiczne znajdowanie najbardziej podobnych fragmentów wiedzy do zapytania użytkownika.

**Najważniejsze bazy wektorowe wykorzystywane w 2024 roku:**

- [**Pinecone**](https://www.pinecone.io/) – w pełni zarządzana, skalowalna baza wektorowa, szeroko stosowana w produkcyjnych systemach GenAI.
- [**Weaviate**](https://weaviate.io/) – open-source’owa baza z bogatym API, wsparciem dla hybrydowego wyszukiwania (wektorowego i tekstowego) oraz integracją z popularnymi narzędziami AI.
- [**Milvus**](https://milvus.io/) – bardzo wydajna, open-source’owa baza, skalująca się do miliardów wektorów, z szerokim wsparciem dla różnych przypadków użycia (RAG, wyszukiwanie obrazów, rekomendacje).
- [**Chroma**](https://trychroma.com/) – lekka, open-source’owa baza, często wykorzystywana w prototypowaniu i mniejszych projektach.
- [**Qdrant**](https://qdrant.tech/) – szybka, open-source’owa baza z naciskiem na łatwość wdrożenia i integrację z ekosystemem Python/AI.
- [**SvectorDB**](https://svectordb.com/) – nowoczesna, serwerlessowa baza zoptymalizowana pod kątem kosztów i łatwości integracji.
- [**Redis**](https://redis.io/docs/interact/search-and-query/search/vectors/) – popularna baza NoSQL z modułem do wyszukiwania wektorowego.
- [**FAISS**](https://github.com/facebookresearch/faiss) – biblioteka Facebooka do wyszukiwania podobieństw w dużych zbiorach wektorów, często używana jako silnik pod spodem innych rozwiązań.
- [**Vespa**](https://vespa.ai/) – platforma do wyszukiwania i rekomendacji z natywnym wsparciem dla wektorów.

**Dodatkowo, coraz większą rolę odgrywają:**
- [**Elasticsearch**](https://www.elastic.co/) – najpopularniejsza na świecie baza do wyszukiwania tekstowego, która od wersji 8.x natywnie wspiera wyszukiwanie wektorowe (HNSW, ANN, hybrydowe zapytania, integracja z Lucene, wsparcie dla GPU, kompresja, skalowalność, bezpieczeństwo, szeroka dokumentacja). Elasticsearch pozwala łączyć klasyczne wyszukiwanie pełnotekstowe z semantycznym, co jest kluczowe w nowoczesnych aplikacjach RAG. [Więcej: blog Elastic](https://www.elastic.co/search-labs/blog/elasticsearch-lucene-vector-database-gains)
- [**LanceDB**](https://lancedb.com/) – nowoczesna, open-source’owa baza zoptymalizowana pod multimodalne AI (tekst, obrazy, audio). Wyróżnia się bardzo wydajnym, kolumnowym formatem danych (Lance), wsparciem dla indeksów IVF+PQ, HNSW, pełnotekstowego wyszukiwania, hybrydowych zapytań, wersjonowania i integracji z Pandas, DuckDB, PyArrow. LanceDB jest lekka, szybka, pozwala na pracę zarówno lokalnie, jak i w chmurze, a jej architektura umożliwia obsługę miliardowych zbiorów na tanim sprzęcie. [Więcej: dokumentacja LanceDB](https://docs.lancedb.com/core/index)
- [**pgvector**](https://github.com/pgvector/pgvector) – rozszerzenie do PostgreSQL, które pozwala przechowywać i wyszukiwać wektory bezpośrednio w relacyjnej bazie danych. Obsługuje indeksy HNSW, IVF, operatory podobieństwa (cosine, L2, dot), integruje się z klasycznymi zapytaniami SQL i pozwala łączyć wyszukiwanie semantyczne z relacyjnymi filtrami, joinami i transakcjami. Idealne do budowy hybrydowych aplikacji, gdzie dane wektorowe i klasyczne współistnieją. [Więcej: dokumentacja pgvector](https://github.com/pgvector/pgvector)

**Wskazówka:** Wybór bazy zależy od skali projektu, wymagań dotyczących wydajności, łatwości wdrożenia oraz integracji z innymi narzędziami (np. LangChain, LlamaIndex, Haystack). Elasticsearch i pgvector są świetne do integracji z istniejącymi systemami, LanceDB do multimodalnych i dużych zbiorów, Pinecone/Weaviate/Milvus do skalowalnych, dedykowanych rozwiązań GenAI.

**Źródła i więcej informacji:**
- [Elasticsearch – blog o wydajności i architekturze wektorowej](https://www.elastic.co/search-labs/blog/elasticsearch-lucene-vector-database-gains)
- [LanceDB – dokumentacja i porównania](https://docs.lancedb.com/core/index)
- [pgvector – porównanie z innymi rozwiązaniami](https://dev.to/gaocegege/pgvector-vs-pgvectors-in-2024-a-comprehensive-comparison-for-vector-search-in-postgresql-3n08)

---

## 🕸️ Bazy Grafowe: Alternatywa i Uzupełnienie dla Baz Wektorowych

Bazy grafowe to wyspecjalizowane systemy bazodanowe, które przechowują dane jako węzły (obiekty) i krawędzie (relacje). Pozwalają one modelować i analizować złożone powiązania między danymi, co jest nieocenione w zastosowaniach takich jak:
- budowa **knowledge graphów** (grafów wiedzy),
- eksploracja relacji (np. powiązania osób, firm, produktów),
- rekomendacje,
- wykrywanie oszustw,
- zaawansowane systemy RAG (GraphRAG, hybrydowe RAG).

**Najważniejsze bazy grafowe wykorzystywane w 2024 roku:**
- [**Neo4j**](https://neo4j.com/) – najpopularniejsza baza grafowa na świecie, szeroko stosowana w knowledge graphach, rekomendacjach, fraud detection, z bogatym ekosystemem narzędzi (Cypher, Graph Data Science, integracje z LLM, GraphRAG, LlamaIndex, LangChain, Google GenAI Toolbox).
- [**Memgraph**](https://memgraph.com/) – wydajna, open-source’owa baza grafowa, kompatybilna z Cypher, wykorzystywana m.in. przez NASA do budowy knowledge graphów i GraphRAG. Mocno wspiera integracje z Pythonem i narzędziami AI.
- [**NebulaGraph**](https://www.nebula-graph.io/) – rozproszona, skalowalna baza grafowa, zoptymalizowana pod bardzo duże zbiory danych (triliony krawędzi), z własnym językiem zapytań nGQL i wsparciem dla chmury.

**Zalety baz grafowych:**
- Naturalne modelowanie złożonych relacji i powiązań (np. multi-hop reasoning, śledzenie powiązań, eksploracja sieci).
- Wydajne zapytania oparte o relacje (np. "znajdź wszystkich znajomych znajomych", "wykryj cykle").
- Możliwość łączenia danych strukturalnych, relacyjnych i wektorowych (np. Neo4j Vector Index, GraphRAG, hybrydowe wyszukiwanie).
- Przejrzystość i wyjaśnialność odpowiedzi (łatwo pokazać ścieżkę uzasadniającą wynik).
- Integracja z narzędziami GenAI (LangChain, LlamaIndex, Google GenAI Toolbox, GraphRAG, agentic architectures).

**Wady baz grafowych:**
- Mniej wydajne w czysto semantycznym wyszukiwaniu na bardzo dużych zbiorach tekstów (tu lepsze są bazy wektorowe).
- Krzywa uczenia się (nowe języki zapytań, np. Cypher, nGQL).
- Wysoki koszt wdrożenia przy bardzo dużej skali (np. Neo4j w wersji enterprise).
- Często wymagają przemyślanego modelowania danych (nie zawsze "wrzucisz wszystko jak leci").

**Przykłady frameworków bazujących na bazach grafowych:**
- LightRAG
- TrustGraph
- Graphiti
- Microsoft GraphRAG
- Nano GraphRAG
- R2R

**Porównanie: Bazy Wektorowe vs. Bazy Grafowe**

| Cecha / Zastosowanie         | Bazy Wektorowe                | Bazy Grafowe                  |
|-----------------------------|-------------------------------|-------------------------------|
| **Model danych**            | Wektory (embeddings)          | Węzły i krawędzie (relacje)   |
| **Optymalne do**            | Szybkie wyszukiwanie podobieństw semantycznych, RAG | Analiza relacji, knowledge graphy, multi-hop reasoning |
| **Wydajność**               | Bardzo duża dla ANN, HNSW     | Bardzo duża dla zapytań relacyjnych |
| **Wyjaśnialność**           | Niska ("dlaczego ten wynik?") | Wysoka (można pokazać ścieżkę relacji) |
| **Integracja z LLM**        | RAG, hybrydowe wyszukiwanie   | GraphRAG, agentic RAG, hybrydowe RAG |
| **Skalowalność**            | Doskonała (miliardy wektorów) | Dobra (triliony relacji w NebulaGraph) |
| **Przykłady**               | Pinecone, Milvus, Chroma, Qdrant, Elasticsearch, LanceDB, pgvector | Neo4j, Memgraph, NebulaGraph |
| **Wady**                    | Brak relacji, "płaskie" wyniki | Krzywa uczenia, koszt, modelowanie |

**Kiedy wybrać bazę grafową?**
- Gdy kluczowe są relacje, powiązania, ścieżki, multi-hop reasoning.
- Gdy budujesz knowledge graph, system rekomendacji, analizę sieci społecznych, fraud detection.
- Gdy chcesz łączyć dane relacyjne, wektorowe i semantyczne (GraphRAG, hybrydowe RAG).

**Kiedy wybrać bazę wektorową?**
- Gdy kluczowa jest szybkość i skalowalność wyszukiwania podobieństw semantycznych (np. RAG na dużych zbiorach dokumentów).
- Gdy nie potrzebujesz złożonych relacji między danymi.

**Więcej o GraphRAG i agentic RAG:**
- [Neo4j GraphRAG – dokumentacja i przykłady](https://neo4j.com/docs/genai/)
- [Memgraph GraphRAG – blog i przykłady NASA](https://memgraph.com/blog/nasa-memgraph-people-knowledge-graph)
- [Porównanie GraphRAG vs. klasyczny RAG (Neo4j)](https://neo4j.com/blog/developer/graphrag-and-agentic-architecture-with-neoconverse/)
- [NebulaGraph RAG – dokumentacja](https://www.nebula-graph.io/)

---

## 🛠️ Frameworki i Narzędzia dla GenAI

### Frameworki Orkiestracyjne

Gdy prosta aplikacja typu "prompt -> odpowiedź" przestaje wystarczać, potrzebujesz frameworka do **orkiestracji** wielu wywołań LLM, narzędzi i źródeł danych.

* **LangChain / LangGraph**: LangChain to kompleksowy framework pozwalający budować złożone łańcuchy (chains) wywołań LLM. LangGraph to jego nowsze rozszerzenie, skupione na tworzeniu cyklicznych grafów, co jest podstawą do budowy zaawansowanych **agentów AI**.
* **Haystack / LlamaIndex**: To frameworki wysoce wyspecjalizowane w budowaniu systemów **RAG**. LlamaIndex skupia się na efektywnym wczytywaniu, indeksowaniu i odpytywaniu Twoich danych (posiada m.in. najlepszy na rynku parser dokumentów `LlamaParse`), podczas gdy Haystack oferuje kompletne narzędzia do budowy produkcyjnych pipeline'ów RAG od A do Z.
* **Pydantic-AI**: Nowa biblioteka, która pozwala na budowanie agentów w oparciu o Pydantic.
* Wiele innych, np. wieloagentowych - CrewAI, Microsoft AutoGen

### Narzędzia Pomocnicze

* **OpenAI SDK**: Oficjalna biblioteka do interakcji z API OpenAI. Niezbędna do pracy z modelami takimi jak GPT-4.
* [**Pydantic**](https://docs.pydantic.dev/latest/): W kontekście GenAI, Pydantic jest kluczowym narzędziem do definiowania **schematu odpowiedzi**, której oczekujemy od LLM. Zamiast prosić o "JSON z imieniem i wiekiem", definiujesz klasę Pydantic i zmuszasz model do zwrócenia 