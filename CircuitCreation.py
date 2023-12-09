import pennylane as qml


def encoded(name1, name2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    binary_encoding = {alphabet[i]: format(i, '05b') for i in range(len(alphabet))}

    name1_binary = ''.join([binary_encoding[char] for char in name1.lower() if char in alphabet])
    name2_binary = ''.join([binary_encoding[char] for char in name2.lower() if char in alphabet])

    total_length = max(len(name1_binary), len(name2_binary))
    num_qubits = (total_length + 4) // 5  # Each qubit can represent 5 bits

    # Create the quantum circuit
    dev = qml.device('default.qubit')

    @qml.qnode(dev)
    def circuit():
        # Apply gates based on the binary encoding
        for i, bit in enumerate(name1_binary):
            if bit == '1':
                qml.PauliX(wires=i // 5)

        for i, bit in enumerate(name2_binary):
            if bit == '1':
                qml.PauliX(
                    wires=num_qubits // 2 + i // 5)

        return qml.probs(wires=range(num_qubits))

    return circuit


# Encode the names "Nicholas" and "Xanadu"
my_circuit = encoded("nicholas", "xanadu")

# Visualize the circuit
qml.drawer.use_style('black_white')
fig, ax = qml.draw_mpl(my_circuit)()
fig.show()
