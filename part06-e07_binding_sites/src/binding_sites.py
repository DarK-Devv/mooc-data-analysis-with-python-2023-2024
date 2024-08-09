import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score, pairwise_distances

def toint(nucleotide):
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return mapping[nucleotide]

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    feature_matrix = np.array(df['X'].apply(lambda x: [toint(n) for n in x]).tolist())
    labels = np.array(df['Y'].tolist())
    return feature_matrix, labels

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = (labels == i)
        new_label = max(set(real_labels[idx]), key=list(real_labels[idx]).count)
        permutation.append(new_label)
    return [permutation[label] for label in labels]

def plot_clusters(features, labels, title):
    plt.figure(figsize=(10, 6))
    plt.scatter(features[:, 0], features[:, 1], c=labels, cmap='viridis', marker='o')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.colorbar()
    plt.show()

def cluster_euclidean(filename):
    features, real_labels = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters=2, linkage='average', affinity='euclidean')
    labels = clustering.fit_predict(features)
    labels = np.array(find_permutation(2, real_labels, labels))
    plot_clusters(features, labels, 'Euclidean Clustering')
    return accuracy_score(real_labels, labels)

def cluster_hamming(filename):
    features, real_labels = get_features_and_labels(filename)
    hamming_distance_matrix = pairwise_distances(features, metric='hamming')
    clustering = AgglomerativeClustering(n_clusters=2, linkage='average', affinity='precomputed')
    labels = clustering.fit_predict(hamming_distance_matrix)
    labels = np.array(find_permutation(2, real_labels, labels))
    plot_clusters(features, labels, 'Hamming Clustering')
    return accuracy_score(real_labels, labels)
