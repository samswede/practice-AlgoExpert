import unittest
from hypothesis import given, strategies as st

def twoColorable(edges):
    """
    Checks if the given graph is two-colorable.

    Args:
        edges (list of list of int): The adjacency list representation of the graph.
    
    Returns:
        bool: True if the graph is two-colorable, False otherwise.
    """
    # Number of nodes in the graph
    number_of_nodes = len(edges)
    # Initialize all nodes with None (unvisited)
    colors = [None] * number_of_nodes

    for node in range(number_of_nodes):
        # Check unvisited nodes
        if colors[node] is None:
            if not twoColorDFS(edges):
                return False

    return True

def twoColorDFS(edges, node, colors, current_color=1):
    """
    Performs a DFS on the given graph and checks if it is two-colorable.

    The problem with this code is that it exceeds the maximum recursion depth...

    Args:
        edges (list of list of int): The adjacency list representation of the graph.
        node (int): The current node in the DFS.
        colors (list of int): The list used to store the color of each node.
        current_color (int): The current color to assign (1 or -1).

    Returns:
        bool: True if the graph is two-colorable, False otherwise.
    """
    # Check if the current node is unvisited
    if colors[node] is None:
        colors[node] = current_color
    elif colors[node] != current_color:
        return False

    # Process all the adjacent nodes
    for adj_node in edges[node]:
        # Change to 'adj_node' to avoid variable name conflict
        if not twoColorDFS(edges, adj_node, colors, -current_color):
            return False
    
    return True

def twoColorDFS(edges, start_node, colors):
    """
    Performs an iterative DFS on the given graph and checks if it is two-colorable.

    This code is correct but it is not the best solution because it uses a stack,
    which is a data structure that is not constant space.

    Args:
        edges (list of list of int): The adjacency list representation of the graph.
        start_node (int): The starting node for the DFS.
        colors (list of int): The list used to store the color of each node.

    Returns:
        bool: True if the graph is two-colorable, False otherwise.
    """
    stack = [(start_node, 1)]  # Start with the starting node and color 1

    while stack:
        node, current_color = stack.pop()
        if colors[node] is None:
            colors[node] = current_color
        elif colors[node] != current_color:
            return False

        # Add adjacent nodes to the stack with the opposite color
        for adj_node in edges[node]:
            if colors[adj_node] is None:
                stack.append((adj_node, -current_color))

    return True


def twoColorDFS(edges):

    currentNode = 0
    currentNodeColor = True

    colors = [None] * len(edges)
    stack = [(currentNode, currentNodeColor)]
    while len(stack) > 0:
        node, currentColor = stack.pop()
        if colors[node] is None:
            colors[node] = currentColor
        elif colors[node] is not currentColor:
            return False
        for adjNode in edges[node]:
            if colors[adjNode] is None:
                stack.append((adjNode, not currentColor))


def twoColorable(adjacency_list):
    """
    Determine if a graph represented by an adjacency list is two-colorable.

    A graph is two-colorable (or bipartite) if its vertices can be divided into two sets such that
    no two adjacent vertices are in the same set. This function uses a depth-first search (DFS)
    approach to try to color the graph using two colors, represented by True and False.

    O(v + e) time | O(v) space

    Args:
        adjacency_list (list of list of int): Adjacency list representation of the graph.
                                             Each list contains the indices of adjacent nodes.

    Returns:
        bool: True if the graph is two-colorable, False otherwise.
    """

    # Initialize colors for each node. None indicates that the node has not been visited.
    colors = [None for _ in range(len(adjacency_list))]

    # Start coloring from the first node (index 0) with True.
    colors[0] = True

    # Initialize the stack with the first node.
    stack = [0]

    # Perform DFS until the stack is empty.
    while len(stack) > 0:
        # Pop the last node from the stack.
        node = stack.pop()

        # Get all the edges (adjacent nodes) of the current node.
        edges = adjacency_list[node]

        # Iterate through each adjacent node.
        for edge in edges:
            # If the adjacent node has not been visited,
            # color it with the opposite color of the current node.
            if colors[edge] is None:
                colors[edge] = not colors[node]
                # Add this adjacent node to the stack for further exploration.
                stack.append(edge)
            # If the adjacent node has been visited and has the same color as the current node,
            # the graph is not two-colorable.
            elif colors[edge] == colors[node]:
                return False
            
    # If the entire graph has been successfully colored with two colors, return True.
    return True


class Tests(unittest.TestCase):

    def test_base_cases(self):
        self.assertIsInstance(twoColorable([[1], [0]]), bool)

    def test_known_value1(self):
        self.assertEqual(twoColorable([[1, 3], [0, 2], [1, 3], [0, 2]]), True)

    def test_known_value2(self):
        self.assertEqual(twoColorable([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]), False)

    def test_known_value4(self):
        self.assertEqual(twoColorable([[1, 2], [0, 3], [0, 3], [1, 2]]), True)

    def test_known_value6(self):
        self.assertEqual(twoColorable([[1, 2], [0, 2, 3], [0, 1, 3], [0, 1, 2]]), False)
    






if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)