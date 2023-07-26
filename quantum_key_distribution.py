# quantum_key_distribution.py - Quantum Key Distribution Module

import random

class QuantumKeyDistribution:
    def __init__(self):
        self.shared_key = ""

    def generate_key(self, length):
        """
        Generate a random binary key of the specified length.

        Parameters:
        - length (int): The length of the binary key to generate.

        Returns:
        - str: The generated binary key.
        """
        key = ''.join(random.choice('01') for _ in range(length))
        self.shared_key = key

    def apply_quantum_noise(self, error_rate):
        """
        Simulate quantum noise in the shared key.

        Parameters:
        - error_rate (float): The probability of a bit flip due to quantum noise.
        """
        noisy_key = ""
        for bit in self.shared_key:
            noisy_bit = bit if random.random() > error_rate else '1' if bit == '0' else '0'
            noisy_key += noisy_bit
        self.shared_key = noisy_key

# Example usage:
if __name__ == "__main__":
    qkd = QuantumKeyDistribution()

    # Generate a key of length 20
    qkd.generate_key(20)
    print("Original Key:", qkd.shared_key)

    # Simulate quantum noise with an error rate of 10%
    qkd.apply_quantum_noise(0.1)
    print("Noisy Key:", qkd.shared_key)
