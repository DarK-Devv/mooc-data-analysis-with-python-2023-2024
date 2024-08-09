import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def fit_line(x, y):
    x = x.reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    slope = model.coef_[0]
    intercept = model.intercept_
    return slope, intercept

def main():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])
    
    slope, intercept = fit_line(x, y)
    
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    
    plt.scatter(x, y, color='blue', label='Data points')
    
    y_fit = slope * x + intercept
    plt.plot(x, y_fit, color='red', label='Fitted line')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Regression Fit')
    plt.legend()
    
    plt.show()

if __name__ == "__main__":
    main()
