# Python dla Data Science, ML i GenAI

> 📖 **Czytaj online:** [**sircypkowskyy.github.io/python-for-genai-guide**](https://sircypkowskyy.github.io/python-for-genai-guide/) - wygodna wersja przeglądarkowa z wyszukiwarką, nawigacją i trybem ciemnym.

> Siema! Ten przewodnik to Twój szybki start w świecie Pythona. Został zaprojektowany tak, abyś mógł/mogła jak najszybciej wykorzystać dotychczasowe doświadczenie programistyczne do produktywnej pracy w ekosystemie Data Science, Machine Learning i Generative AI.

Jeśli masz już doświadczenie w językach takich jak **C++**, **C#** czy **Java**, ten przewodnik pomoże Ci szybko odnaleźć się w nowym środowisku: zrozumieć kluczowe różnice, poznać współczesny tooling i wykorzystać swoje umiejętności w praktyce - bez zbędnej teorii, za to z naciskiem na praktyczne różnice i dobre praktyki.

## Jak korzystać z przewodnika

Wiedza została podzielona na osiem tematycznych rozdziałów. Zacznij od pierwszego i przechodź kolejno - każdy rozdział zakłada znajomość poprzednich.

| Rozdział | O czym jest |
|---|---|
| **1. [Filozofia i podstawy](./docs/01-philosophy-and-basics.md)** | Dlaczego Python działa inaczej: model wykonania, typowanie, OOP, obsługa błędów. |
| **2. [Środowiska i narzędzia](./docs/02-environment-and-tools.md)** | Nowoczesny tooling: `uv`, `ruff`, kontrola typów, Jupyter. |
| **3. [Stos Data Science](./docs/03-data-science-stack.md)** | Pandas, NumPy, Polars, DuckDB, Pydantic, wizualizacja. |
| **4. [Web Development i API](./docs/04-web-development.md)** | FastAPI, Flask, Django, serwery ASGI, model async. |
| **5. [Machine Learning](./docs/05-machine-learning-guide.md)** | scikit-learn, PyTorch, gradient boosting, rygor ML, MLOps. |
| **6. [GenAI i RAG](./docs/06-generative-ai-and-rag.md)** | LLM-y, RAG, agenci, MCP, bezpieczeństwo aplikacji LLM. |
| **7. [Architektura aplikacji](./docs/07-architecture-and-good-practices.md)** | Topologie, podział domenowy, Ports & Adapters, ADR. |
| **8. [Słowniczek pojęć](./docs/08-glossary.md)** | Szybkie wyjaśnienia nieznanych terminów. |

## Mapa ekosystemu

Python to przede wszystkim potężny ekosystem bibliotek. Oto najważniejsze obszary, w których będziesz pracować:

* **Analiza danych** - [Pandas](https://pandas.pydata.org/) ("SQL na sterydach"), [NumPy](https://numpy.org/) (fundament obliczeń numerycznych), [Polars](https://pola.rs/) i [DuckDB](https://duckdb.org/) dla większej skali.
* **Web i API** - [FastAPI](https://fastapi.tiangolo.com/) (nowoczesne, async API), [Flask](https://flask.palletsprojects.com/) (minimalistyczny micro-framework), [Django](https://www.djangoproject.com/) (batteries-included).
* **Machine Learning** - [scikit-learn](https://scikit-learn.org/) (klasyczny ML), [PyTorch](https://pytorch.org/) (dominujący framework deep learningu), gradient boosting (XGBoost, LightGBM, CatBoost).
* **Generative AI** - frameworki orkiestracji ([LangGraph](https://langchain-ai.github.io/langgraph/), [LlamaIndex](https://www.llamaindex.ai/), [PydanticAI](https://ai.pydantic.dev/)), wzorzec **RAG** oraz **MCP (Model Context Protocol)** do łączenia agentów z narzędziami.

> [!TIP]
> Zanim zaczniesz pisać kod, poznaj współczesny tooling: napisane w Rust [**uv**](https://docs.astral.sh/uv/) (zunifikowany menedżer projektów) i [**Ruff**](https://docs.astral.sh/ruff/) (błyskawiczny linter i formatter). Szczegóły w rozdziale [Środowiska i narzędzia](./docs/02-environment-and-tools.md).

## Zasoby do dalszej nauki

Poniższe materiały są świetnym punktem startowym i są **całkowicie darmowe**:

* **Oficjalna dokumentacja Pythona (PL)** - <https://docs.python.org/pl/3/>
* ***Automate the Boring Stuff with Python*** - <https://automatetheboringstuff.com/>
* ***Python for Everybody*** - <https://www.py4e.com/>
* ***CS50's Introduction to Programming with Python*** (Harvard) - <https://cs50.harvard.edu/python/>
* ***Python Programming MOOC*** (Uniwersytet Helsiński) - <https://programming.mooc.fi/>
* **Python Tutor** (wizualizacja wykonania kodu) - <https://pythontutor.com/>
* **[Boot.dev](https://www.boot.dev/)** - interaktywna ścieżka od Pythona po backend i CS (część darmowa, część płatna)

---

*Stan wiedzy: maj 2026. Przewodnik open-source - [repozytorium na GitHubie](https://github.com/SirCypkowskyy/python-for-genai-guide). Autor: [Cyprian Gburek](https://gburek.dev).*
