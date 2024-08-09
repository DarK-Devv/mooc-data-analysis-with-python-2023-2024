import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def read_lines_from_file(file_path, fraction):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        lines = f.readlines()
    lines = lines[:int(len(lines) * fraction)]
    return lines

def spam_detection(random_state, fraction=0.1):
    ham_lines = read_lines_from_file('src/ham.txt.gz', fraction)
    spam_lines = read_lines_from_file('src/spam.txt.gz', fraction)
    
    all_emails = ham_lines + spam_lines
    labels = [0] * len(ham_lines) + [1] * len(spam_lines)
    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_emails)
    y = np.array(labels)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, train_size=0.75, random_state=random_state)
    
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    test_sample_size = len(y_test)
    misclassified_samples = (y_test != y_pred).sum()
    
    return accuracy, test_sample_size, misclassified_samples

def main():
    accuracy, test_sample_size, misclassified_samples = spam_detection(random_state=0, fraction=0.1)
    print(f"Accuracy: {accuracy}")
    print(f"Test sample size: {test_sample_size}")
    print(f"Misclassified samples: {misclassified_samples}")

if __name__ == "__main__":
    main()
