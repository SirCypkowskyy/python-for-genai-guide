# 5. Przewodnik po Machine Learningu: Trenowanie Modeli w Pythonie

> [!NOTE]
> Python jest niekwestionowanym liderem i *lingua franca* w świecie Machine Learningu (ML). Jego biblioteki oferują spójne i potężne narzędzia do implementacji zarówno klasycznych algorytmów, jak i najnowocześniejszych, głębokich sieci neuronowych. W tej sekcji poznasz kluczowe frameworki, które stanowią fundament pracy każdego specjalisty danych.

---

## 🏛️ [Scikit-Learn](https://scikit-learn.org/): Fundament Klasycznego Machine Learningu

Jeśli dopiero zaczynasz swoją przygodę z uczeniem maszynowym w Pythonie, [**Scikit-Learn**](https://scikit-learn.org/) to absolutnie **najlepszy punkt startu**. To potężna i jednocześnie niezwykle przyjazna biblioteka, która gromadzi w jednym miejscu dziesiątki sprawdzonych algorytmów klasycznego ML.

### Filozofia: Spójny i Prosty Interfejs

Największą siłą [Scikit-Learn](https://scikit-learn.org/) jest ujednolicony interfejs dla wszystkich algorytmów. Niezależnie od tego, czy budujesz model regresji liniowej, las losowy czy system klastrowania, podstawowe kroki są zawsze takie same:

1.  **Inicjalizacja modelu**: `model = RandomForestClassifier()`
2.  **Trenowanie modelu**: `model.fit(X_train, y_train)`
3.  **Przewidywanie na nowych danych**: `predictions = model.predict(X_test)`

Ta spójność drastycznie obniża próg wejścia i pozwala skupić się na zrozumieniu danych i samego problemu, a nie na walce z różnymi API.

### Dokumentacja jako Interaktywny Podręcznik

Dokumentacja [Scikit-Learn](https://scikit-learn.org/) to w praktyce **darmowy, interaktywny podręcznik do podstaw uczenia maszynowego**. Każdy algorytm jest opatrzony nie tylko przykładami kodu, ale również szczegółowymi wyjaśnieniami matematycznymi, intuicjami, zaletami, wadami i najlepszymi praktykami. Jest to nieocenione źródło wiedzy, które będzie Ci towarzyszyć przez długi czas.

### Typowy Cykl Pracy w Scikit-Learn

Poniższy przykład ilustruje klasyczny, kompletny proces budowy i oceny modelu klasyfikacyjnego.

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Załóżmy, że X to nasze dane (cechy), a y to etykiety (cel)
# X, y = ...

# 1. Podział danych na zbiór treningowy i testowy
# Zbiór treningowy służy do "nauczenia" modelu, a testowy do oceny jego skuteczności
# na danych, których wcześniej nie widział.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Inicjalizacja modelu
# Wybieramy algorytm - w tym przypadku las losowy (RandomForestClassifier).
model = RandomForestClassifier(n_estimators=100)

# 3. Trenowanie modelu
# Metoda .fit() "uczy" model na podstawie danych treningowych.
model.fit(X_train, y_train)

# 4. Przewidywanie na danych testowych
# Używamy wytrenowanego modelu, aby wygenerować predykcje dla zbioru testowego.
predictions = model.predict(X_test)

# 5. Ocena modelu
# Porównujemy predykcje z rzeczywistymi etykietami ze zbioru testowego.
# Metryka accuracy_score mówi nam, jaki procent predykcji był poprawny.
accuracy = accuracy_score(y_test, predictions)
print(f"Dokładność modelu: {accuracy:.4f}")

```

[Scikit-Learn](https://scikit-learn.org/) zapewnia ujednolicony interfejs dla dziesiątek algorytmów, w tym regresji (predykcji wartości ciągłych), klasyfikacji (przypisywania do klas, czyli zbioru dozwolonych odpowiedzi) i klasteryzacji (grupowania obiektów).

-----

## 🧠 [TensorFlow](https://www.tensorflow.org/) i [Keras](https://keras.io/): Wrota do Świata Deep Learningu

Gdy wchodzisz w świat **deep learningu** (głębokich sieci neuronowych), kluczowymi bibliotekami stają się [TensorFlow](https://www.tensorflow.org/) i [Keras](https://keras.io/).

  * [**TensorFlow**](https://www.tensorflow.org/): To potężny, niskopoziomowy silnik obliczeniowy stworzony przez Google. Zapewnia fundamentalne narzędzia do budowania i wykonywania grafów obliczeniowych, które są podstawą działania sieci neuronowych. Jest zoptymalizowany do pracy na dużą skalę, z wykorzystaniem zarówno CPU, jak i akceleratorów sprzętowych takich jak [GPU](https://pl.wikipedia.org/wiki/Procesor_graficzny) i [TPU](https://pl.wikipedia.org/wiki/Tensor_Processing_Unit).

  * [**Keras**](https://keras.io/): To wysokopoziomowe, niezwykle przyjazne dla użytkownika API, które działa na szczycie TensorFlow. Jego celem jest radykalne uproszczenie procesu budowania, trenowania i testowania nawet bardzo skomplikowanych modeli sieci neuronowych. Keras jest obecnie w pełni zintegrowany z TensorFlow jako moduł `tf.keras`, co czyni go standardowym sposobem na pracę z sieciami neuronowymi w tym ekosystemie.

W praktyce, do większości zadań używa się API Keras do szybkiego prototypowania i budowania modeli, a sięga po niższe poziomy TensorFlow, gdy potrzebna jest niestandardowa funkcjonalność lub maksymalna optymalizacja wydajności.