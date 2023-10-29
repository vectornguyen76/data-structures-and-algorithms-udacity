import sys
import heapq


def encoded_text(huffman_dict, data):
    """
    Encodes the input data using the Huffman dictionary.

    :param huffman_dict: Huffman dictionary mapping characters to binary codes
    :param data: Input data to be encoded
    :return: Encoded binary data
    """
    huffcode = ''
    for c in data:
        huffcode += str(huffman_dict[c])
    return huffcode


def huffman_encoding(data):
    """
    Perform Huffman encoding on the input data.

    :param data: Input data to be encoded
    :return: Encoded binary data and Huffman tree
    """
    
    huff = dict()
    global huffman_dict
    huffman_dict = {}

    # Calculate character frequencies
    for char in data:
        huff[char] = huff.get(char, 0) + 1

    # Transform the frequencies into a heap tree structure
    heap = [[frequency, [symbol, '']] for symbol, frequency in huff.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        huffman_dict[heap[0][1][0]] = str(heap[0][0])
        huffcode = encoded_text(huffman_dict, data)
        return huffcode, heap

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Add '0' to left and '1' to right
        for value in left[1:]:
            value[1] = '0' + value[1]
        for value in right[1:]:
            value[1] = '1' + value[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    # Create a dictionary of character-to-binary code mappings
    huffman_list = right[1:] + left[1:]
    huffman_dict = {a[0]: str(a[1]) for a in huffman_list}
    huffcode = encoded_text(huffman_dict, data)

    return huffcode, heap


def huffman_decoding(data,tree):
    """
    Decode the Huffman-encoded data using the Huffman tree.

    :param data: Huffman-encoded binary data
    :return: Decoded text
    """
    decoded_text = ''
    current_code = ''

    for bit in data:
        current_code += bit

        if current_code in huffman_dict.values():
            for key in huffman_dict:
                if current_code == huffman_dict[key]:
                    decoded_text += key
                    current_code = ""
    return decoded_text


if __name__ == "__main__":
    test_cases = [
        "The bird is the word",
        "AAAAAAAAAA",
        "",
        "ssddffssccwww",
        "qqdddssff33221saaaaaaaaaaaaaaaaaaaaaaaaaadasdasdasdadasd"
    ]

    for i, data in enumerate(test_cases, 1):
        print(f'***** Testcase {i} *****')
        print("The size of the data is:", sys.getsizeof(data))
        print("The content of the data is:", data)
        if data == "":
            print("No data to encode!")
            continue
        
        encoded_data, tree = huffman_encoding(data)
        print("The size of the encoded data is:", sys.getsizeof(int(encoded_data, base=2)))
        print("The content of the encoded data is:", encoded_data)
        decoded_data = huffman_decoding(encoded_data, tree)
        print("The size of the decoded data is:", sys.getsizeof(decoded_data))
        print("The content of the decoded data is:", decoded_data)
        print()
