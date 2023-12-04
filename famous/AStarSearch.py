import unittest
from typing import List

'''
// Create a min heap for F values
minHeap = new minHeap([start])

while minHeap is not empty:
    currentNode = minHeap.pop() // pop the node with the smallest f value
    if currentNode == end:
        break
    for neighbor in currentNode.neighbors:
        if neighbor is obstacle:
            continue
            
        // update F, G, H values
        neighbor.g = currentNode.g + distance(currentNode, neighbor)
        neighbor.h = heuristic_distance(neighbor, end)
        neighbor.f = neighbor.g + neighbor.h

        if neighbor is not in minHeap:
            minHeap.insert(neighbor)
        else:
            minHeap.update(neighbor)


'''

class Node:
    def __init__(self, row, column, isObstacle):
        self.id = str(row) + "-" + str(column)
        self.isObstacle = isObstacle
        self.row = row
        self.column = column

        self.g = float('inf') # distance from start node
        #self.h = float('inf') # heuristic distance from end node
        self.f = float('inf') # g + h = estimated distance from start to end

        self.cameFrom = None

def aStarSearch(startNode, goalNode, graph):
    nodes = initialiseGraph(graph)

    startRow, startCol = startNode[0], startNode[1]
    goalRow, goalCol = goalNode[0], goalNode[1]

    startNode = nodes[startRow][startCol]
    goalNode = nodes[goalRow][goalCol]

    startNode.g = 0
    startNode.f = startNode.g + heuristic_distance(startNode, goalNode)

    nodesToVisit = MinHeap([startNode])

    while not nodesToVisit.isEmpty():
        currentNode = nodesToVisit.remove() # pop the node with the smallest f value
        print(f'currentNode: {currentNode.id}')
        if currentNode == goalNode:
            break

        neighbors = getNeighboringNodes(currentNode, nodes)

        for neighbor in neighbors:
            print(f'considering neighbor {neighbor.id}')

            if neighbor.isObstacle == 1:
                print(f'neighbor {neighbor.id} is an obstacle')
                continue
            tenativeGScore = currentNode.g + 1 # current min distance + distance(currentNode, neighbor)

            if tenativeGScore >= neighbor.g:
                # the neighbor is already closer to the start node
                # therefore, we don't need to update it
                print(f'neighbor {neighbor.id} is already closer to the start node')
                continue
            
            # the neighbor is closer to the start node
            print(f'neighbor {neighbor.id} is closer to the start node')
            neighbor.cameFrom = currentNode

            neighbor.g = tenativeGScore
            neighbor.f = neighbor.g + heuristic_distance(neighbor, goalNode)

            print(f'neighbor {neighbor.id} has g: {neighbor.g}, f: {neighbor.f}')

            if not nodesToVisit.containsNode(neighbor):
                nodesToVisit.insert(neighbor)
                print(f'neighbor {neighbor.id} was not in the heap, so it was inserted')
            else:
                nodesToVisit.update(neighbor)
                print(f'neighbor {neighbor.id} was in the heap, so it was updated')

    return reconstructPath(goalNode)


def reconstructPath(goalNode):
    if not goalNode.cameFrom:
        return [] # there was no path to the goal node
    
    currentNode = goalNode
    path = []

    # traversing backwards from the goal node to the start node
    while currentNode is not None:
        path.append([currentNode.row, currentNode.column])
        currentNode = currentNode.cameFrom

    return list(reversed(path))


def heuristic_distance(node1, node2):
    # Manhattan distance
    return abs(node1.row - node2.row) + abs(node1.column - node2.column)

def initialiseGraph(graph):
    nodes = []
    for row in range(len(graph)):
        nodes.append([])
        for column in range(len(graph[row])):
            nodes[row].append(Node(row, column, graph[row][column]))
    return nodes

def getNeighboringNodes(node, nodes):
    neighbors = []

    numRows = len(nodes)
    numColumns = len(nodes[0])

    row = node.row
    column = node.column

    if row < numRows - 1: # if not last row, DOWN
        neighbors.append(nodes[row + 1][column])
    if row > 0: # if not first row, UP
        neighbors.append(nodes[row - 1][column])
    if column < numColumns - 1: # if not last column, RIGHT
        neighbors.append(nodes[row][column + 1])
    if column > 0: # if not first column, LEFT
        neighbors.append(nodes[row][column - 1])
    return neighbors


# Priority Queue, implemented as a Min Heap.
class MinHeap:
    def __init__(self, array):
        # Holds the position in the heap of each node
        self.nodePositionsInHeap = {node.id: idx for idx, node in enumerate(array)}
        self.heap = self.buildHeap(array)
    def isEmpty(self):
        return len(self.heap) == 0
    
    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx].f < heap[childOneIdx].f:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap].f < heap[currentIdx].f:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
        
    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx].f < heap[parentIdx].f:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        node = self.heap.pop()
        del self.nodePositionsInHeap[node.id]
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return node

    # O(log(n)) time | O(1) space
    def insert(self, node):
        self.heap.append(node)
        self.nodePositionsInHeap[node.id] = len(self.heap) - 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        self.nodePositionsInHeap[heap[i].id] = j
        self.nodePositionsInHeap[heap[j].id] = i
        heap[i], heap[j] = heap[j], heap[i]

    def containsNode(self, node):
        return node.id in self.nodePositionsInHeap
    

    def update(self, node):
        self.siftUp(self.nodePositionsInHeap[node.id], self.heap)


def visualize_search(inputs):
    # Extracting inputs
    startNode = inputs['startNode']
    goalNode = inputs['goalNode']
    graph = inputs['graph']
    path = inputs['path']

    # Creating a copy of the graph to modify
    visualized_graph = [row[:] for row in graph]

    # Marking the path in the graph
    # 2 for start, 3 for path, 4 for goal
    for step in path:
        row, column = step
        visualized_graph[row][column] = 3

    # Marking start and goal nodes
    visualized_graph[startNode[0]][startNode[1]] = 2
    visualized_graph[goalNode[0]][goalNode[1]] = 4

    return visualized_graph

import matplotlib.pyplot as plt
import numpy as np


def plot_visualized_graph(visualized_graph):
    # Convert the visualized_graph to a NumPy array for easier handling with matplotlib
    visualized_graph = np.array(visualized_graph)

    # Create a color map for the visualization
    colors = ['white', 'black', 'green', 'blue', 'red']
    cmap = plt.cm.colors.ListedColormap(colors)

    # Create a figure and axis object, adjusting the figure size dynamically based on the graph
    fig, ax = plt.subplots(figsize=(visualized_graph.shape[1]/2, visualized_graph.shape[0]/2))

    # Display the image
    cax = ax.imshow(visualized_graph, cmap=cmap)

    # Create a color bar
    bounds = [0, 1, 2, 3, 4, 5]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)
    plt.colorbar(cax, ax=ax, boundaries=bounds, ticks=[0, 1, 2, 3, 4])

    # Set axis labels
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')

    # Set title
    ax.set_title('Visualized Search Path')

    # Show the plot
    plt.show()



class Tests(unittest.TestCase):

    def test_base_cases(self):
        self.assertIsInstance(aStarSearch(), List)


    def test_case_1(self):
        test_1 = {
        "startNode": [0, 1],
        "goalNode": [4, 3],
        "graph": [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0]
                ],
        "path": [
                    [0, 1],
                    [0, 0],
                    [1, 0],

                    [2, 0],
                    [2, 1],

                    [3, 1],
                    [4, 1],
                    [4, 2],
                    [4, 3]
                ],
        "return": [
                    [2, 2, 0, 0, 0],
                    [2, 1, 1, 1, 0],
                    [2, 2, 0, 0, 0],
                    [1, 2, 1, 1, 1],
                    [0, 2, 2, 2, 0]
                ]
        }
        self.assertEqual(aStarSearch(graph=test_1['graph'], start=test_1['startNode'], goal=test_1['goalNode']), test_1['path'])
    def test_case_2(self):
        {
  "startRow": 1,
  "startCol": 1,
  "endRow": 8,
  "endCol": 8,
  "graph": [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  ]
}
        test_2 = {
        "startNode": [1, 1],
        "goalNode": [8, 8],
        "graph": [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                ],
        "path": [
                    [0, 1],
                    [0, 0],
                    [1, 0],

                    [2, 0],
                    [2, 1],

                    [3, 1],
                    [4, 1],
                    [4, 2],
                    [4, 3]
                ]
        }
        self.assertEqual(aStarSearch(graph=test_2['graph'], start=test_2['startNode'], goal=test_2['goalNode']), test_2['path'])
 

if __name__ == "__main__":
    #unittest.main(argv=['first-arg-is-ignored'], exit=False)
    inputs = {}
    inputs['startNode'] = [1, 1]
    inputs['goalNode'] = [8, 8]
    inputs['graph'] = [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                ]
    
    path = aStarSearch(startNode=inputs['startNode'], goalNode=inputs['goalNode'], graph=inputs['graph'])
    print(f'path: {path}')
    inputs['path'] = path
    visualized_graph = visualize_search(inputs)
    plot_visualized_graph(visualized_graph)

