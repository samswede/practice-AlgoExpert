
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
    
''' [
  Node { name: 'B', children: [ [Node], [Node] ] },
  Node { name: 'C', children: [] },
  Node { name: 'D', children: [ [Node], [Node] ] }
]
'''
