import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    data = pd.read_csv('src/data.tsv', sep='\t')
    
    variances = data.var().values
    
    pca = PCA()
    pca.fit(data)
    
    explained_variances = pca.explained_variance_
    
    return variances, explained_variances

def main():
    variances, explained_variances = explained_variance()
    
    print("The variances are: " + " ".join(f"{v:.3f}" for v in variances))
    
    print("The explained variances after PCA are: " + " ".join(f"{ev:.3f}" for ev in explained_variances))
    
    cumulative_explained_variance = np.cumsum(explained_variances)
    plt.plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, marker='o')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('Cumulative Explained Variance by PCA Components')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
