# Problem 5: Autocomplete with Tries

This is a Python implementation of a Trie data structure, used for efficient storage and retrieval of words. The Trie is composed of two main classes: `TrieNode` and `Trie`. The provided code defines the structure of these classes and includes some test cases.

## TrieNode

The `TrieNode` class represents a single node in the Trie. Each node contains the following attributes:

- `is_word`: A boolean flag that indicates whether the node represents the end of a word.
- `children`: A dictionary that maps characters to child nodes.

The following methods are defined for `TrieNode`:

- `find_words(self, prefix)`: This method finds all words in the Trie starting with the given `prefix`. It recursively traverses the Trie and collects matching words.

- `insert(self, char)`: This method inserts a new character as a child of the current node.

## Trie

The `Trie` class is the main structure that contains the root node and provides the following methods:

- `insert(self, word)`: This method adds a word to the Trie. It iterates through each character of the word, creating nodes as needed and marking the final node as the end of a word.

- `find(self, prefix)`: This method finds the Trie node that represents a given `prefix`. It traverses the Trie following the characters in the prefix and returns the corresponding node.

- `match(self, prefix)`: This method returns all matching words in the Trie for a given `prefix`. It uses the `find` method to locate the appropriate node and then calls the `find_words` method of that node to retrieve matching words.

## Time Complexity

- The time complexity for inserting a word into the Trie is O(L), where L is the length of the word.
- The time complexity for finding a Trie node for a given prefix is also O(L).
- The time complexity for finding all words with a given prefix is O(K), where K is the total number of words with that prefix.

## Space Complexity

- The space complexity of the Trie depends on the number of unique characters in the words and the number of words. In the worst case, if all words have unique characters, the space complexity is O(N), where N is the total number of characters in all the words.
