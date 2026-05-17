# Python - Onboarding dla dewelopera

> [!TIP]
> 📖 **Czytaj online:** [**sircypkowskyy.github.io/python-for-genai-guide**](https://sircypkowskyy.github.io/python-for-genai-guide/) — wygodna wersja przeglądarkowa z wyszukiwarką, nawigacją i trybem ciemnym (generowana automatycznie z tego repozytorium).

> [!NOTE]
> Siema! Ten przewodnik to Twój szybki start w świecie Pythona. Został zaprojektowany, abyś mógł/mogła jak najszybciej wykorzystać swoje dotychczasowe doświadczenie programistyczne do produktywnej pracy w naszym ekosystemie Data Science, Machine Learning i AI.

## Struktura Przewodnika

Ten dokument to tylko wierzchołek góry lodowej. Pełna wiedza została podzielona na tematyczne moduły. Zacznij od pierwszego i przechodź kolejno przez następne.

* **1. 📖 [Filozofia i Podstawy](./docs/01-philosophy-and-basics.md)**: Zrozum, dlaczego Python działa inaczej.
* **2. 🛠️ [Środowiska i Narzędzia](./docs/02-environment-and-tools.md)**: Naucz się zarządzać projektami jak profesjonalista.
* **3. 📊 [Stos Technologiczny Data Science](./docs/03-data-science-stack.md)**: Poznaj biblioteki do pracy z danymi.
* **4. 🌐 [Web Development i API](./docs/04-web-development.md)**: Twórz backendy i usługi.
* **5. 🤖 [Przewodnik po Machine Learningu](./docs/05-machine-learning-guide.md)**: Trenuj swoje pierwsze modele.
* **6. 🧠 [Aplikacje GenAI i RAG](./docs/06-generative-ai-and-rag.md)**: Buduj inteligentne systemy oparte na LLM.
* **7. 🏛️ [Architektura Aplikacji i Dobre Praktyki](./docs/07-architecture-and-good-practices.md)**: Projektuj systemy, które przetrwają wzrost.
* **8. 📚 [Słowniczek Pojęć](./docs/08-glossary.md)**: Szybko sprawdź nieznane terminy.

## Wprowadzenie

Python to nie tylko język programowania – to cała filozofia pracy, społeczność oraz ekosystem narzędzi, które napędzają współczesną analizę danych, machine learning, sztuczną inteligencję i nowoczesne aplikacje webowe. Jeśli masz już doświadczenie w innych językach, takich jak `C++`, `C#` czy `Java`, ten przewodnik pomoże Ci szybko odnaleźć się w nowym środowisku, zrozumieć kluczowe różnice i wykorzystać swoje dotychczasowe umiejętności w praktyce.

Współczesny Python to narzędzie pierwszego wyboru dla inżynierów danych, analityków, naukowców i deweloperów budujących nowoczesne aplikacje. Jego siła tkwi w prostocie, czytelności oraz ogromnej liczbie gotowych bibliotek, które pozwalają skupić się na rozwiązywaniu realnych problemów, a nie na walce z infrastrukturą czy zawiłościami składni.

Ten przewodnik został stworzony z myślą o osobach, które chcą szybko wejść na wyższy poziom produktywności w ekosystemie Pythona – bez zbędnej teorii, za to z naciskiem na praktyczne różnice, dobre praktyki i najważniejsze narzędzia. Znajdziesz tu porównania z innymi językami, mapę najważniejszych bibliotek oraz wskazówki, jak efektywnie zarządzać środowiskiem pracy.

Niezależnie od tego, czy chcesz analizować dane, budować API, trenować modele ML czy eksperymentować z generatywną AI – Python otwiera przed Tobą nowe możliwości. Zacznijmy tę podróż!

## Ekosystem Narzędzi: Twój Nowy Zestaw

Python to przede wszystkim potężny ekosystem bibliotek. Poniżej znajduje się mapa kluczowych narzędzi, z którymi będziesz pracować.

* **Analiza Danych:** [**Pandas**](https://pandas.pydata.org/) to fundamentalna biblioteka do analizy danych, często opisywana jako "SQL na sterydach", gdzie operacje znane z SQL (WHERE, GROUP BY, JOIN) mają swoje intuicyjne odpowiedniki na obiektach DataFrame. [**NumPy**](https://numpy.org/) jest fundamentem dla wszystkich obliczeń numerycznych, zapewniając niezwykle wydajne, wielowymiarowe tablice i operacje na nich, na których zbudowany jest m.in. Pandas.
* **Web Development & API:** [**FastAPI**](https://fastapi.tiangolo.com/) to nowoczesny, ekstremalnie wydajny framework idealny do budowy API, wykorzystujący asynchroniczność i type hints do automatycznej walidacji danych. [**Flask**](https://flask.palletsprojects.com/en/stable/) to minimalistyczny "micro-framework", dający pełną elastyczność i świetnie nadający się do mniejszych projektów i prototypów. [**Django**](https://www.djangoproject.com/) to potężny framework typu "batteries-included", który dostarcza kompletny zestaw narzędzi (ORM, panel admina) do budowy dużych, złożonych aplikacji.
* **Machine Learning:** [**Scikit-Learn**](https://scikit-learn.org/) jest najlepszym punktem startowym dla klasycznego machine learningu, oferując ujednolicony interfejs dla dziesiątek algorytmów oraz dokumentację, która służy jako praktyczny podręcznik do ML. W świecie deep learningu [**PyTorch**](https://pytorch.org/) jest dziś dominującym frameworkiem — króluje zarówno w badaniach, jak i w nowoczesnych systemach AI, dzięki czytelnemu, "pythonowemu" API i dynamicznemu grafowi obliczeń. Drugim filarem jest [**TensorFlow**](https://www.tensorflow.org/) / [**Keras**](https://keras.io/), gdzie TensorFlow stanowi potężny silnik obliczeniowy, a Keras dostarcza wysokopoziomowe, przyjazne API do budowy i trenowania sieci neuronowych.
* **Generative AI:** Frameworki orkiestracyjne, takie jak [**LangChain**](https://www.langchain.com/) czy [**LlamaIndex**](https://www.llamaindex.ai/), pozwalają budować złożone aplikacje oparte na modelach językowych (LLM), które integrują się z zewnętrznymi narzędziami i źródłami danych. [**LangGraph**](https://langchain-ai.github.io/langgraph/) (w wersji 1.0) wyrósł na domyślny runtime do budowy **agentów AI** — systemów, które planują i wykonują wieloetapowe zadania w pętli rozumowania. Standardem łączenia agentów z zewnętrznymi narzędziami stał się **MCP (Model Context Protocol)** — otwarty protokół nazywany "USB-C dla AI". Kluczową koncepcją pozostaje **RAG (Retrieval-Augmented Generation)**, wzorzec architektoniczny, który "uziemia" odpowiedzi modelu w konkretnej, aktualnej wiedzy, zapobiegając halucynacjom i pozwalając na pracę z prywatnymi danymi.

> [!WARNING]
> Zanim zaczniesz, upewnij się, że rozumiesz, jak zarządzać zależnościami. We współczesnym Pythonie standardem stał się nowoczesny, napisany w Rust tooling — [**uv**](https://docs.astral.sh/uv/) (zunifikowany menedżer projektów i pakietów) oraz [**Ruff**](https://docs.astral.sh/ruff/) (błyskawiczny linter i formatter). Szczegółowe informacje znajdziesz w przewodniku o środowiskach i narzędziach.

## Zasoby do Dalszej Nauki

Poniższe materiały są absolutnie najlepszym punktem startowym i są **całkowicie darmowe**.

### Dokumentacja oficjalna i książki

  * **Oficjalna dokumentacja Pythona (PL)**: https://docs.python.org/pl/3/
  * ***Automate the Boring Stuff with Python***: https://automatetheboringstuff.com/
  * ***Python for Everybody***: https://www.py4e.com/

### Najlepsze kursy wideo

  * ***CS50's Introduction to Programming with Python*** (Harvard): https://cs50.harvard.edu/python/
  * ***Python Programming MOOC*** (Uniwersytet Helsiński): https://programming.mooc.fi/

### Narzędzia

  * **Python Tutor**: https://pythontutor.com/ - wizualizacja wykonania kodu krok po kroku.

---
*Dokumentacja wygenerowana [^1] na podstawie materiałów wewnętrznych.*

[^1]: Ostatnia aktualizacja: 17 maja 2026.