#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def subfigures(a):
    # Extracting data from the array
    x = a[:, 0]
    y = a[:, 1]
    colors = a[:, 2]
    sizes = a[:, 3]

    # Creating a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plotting the graph in the left subplot
    ax1.plot(x, y)
    ax1.set_title('Line Plot')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    # Plotting the scatter plot in the right subplot
    scatter = ax2.scatter(x, y, c=colors, s=sizes, cmap='viridis')
    ax2.set_title('Scatter Plot')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    
    # Adding a colorbar to the scatter plot
    fig.colorbar(scatter, ax=ax2, label='Color')

    # Display the plot
    plt.tight_layout()
    plt.show()

def main():
    # Example 2D array
    a = np.array([
        [1, 2, 3, 40],
        [2, 3, 4, 50],
        [3, 4, 5, 60],
        [4, 5, 6, 70],
        [5, 6, 7, 80]
    ])
    
    # Calling the subfigures function
    subfigures(a)

# Run the main function to test the solution
if __name__ == "__main__":
    main()
