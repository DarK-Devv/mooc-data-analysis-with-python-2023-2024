#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def to_grayscale(image):
    # Use the provided weights to convert the image to grayscale
    gray = 0.2126 * image[:, :, 0] + 0.7152 * image[:, :, 1] + 0.0722 * image[:, :, 2]
    return gray

def to_red(image):
    # Create a copy of the image and zero out the green and blue channels
    red_image = image.copy()
    red_image[:, :, 1] = 0  # Zero out green channel
    red_image[:, :, 2] = 0  # Zero out blue channel
    return red_image

def to_green(image):
    # Create a copy of the image and zero out the red and blue channels
    green_image = image.copy()
    green_image[:, :, 0] = 0  # Zero out red channel
    green_image[:, :, 2] = 0  # Zero out blue channel
    return green_image

def to_blue(image):
    # Create a copy of the image and zero out the red and green channels
    blue_image = image.copy()
    blue_image[:, :, 0] = 0  # Zero out red channel
    blue_image[:, :, 1] = 0  # Zero out green channel
    return blue_image

def main():
    # Load the image
    image = mpimg.imread('src/painting.png')
    
    # Convert to grayscale
    gray_image = to_grayscale(image)
    
    # Display grayscale image
    plt.figure(figsize=(8, 6))
    plt.imshow(gray_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')
    plt.show()
    
    # Convert to red, green, and blue images
    red_image = to_red(image)
    green_image = to_green(image)
    blue_image = to_blue(image)
    
    # Create a figure with three subplots
    fig, axes = plt.subplots(3, 1, figsize=(8, 18))
    
    # Display red image
    axes[0].imshow(red_image)
    axes[0].set_title('Red Channel')
    axes[0].axis('off')
    
    # Display green image
    axes[1].imshow(green_image)
    axes[1].set_title('Green Channel')
    axes[1].axis('off')
    
    # Display blue image
    axes[2].imshow(blue_image)
    axes[2].set_title('Blue Channel')
    axes[2].axis('off')
    
    # Show the plots
    plt.tight_layout()
    plt.show()

# Run the main function to test the solution
if __name__ == "__main__":
    main()

