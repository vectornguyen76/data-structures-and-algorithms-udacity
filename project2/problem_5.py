import hashlib
import datetime


def calc_hash(data, timestamp, prev_hash):
    sha = hashlib.sha256()
    hash_str = data.encode("utf-8") + str(timestamp).encode("utf-8") + prev_hash
    sha.update(hash_str)
    return sha.digest()

class Block():

    def __init__(self, data, timestamp, prev_hash):
        self.timestamp = timestamp
        self.data = data
        self.prev = None
        self.prev_hash = prev_hash
        self.hash = calc_hash(data, timestamp, prev_hash)

    def __repr__(self):
        return (
            f"Block []: {repr(self.data)}\n"
            f"Hash: {repr(self.hash)}\n"
            f"Previous Hash: {repr(self.prev_hash)}\n"
            f"{repr(self.timestamp)}\n"
        ) 

class BlockChain:

    def __init__(self) -> None:
        self.current = None

    def append(self, data):
        current_time = datetime.datetime.utcnow()
        if self.current is None:
            self.current = Block(data, current_time, b'0')
        else:
            new_block = Block(data, current_time, self.current.hash)
            new_block.prev = self.current
            self.current = new_block

    def size(self):
        """Return size of Chain"""

        count = 0
        temp = self.current
        while(temp is not None):
            count += 1
            temp = temp.prev
        return count
    
    def to_list(self):
        """Return a list of Block"""

        list_block = []
        temp = self.current
        while(temp is not None):
            list_block.append(temp)
            temp = temp.prev
        return list_block
    
if __name__ == "__main__":
    """
    Test Case 1: Creating an Empty BlockChain
    """
    print("Test Case 1: Empty BlockChain")
    block_chain_A = BlockChain()
    print("Size:", block_chain_A.size())  # Expecting 0
    print("Blocks in the chain:")
    for item in block_chain_A.to_list():
        print(item)
    print("\n")

    """
    Test Case 2: Creating a BlockChain with One Block (Genesis)
    """
    print("Test Case 2: BlockChain with One Block (Genesis)")
    block_chain_B = BlockChain()
    block_chain_B.append("Genesis")
    print("Size:", block_chain_B.size())  # Expecting 1
    print("Blocks in the chain:")
    for item in block_chain_B.to_list():
        print(item)
    print("\n")

    """
    Test Case 3: Creating a BlockChain with Two Blocks (Genesis and Exodus)
    """
    print("Test Case 3: BlockChain with Two Blocks (Genesis and Exodus)")
    block_chain_C = BlockChain()
    block_chain_C.append("Genesis")
    block_chain_C.append("Exodus")
    print("Size:", block_chain_C.size())  # Expecting 2
    print("Blocks in the chain:")
    for item in block_chain_C.to_list():
        print(item)
    print("\n")

    """
    Test Case 4: Creating a BlockChain with Five Blocks (Genesis, Exodus, Leviticus, Numbers, Deuteronomy)
    """
    print("Test Case 4: BlockChain with Five Blocks (Genesis, Exodus, Leviticus, Numbers, Deuteronomy)")
    block_chain_D = BlockChain()
    block_chain_D.append("Genesis")
    block_chain_D.append("Exodus")
    block_chain_D.append("Leviticus")
    block_chain_D.append("Numbers")
    block_chain_D.append("Deuteronomy")
    print("Size:", block_chain_D.size())  # Expecting 5
    print("Blocks in the chain:")
    for item in block_chain_D.to_list():
        print(item)
    print("\n")
