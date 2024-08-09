import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode

def plant_clustering():
    iris = load_iris()
    X = iris.data
    y = iris.target

    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(X)
    clusters = kmeans.predict(X)

    labels = np.zeros_like(clusters)
    for i in range(3):
        mask = (clusters == i)
        labels[mask] = mode(y[mask])[0]

    accuracy = accuracy_score(y, labels)
    return accuracy

accuracy = plant_clustering()
print(f"Accuracy Score: {accuracy:.2f}")
