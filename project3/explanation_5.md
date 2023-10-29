# Problem 5: Autocomplete with Tries

This repository contains a Python implementation of a Trie data structure for efficiently storing and searching words. The Trie is implemented with two classes: `TrieNode` and `Trie`, and is used to search for words based on prefixes.

## Reasoning Behind Code Decisions

1. **TrieNode Class**: The `TrieNode` class represents a single node in the Trie. It is initialized with attributes `is_word`, which indicates if a word ends at that node, and `children`, a dictionary that maps characters to child nodes. The `TrieNode` class includes three main methods:
   - `find_words(prefix)`: This method recursively searches the Trie for words that start with a given prefix and returns a list of matching words.
   - `insert(char)`: This method inserts a character into the node's children dictionary, creating a new node for it.

2. **Trie Class**: The `Trie` class represents the Trie itself. It contains the root node and includes methods for inserting words and searching for words based on prefixes. The `Trie` class includes three main methods:
   - `insert(word)`: This method inserts a word into the Trie by iterating through the characters of the word and creating new nodes as needed.
   - `find(prefix)`: This method finds the Trie node that represents a given prefix, allowing for efficient word lookup.
   - `match(prefix)`: This method returns a list of matching words that start with a given prefix by first finding the corresponding node and then using the `find_words` method of that node.

3. **Efficiency**: The Trie data structure is efficient for storing and searching for words, especially when dealing with prefixes. The time complexity of inserting a word is O(L), where L is the length of the word. The time complexity of searching for words with a given prefix is O(K), where K is the length of the prefix. The Trie structure reduces the time complexity for word search by efficiently eliminating non-matching branches.
