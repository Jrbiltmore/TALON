# blockchain_space_data_management.py - Blockchain for Space Data Management Module

import hashlib
import datetime
import json

class BlockchainSpaceData:
    def __init__(self):
        self.chain = []
        self.pending_data = []

        # Genesis block
        self.add_block(previous_hash='0', proof=100)

    def add_block(self, proof, previous_hash=None):
        """Add a new block to the blockchain."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'data': self.pending_data,
            'proof': proof,
            'previous_hash': previous_hash or self.hash_block(self.chain[-1])
        }
        self.pending_data = []
        self.chain.append(block)

    def add_data_to_block(self, data):
        """Add data to be included in the next block."""
        self.pending_data.append(data)

    def hash_block(self, block):
        """Create a SHA-256 hash of a block."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """Find a number (proof) that, when hashed with the previous proof, produces a hash with leading zeros."""
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """Check if the proof is valid by verifying if the hash contains leading zeros."""
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Example: Adjust the number of leading zeros for difficulty level.

# Example usage:
if __name__ == "__main__":
    space_data_blockchain = BlockchainSpaceData()
    space_data_blockchain.add_data_to_block("Satellite telemetry data")
    space_data_blockchain.add_data_to_block("Astronomical observations")
    space_data_blockchain.add_data_to_block("Spacecraft sensor readings")

    # Mining a new block
    last_block = space_data_blockchain.chain[-1]
    last_proof = last_block['proof']
    proof = space_data_blockchain.proof_of_work(last_proof)
    space_data_blockchain.add_block(proof)

    # Display the blockchain
    print(json.dumps(space_data_blockchain.chain, indent=4))
