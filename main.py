# Biblioteki
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# Zadanie 1
# Przygotowanie środowiska i danych

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print(f"df.head()\n{df.head()}\n")

print(f"df.info()")
print(df.info())

print(f"\ndf.describe()\n{df.describe()}\n")

# Zadanie 2
# Stworzenie prostego modelu ML - Wariant A: scikit-learn

X = df
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.3,random_state=42
)

print(f"Rozmiar X_train: {X_train.shape}")
print(f"Rozmiar X_test: {X_test.shape}")

print(f"\nX_train.head()\n{X_train.head()}")

import category_encoders as ce
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Wybór i wytrenowanie modelu
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predykcja
y_pred = model.predict(X_test)

# Wyświetlenie rozszerzonych metryk
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")
print("\nFull Classification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# Feature Importance
feature_scores = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nIstotność cech:")
print(feature_scores)

# Zadanie 3
# Zapisanie i ładowanie modelu - Pickle

import pickle
with open('RFC_Model', 'wb') as f:
    pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)

# load_model.py - zapisać w osobnym pliku
with open('RFC_Model', 'rb') as f:
    data = pickle.load(f)

sample_data = [[5.1, 3.5, 1.4, 0.2]] # sepal length, sepal width, petal length, petal width

# Zadanie 4: Wersjonowanie modelu w praktyce

