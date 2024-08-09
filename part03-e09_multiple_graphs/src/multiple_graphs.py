#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    # Data for the first graph
    x1 = [2, 4, 6, 7]
    y1 = [4, 3, 5, 1]
    
    # Data for the second graph
    x2 = [1, 2, 3, 4]
    y2 = [4, 2, 3, 1]
    
    # Plot the first graph
    plt.plot(x1, y1, label='Graph 1')
    
    # Plot the second graph
    plt.plot(x2, y2, label='Graph 2')
    
    # Adding title and labels
    plt.title('title')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    
    # Adding legend
    plt.legend()
    
    # Display the plot
    plt.show()

# Run the main function to display the plot
if __name__ == "__main__":
    main()
