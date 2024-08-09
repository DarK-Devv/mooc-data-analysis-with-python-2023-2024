import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
from scipy.optimize import linear_sum_assignment

def load_data():
    return pd.read_csv('src/data.tsv', sep='\t')

def find_permutation(n_clusters, true_labels, cluster_labels):
    permutation = []
    for i in range(n_clusters):
        idx = cluster_labels == i
        if np.sum(idx) == 0:
            continue
        new_label = np.bincount(true_labels[idx]).argmax()
        permutation.append(new_label)
    return permutation

def compute_accuracy(true_labels, cluster_labels):
    non_outliers = cluster_labels != -1
    if len(set(cluster_labels[non_outliers])) != len(set(true_labels)):
        return np.nan
    permutation = find_permutation(len(set(true_labels)), true_labels[non_outliers], cluster_labels[non_outliers])
    new_labels = np.zeros_like(cluster_labels)
    for i, label in enumerate(set(cluster_labels[non_outliers])):
        new_labels[cluster_labels == label] = permutation[i]
    return accuracy_score(true_labels[non_outliers], new_labels[non_outliers])

def nonconvex_clusters():
    data = load_data()
    results = []
    X = data[['X1', 'X2']].values
    y = data['y'].values
    eps_values = np.arange(0.05, 0.2, 0.05)
    
    for eps in eps_values:
        dbscan = DBSCAN(eps=eps)
        cluster_labels = dbscan.fit_predict(X)
        accuracy = compute_accuracy(y, cluster_labels)
        n_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
        n_outliers = np.sum(cluster_labels == -1)
        results.append((eps, accuracy, n_clusters, n_outliers))
    
    result_df = pd.DataFrame(results, columns=['eps', 'Score', 'Clusters', 'Outliers'])
    result_df = result_df.astype({'eps': 'float', 'Score': 'float', 'Clusters': 'float', 'Outliers': 'float'})
    return result_df

if __name__ == "__main__":
    result_df = nonconvex_clusters()
    print(result_df)
