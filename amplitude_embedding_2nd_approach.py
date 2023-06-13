from qiskit import QuantumCircuit, transpile, assemble, Aer, execute, ClassicalRegister, QuantumRegister
import cv2, math
import numpy as np
import matplotlib.pyplot as plt

# Config for console outcome
np.set_printoptions(threshold=np.inf)

# Load the image
image = cv2.imread('space_invader.png')

# Normalize the pixel values to range [0, 1] for Amplitude Embedding
normalized_image = image / 255.0

# Flatten the image into a 1D vector
dataset = normalized_image.flatten()

# Flattened image lenght (dataset): 91 140
#print("Flattened image len:", len(flattened_image))

# Define the number of qubits required based on the image size
num_qubits = int(math.ceil(math.log2(len(dataset))))

# Quantum circuit creation
qc = QuantumCircuit(num_qubits, num_qubits)

#X-gate is applied to all qubits:
#qc.x([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

for value in dataset:
    # Convert the normalized value to binary string representation
    binary_value = format(int(value * (2**num_qubits - 1)), f'0{num_qubits}b')

print(binary_value)

#Measure all the qubits
qc.measure_all()

# Draw the qcircuit using Matplot library
qc.draw(output='mpl')
#plt.show()

#print(dataset[0])


