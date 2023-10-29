from math import sqrt, pow

def estimated_distance(origin, destination):
    """
    Calculate the estimated distance between two points using Euclidean distance formula.
    
    Args:
        origin (tuple): The coordinates of the origin point (x, y).
        destination (tuple): The coordinates of the destination point (x, y).
        
    Returns:
        float: The estimated distance between the origin and destination points.
    """
    return sqrt(pow((origin[0] - destination[0]), 2) + pow((origin[1] - destination[1]), 2))

def shortest_path(graph, start, end):
    """
    Find the shortest path in a graph using the A* search algorithm.

    Args:
        graph (object): An object representing the graph with intersections and roads.
        start (int): The starting intersection index.
        end (int): The destination intersection index.

    Returns:
        list: A list of intersection indices representing the shortest path from start to end.
    """
    g_cost = {}  # Cost to reach each position from the start position
    est_cost = {}  # Estimated total cost from start to end via this position

    g_cost[start] = 0
    est_cost[start] = estimated_distance(graph.intersections[start], graph.intersections[end])

    closed_set = set()  # Set of closed nodes
    open_set = set([start])  # Set of open nodes
    came_from = {}  # Map of nodes to their predecessors

    while len(open_set) > 0:
        # Get the node in the open set with the lowest estimated total cost
        current = None
        current_f_score = None
        for node in open_set:
            if current is None or est_cost[node] < current_f_score:
                current_f_score = est_cost[node]
                current = node

        # Check if we have reached the goal
        if current == end:
            # Reconstruct and return the path from end to start
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        # Mark the current node as closed
        open_set.remove(current)
        closed_set.add(current)

        for neighbor in graph.roads[current]:
            if neighbor in closed_set:
                continue  # Skip nodes that have already been visited
            tentative_g_score = g_cost[current] + estimated_distance(graph.intersections[current], graph.intersections[neighbor])

            if neighbor not in open_set:
                open_set.add(neighbor)  # Add new node to the open set
            elif tentative_g_score >= g_cost[neighbor]:
                continue  # This g_cost is worse than a previously found path

            # Adopt the better g_cost score
            came_from[neighbor] = current
            g_cost[neighbor] = tentative_g_score
            h_score = estimated_distance(graph.intersections[neighbor], graph.intersections[end])
            est_cost[neighbor] = g_cost[neighbor] + h_score
