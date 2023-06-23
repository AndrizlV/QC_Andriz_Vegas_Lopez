"""from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Classical data to encode: "10"
classical_data = "10"

# Amplitude embedding
for i, bit in enumerate(classical_data):
    if bit == '1':
        qc.x(i)

# Measure the qubits
qc.measure_all()

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1)
result = job.result()
counts = result.get_counts()

# Print the measurement outcome
print("Measurement outcome:", list(counts.keys())[0])

"""
import warnings 
warnings.filterwarnings("ignore")

#import numpy as np

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ, execute
from qiskit.visualization import *
from qiskit.providers.aer import QasmSimulator

from qiskit.quantum_info import Statevector
import numpy as np
import math

# Define the dataset
dataset = np.array([
[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
[0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
])
#print(dataset)

# The norm of the dataset is taken and each component is divided by this norm
normalized_dataset = dataset / np.sqrt(np.sum(np.square(dataset)))
#print(normalized_dataset)

# Proceed with Amplitude Embedding just if the normalization was right
if (np.sum(np.square(normalized_dataset)) == 1):

    # Initialize the quantum circuit
    num_qubits = int(math.ceil(math.log2(np.size(dataset))))
    print(f"Circuit's number of qubits: {num_qubits}")
    qc = QuantumCircuit(num_qubits)

    dataset_flatten = normalized_dataset.flatten()

    # Flatten the array and iterate through each element
    for i in range(np.size(dataset_flatten)):
      Amplitude = dataset_flatten[i]
      binary_string = format(i, '0{}b'.format(num_qubits))
      print(f"Amplitude: {Amplitude} with quantum state: {binary_string}")
    # # Apply amplitude embedding
    # for i, amplitude in enumerate(normalized_dataset):
    #     binary_string = format(i, '0{}b'.format(num_qubits))
    #     print(f"Data No. {i} with value {amplitude}")

    #     for j, bit in enumerate(binary_string):
    #         if bit == '1':
    #             qc.h(j)  # Flip qubit state if the bit is 1

    # Draw the circuit
    qc.measure_all()

    print(qc.draw())
else:
    print("The normalization process has an error. Amplitude embedding cannot be done")