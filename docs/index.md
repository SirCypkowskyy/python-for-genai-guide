<div class="hero" markdown>

<span class="hero-kicker">~/python-for-genai-guide</span>

# Python dla Data Science, ML i GenAI

Szybki start dla doświadczonych programistów C++, C# i Java wchodzących w ekosystem Data Science, Machine Learning i Generative AI - bez zbędnej teorii, z naciskiem na praktyczne różnice i dobre praktyki.

[Zacznij od rozdziału 1](01-philosophy-and-basics.md)
[Repozytorium na GitHubie](https://github.com/SirCypkowskyy/python-for-genai-guide)

<span class="hero-status">8 rozdziałów &middot; od C++/C#/Java do Pythona &middot; open-source &middot; stan wiedzy: maj 2026</span>

</div>

## Ścieżka nauki

Wiedza została podzielona na osiem tematycznych rozdziałów. Zacznij od pierwszego i przechodź kolejno - każdy rozdział zakłada znajomość poprzednich.

<div class="grid cards" markdown>

-   <span class="ch-num">01</span> **[Filozofia i podstawy](01-philosophy-and-basics.md)**

    Dlaczego Python działa inaczej: model wykonania, typowanie, OOP, obsługa błędów.

-   <span class="ch-num">02</span> **[Środowiska i narzędzia](02-environment-and-tools.md)**

    Nowoczesny tooling: `uv`, `ruff`, kontrola typów, Jupyter.

-   <span class="ch-num">03</span> **[Stos Data Science](03-data-science-stack.md)**

    Pandas, NumPy, Polars, DuckDB, Pydantic, wizualizacja danych.

-   <span class="ch-num">04</span> **[Web Development i API](04-web-development.md)**

    FastAPI, Flask, Django, serwery ASGI, model async.

-   <span class="ch-num">05</span> **[Machine Learning](05-machine-learning-guide.md)**

    scikit-learn, PyTorch, gradient boosting, rygor ML, MLOps.

-   <span class="ch-num">06</span> **[GenAI i RAG](06-generative-ai-and-rag.md)**

    LLM-y, RAG, agenci, MCP, bezpieczeństwo aplikacji LLM.

-   <span class="ch-num">07</span> **[Architektura aplikacji](07-architecture-and-good-practices.md)**

    Topologie, podział domenowy, Ports & Adapters, ADR.

-   <span class="ch-num">08</span> **[Słowniczek pojęć](08-glossary.md)**

    Szybkie wyjaśnienia nieznanych terminów.

</div>

## Mapa ekosystemu

Python to przede wszystkim potężny ekosystem bibliotek. Oto najważniejsze obszary, w których będziesz pracować:

* **Analiza danych** - [Pandas](https://pandas.pydata.org/) ("SQL na sterydach"), [NumPy](https://numpy.org/) (fundament obliczeń numerycznych), [Polars](https://pola.rs/) i [DuckDB](https://duckdb.org/) dla większej skali.

* **Web i API** - [FastAPI](https://fastapi.tiangolo.com/) (nowoczesne, async API), [Flask](https://flask.palletsprojects.com/) (minimalistyczny micro-framework), [Django](https://www.djangoproject.com/) (batteries-included).

* **Machine Learning** - [scikit-learn](https://scikit-learn.org/) (klasyczny ML), [PyTorch](https://pytorch.org/) (dominujący framework deep learningu), gradient boosting (XGBoost, LightGBM, CatBoost).

* **Generative AI** - frameworki orkiestracji ([LangGraph](https://langchain-ai.github.io/langgraph/), [LlamaIndex](https://www.llamaindex.ai/), [PydanticAI](https://ai.pydantic.dev/)), wzorzec **RAG** oraz **MCP (Model Context Protocol)** do łączenia agentów z narzędziami.

> [!TIP]
> Zanim zaczniesz pisać kod, poznaj współczesny tooling: napisane w Rust [**uv**](https://docs.astral.sh/uv/) (zunifikowany menedżer projektów) i [**Ruff**](https://docs.astral.sh/ruff/) (błyskawiczny linter i formatter). Szczegóły w rozdziale [Środowiska i narzędzia](02-environment-and-tools.md).

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
