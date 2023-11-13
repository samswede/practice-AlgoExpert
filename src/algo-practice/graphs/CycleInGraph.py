# Input: List of edges
# Output: Boolean indicating if there is a cycle in the graph

# Input example:
# edges = [
#     [1, 3],
#     [2, 3, 4],
#     [0],
#     [],
#     [2, 5],
#     []
# ]

# Output example:
# True


def threeColorDFS(edges, index, colors= None):
    """
    Perform a depth-first search (DFS) to detect a cycle in a directed graph using a three-color marking scheme.

    The nodes are marked with three colors:
    - White (0): Unvisited nodes.
    - Gray (1): Nodes that are currently being visited (in the recursion stack).
    - Black (2): Nodes that have been completely visited.

    A cycle is detected if a node being visited (gray) is encountered again.

    Args:
        edges (list of list of int): The adjacency list representation of the graph. 
                                     Each index represents a node, and the list at each index 
                                     contains the nodes that can be reached from that node.
        index (int): The starting index (node) for the DFS.
        colors (list of int): The list used to store the color of each node. It should have
                              the same length as 'edges'. If None, it will be initialized
                              with all nodes marked as white (unvisited).

    Returns:
        bool: True if a cycle is detected in the graph, False otherwise.

    Example:
        >>> graph = [[1, 2], [2], [0, 3], []]
        >>> threeColorDFS(graph, 0, None)
        True
    """

    if colors is None:
        colors = [0] * len(edges)

    # Detect a cycle (back-edge)
    if colors[index] == 1:
        return True

    # Node already completely processed, no cycle found in this path
    if colors[index] == 2:
        return False

    # Mark the current node as being processed (gray)
    colors[index] = 1

    # Recursively process all the adjacent nodes
    for edge in edges[index]:
        if threeColorDFS(edges, edge, colors):
            return True
    
    # Mark the node as completely processed (black)
    colors[index] = 2
    return False


def cycleInGraph(edges):
    """
    Checks if there is a cycle in the given graph.

    Args:
        edges (list of list of int): The adjacency list representation of the graph. 

    Returns:
        bool: True if a cycle is detected in the graph, False otherwise.
    """
    number_of_nodes = len(edges)
    colors = [0] * number_of_nodes

    for node in range(number_of_nodes):
        if colors[node] == 0:
            if threeColorDFS(edges, node, colors):
                return True

    return False

