"""
Kevin Jofroit's mentorship on Quantum Image Processing for Space Applications
assignment: quantum embedding for the space invader image
autor: @Andriz vegas Lopez 
"""

import cv2, math 
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
import numpy as np
import matplotlib.pyplot as plt

# Space color: BGR
# Tuples are inmutable
# Outcome without limits
np.set_printoptions(threshold=np.inf)

# Read the image
image = cv2.imread('space_invader.png')

# Number of pixels estimation
number_of_pixels = image.shape[0]*image.shape[1]

# Number of pixels and Color space estimation
dataset = image.size

# image parameters
print(f"height: {image.shape[0]}, width: {image.shape[1]}, number of pixels: {number_of_pixels}, dataset: {dataset}")

# 
if (dataset == number_of_pixels*image.shape[2]):
    number_of_qubits = math.log2(dataset)
    print("Raw number of qubits: ", round(number_of_qubits, 3))
    print("Number of qubits: ", math.ceil(number_of_qubits))
    print("Test", image[80, 80])

    #image[0,0] = (0, 0, 0)

    qc = QuantumCircuit(math.ceil(number_of_qubits))

    image_test = (image.copy())/255.0   

    # Split the image into channels
    b, g, r = cv2.split(image_test)

    # ----------------------------------------------------- blue
    # Square each value of the blue channel
    squared_b = np.square(b)

    # Add all the squared values of the blue channel
    sum_squared_b = np.sum(squared_b)

    # Take the square root of the resulting sum
    sqrt_sum_squared_b = np.sqrt(sum_squared_b)

    # Assign the square root value to the blue channel
    modified_b = np.copy(b)
    modified_b[:, :] = sqrt_sum_squared_b

    # Merge the modified blue channel back into the image
    modified_image_with_blue = cv2.merge((modified_b, g, r))

    #------------------------------------------------- green 
    # Square each value of the green channel
    squared_g = np.square(g)

    # Add all the squared values of the green channel
    sum_squared_g = np.sum(squared_g)

    # Take the square root of the resulting sum
    sqrt_sum_squared_g = np.sqrt(sum_squared_g)

    # Assign the square root value to the green channel
    modified_g = np.copy(g)
    modified_g[:, :] = sqrt_sum_squared_g

    # Merge the modified blue channel back into the image
    modified_image_with_green = cv2.merge((b, modified_g, r))

    #------------------------------------------------- red
    # Square each value of the green channel
    squared_r = np.square(r)

    # Add all the squared values of the green channel
    sum_squared_r = np.sum(squared_r)

    # Take the square root of the resulting sum
    sqrt_sum_squared_r = np.sqrt(sum_squared_r)

    # Assign the square root value to the green channel
    modified_r = np.copy(r)
    modified_r[:, :] = sqrt_sum_squared_r

    # Merge the modified blue channel back into the image
    modified_image_with_red = cv2.merge((b, g, modified_r))

    # Row to plot for blue channel ----------------------------------------
    fig1, axs = plt.subplots(3, 4)

    axs[0][0].imshow(b)
    axs[0][0].set_title('Pure blue channel')
    axs[0][0].axis('off')

    axs[0][1].imshow(squared_b)
    axs[0][1].set_title('Squared blue channel')
    axs[0][1].axis('off')

    axs[0][2].imshow(modified_b[:, :])
    axs[0][2].set_title('Normalized blue channel')
    axs[0][2].axis('off')

    axs[0][3].imshow(modified_image_with_blue)
    axs[0][3].set_title('Merged with original')
    axs[0][3].axis('off')

    # Row to plot for green channel ----------------------------------------
    axs[1][0].imshow(g)
    axs[1][0].set_title('Pure green channel')
    axs[1][0].axis('off')

    axs[1][1].imshow(squared_g)
    axs[1][1].set_title('Squared green channel')
    axs[1][1].axis('off')

    axs[1][2].imshow(modified_g[:, :])
    axs[1][2].set_title('Normalized green channel')
    axs[1][2].axis('off')

    axs[1][3].imshow(modified_image_with_green)
    axs[1][3].set_title('Merged with original')
    axs[1][3].axis('off')

    # Row to plot for red channel ----------------------------------------
    axs[2][0].imshow(r)
    axs[2][0].set_title('Pure red channel')
    axs[2][0].axis('off')

    axs[2][1].imshow(squared_r)
    axs[2][1].set_title('Squared red channel')
    axs[2][1].axis('off')

    axs[2][2].imshow(modified_r[:, :])
    axs[2][2].set_title('Normalized red channel')
    axs[2][2].axis('off')

    axs[2][3].imshow(modified_image_with_red)
    axs[2][3].set_title('Merged with original')
    axs[2][3].axis('off')

    # Adjust the layout
    plt.tight_layout()

    # Show the plot
    plt.show()

    print(image_test[0][0])
    cv2.imshow('Image', image_test)

    # Wait for a key press to close the window
    cv2.waitKey(0)
