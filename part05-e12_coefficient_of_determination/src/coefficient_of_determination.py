import pandas as pd
from sklearn.linear_model import LinearRegression

def coefficient_of_determination(file_path='src/mystery_data.tsv'):
    data = pd.read_csv(file_path, sep='\t')
    
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    
    model = LinearRegression()
    
    model.fit(X, y)
    r2_all_features = model.score(X, y)
    
    r2_scores = [r2_all_features]
    
    for i in range(X.shape[1]):
        X_single_feature = X[:, i].reshape(-1, 1)
        model.fit(X_single_feature, y)
        r2_single_feature = model.score(X_single_feature, y)
        r2_scores.append(r2_single_feature)
    
    return r2_scores

def main():
    r2_scores = coefficient_of_determination()
    
    print(f"R2 score with all features: {r2_scores[0]}")
    for i in range(1, len(r2_scores)):
        print(f"R2 score with feature X{i}: {r2_scores[i]}")

if __name__ == "__main__":
    main()
