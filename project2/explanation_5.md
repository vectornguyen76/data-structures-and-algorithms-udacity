# Problem 5: Blockchain

This code provides a basic implementation of a blockchain, which includes a `Block` class for creating blocks and a `BlockChain` class for managing the blockchain.

## `Block` Class

The `Block` class represents a block in the blockchain. It has the following attributes and methods:

- `timestamp`: The timestamp when the block was created.
- `data`: Data stored in the block.
- `prev`: Reference to the previous block (linked list style).
- `prev_hash`: Hash of the previous block.
- `hash`: Hash of the current block, calculated using the `calc_hash` function.

### `__init__(self, data, timestamp, prev_hash)`

The constructor initializes a block with the given data, timestamp, and the hash of the previous block. It also calculates the hash of the current block.

### `__repr__(self)`

This method returns a string representation of the block, including data, hash, previous hash, and timestamp.

## `BlockChain` Class

The `BlockChain` class is responsible for managing the blockchain. It has the following methods:

- `__init__(self)`: Initializes an empty blockchain.

- `append(self, data)`: Appends a new block with the given data to the blockchain.

- `size(self)`: Returns the size of the blockchain, i.e., the number of blocks.

- `to_list(self)`: Returns a list of blocks in the blockchain.

## Hash Calculation

The `calc_hash` function takes data, timestamp, and the previous block's hash as input and calculates the SHA-256 hash of this information. This hash is used for ensuring the integrity of the blockchain.

## Efficiency

- The time efficiency of this code is generally good for appending new blocks because it only calculates the hash of the current block and maintains references to the previous block. Calculating the hash is done using the SHA-256 algorithm, which is reasonably fast.

- The space efficiency is determined by the number of blocks in the blockchain. Each block contains some overhead due to its attributes and references to the previous block. The space complexity of the blockchain can be considered O(n), where 'n' is the number of blocks in the chain.