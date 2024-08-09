#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def center(image):
    h, w = image.shape[:2]
    return (h - 1) / 2, (w - 1) / 2

def radial_distance(image):
    h, w = image.shape[:2]
    center_y, center_x = center(image)
    y, x = np.ogrid[:h, :w]
    distance = np.sqrt((y - center_y) ** 2 + (x - center_x) ** 2)
    return distance

def scale(a, tmin=0.0, tmax=1.0):
    a_min, a_max = a.min(), a.max()
    if a_min == a_max:  # Handle the case where all values are the same
        return np.full_like(a, tmin)
    scaled_a = (a - a_min) / (a_max - a_min) * (tmax - tmin) + tmin
    return scaled_a

def radial_mask(image):
    distance = radial_distance(image)
    scaled_distance = scale(distance, tmin=0.0, tmax=1.0)
    mask = 1 - scaled_distance
    return mask

def radial_fade(image):
    mask = radial_mask(image)
    if image.ndim == 3:  # Color image
        faded_image = image * mask[:, :, np.newaxis]
    else:  # Grayscale image
        faded_image = image * mask
    return faded_image

def main():
    # Load the image
    image = mpimg.imread('src/painting.png')
    
    # Create the radial mask
    mask = radial_mask(image)
    
    # Apply the radial fade
    faded_image = radial_fade(image)
    
    # Create a figure with three subplots
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))
    
    # Display the original image
    axes[0].imshow(image)
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    # Display the mask
    axes[1].imshow(mask, cmap='gray')
    axes[1].set_title('Radial Mask')
    axes[1].axis('off')
    
    # Display the faded image
    axes[2].imshow(faded_image)
    axes[2].set_title('Faded Image')
    axes[2].axis('off')
    
    # Show the plots
    plt.tight_layout()
    plt.show()

# Run the main function to test the solution
if __name__ == "__main__":
    main()
