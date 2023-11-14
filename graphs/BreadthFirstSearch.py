import unittest
from hypothesis import given, strategies as st

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def breadthFirstSearch(self, array, queue= None, depth=0):
        if depth == 0:
            array.append(self.name)
            queue=[]

        for child in self.children:
            array.append(child.name)
            queue.append(child)

        if len(queue) > 0:
            queue.pop(0).breadthFirstSearch(array, queue, depth+1)
        return array
    
    # The above solution works but is not the best solution.
    # Because we are using recursion, we are using a call stack,
    # which is a data structure that is not constant space.
    

# The following is the solution from AlgoExpert:

# O(v + e) time | O(v) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = []
        queue.append(self)
        
        while len(queue) > 0:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for child in currentNode.children:
                queue.append(child)
            
        return array