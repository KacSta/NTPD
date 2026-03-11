import pickle

with open('RFC_Model', 'rb') as f:
    data = pickle.load(f)

sample_data = [[5.1, 3.5, 1.4, 0.2]] # sepal length, sepal width, petal length, petal width

prediction = data.predict(sample_data)

print(f"Wynik predykcji dla danych {sample_data}: {prediction}")