# Problem 7: Request Routing in a Web Server with a Trie

This code defines a router using a data structure called RouteTrie. The router is implemented using three classes: RouteTrie, RouteTrieNode, and Router. The router is responsible for handling requests and routing them to the appropriate handlers based on the path.

## Reasoning Behind Code Decisions

1. **RouteTrie Class**: This class represents the router's routing tree. It contains methods to insert routes (with their associated handlers) and find handlers for a given path. The Trie data structure efficiently stores and searches for routes. Each node in the Trie represents a part of the path.

2. **RouteTrieNode Class**: This class defines nodes in the routing tree. Each node has children nodes for different path parts and an optional handler for that specific path. The TrieNode data structure is similar to a prefix tree used for autocomplete.

3. **Router Class**: This class wraps the RouteTrie and handles adding routes with their associated handlers and looking up handlers for a given path. It also provides a "not found" handler to be used when no matching route is found.

4. **Efficiency**: The Trie data structure used in the RouteTrie efficiently handles routing. It reduces the lookup time for routes by efficiently traversing the Trie based on the path components. The time complexity of looking up a route is O(m), where m is the number of path components. Inserting a route into the Trie has a time complexity of O(m).
