# Problem 7: Request Routing in a Web Server with a Trie

This code implements a route handling system using a Route Trie and a Router. The Route Trie is used to store routes and their associated handlers, and the Router class handles the routing of incoming requests to the appropriate handlers.

## RouteTrie

The `RouteTrie` class is responsible for storing routes and their handlers. It uses a tree structure where each node represents a part of the route. The key functions of the `RouteTrie` class are:

- `insert(self, path_parts, handler)`: Inserts a route into the Route Trie by iteratively creating nodes for each part of the route and associating the final node with the given handler.

- `find(self, path_parts)`: Searches for a route in the Route Trie by traversing the tree according to the path parts. If the full route is found, it returns the associated handler; otherwise, it returns None.

## RouteTrieNode

The `RouteTrieNode` class represents a single node in the Route Trie. It contains a dictionary of children nodes and an optional handler associated with the route ending at that node.

## Router

The `Router` class wraps the Route Trie and provides high-level functionality for adding handlers to routes and looking up handlers for specific routes. It contains the following key methods:

- `add_handler(self, path, handler)`: Adds a handler for a specific route by splitting the path into parts and inserting it into the Route Trie.

- `lookup(self, path)`: Looks up and returns the handler associated with a specific route.

- `split_path(self, path)`: Splits a route path into its constituent parts. This is useful for parsing and processing route paths.

## Efficiency

- **Time Complexity**:

    - Insertion of a route into the Route Trie has a time complexity of O(K), where K is the number of parts (segments) in the route. This is because we iterate through each part of the route to insert it into the trie.
    
    - Looking up a route in the Route Trie also has a time complexity of O(K) since it involves iterating through the parts of the route to find the associated handler.

    - Splitting a route path into parts has a time complexity of O(N), where N is the length of the path. In the worst case, this is a linear operation.

- **Space Complexity**:

    - The space complexity of the Route Trie depends on the number of unique route parts and the number of routes. In the worst case, where all routes are distinct, the space complexity is O(N), where N is the total number of parts in all routes.
