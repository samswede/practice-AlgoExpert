# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.

# Iterative Solution

# The iterative solution is more space efficient than the recursive solution.
# This is because the recursive solution uses the call stack to store the
# intermediate values, whereas the iterative solution uses a while loop to
# traverse the tree and does not use the call stack to store intermediate values.

# The callstack is a data structure that stores information about the active
# subroutines of a computer program. The call stack is used to save the
# return address of each active subroutine. If a subroutine is called
# recursively, the return address is saved for each invocation of the subroutine.
# When the subroutine returns, the most recently saved return address is
# retrieved from the call stack, and execution continues at that address.

# The call stack is a LIFO (Last In First Out) data structure. This means that
# the most recently pushed item is popped first. The call stack is used to
# implement function calls in most programming languages, and is often referred
# to as the program stack or execution stack.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Average: O(Log(n)) time | O(1) space
        # Worst: O(n) time | O(1) space
        currentNode = self

        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
                    
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self
        
    def contains(self, value):
        # Average: O(Log(n)) time | O(1) space
        # Worst: O(n) time | O(1) space
        
        currentNode = self

        while currentNode is not None:
            
            if value < currentNode.value:
                currentNode = currentNode.left

            elif value > currentNode.value:
                currentNode = currentNode.right

            else: #currentNode is currentNode.value
                return True
        return False

    def remove(self, value, parentNode=None):
        currentNode = self

        # Start traversing the tree to find the node to remove
        while currentNode is not None:
            if value < currentNode.value:
                # If the value is less than the current node's value, go left
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                # If the value is greater than the current node's value, go right
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # Found the node to be removed

                # Case 1: Node has two children
                if currentNode.left is not None and currentNode.right is not None:
                    # Find the node with the minimum value in the right subtree
                    minValueNode = currentNode.right.getMinValueNode()
                    # Replace the current node's value with the found minimum value
                    currentNode.value = minValueNode.value
                    # Recursively remove the minimum value node from the right subtree
                    currentNode.right.remove(minValueNode.value, currentNode)
                    break

                # Handling removal when the node is the root
                if parentNode is None:
                    # Root node with one child or no children
                    if currentNode.left is not None:
                        # Root has only left child, replace root data with left child data
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        # Root has only right child, replace root data with right child data
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # Root has no children, which means it's a single-node tree
                        # Here, you can choose to do nothing or set `self.value` to `None`
                        # to represent an empty tree
                        pass
                else:
                    # Node with one child or no children and it's not the root
                    if parentNode.left == currentNode:
                        # If the current node is a left child, update parent's left pointer
                        parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                    elif parentNode.right == currentNode:
                        # If the current node is a right child, update parent's right pointer
                        parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break

        return self


    def getMinValueNode(self):
        currentNode = self

        while currentNode.left is not None:
            currentNode = currentNode.left

        return currentNode
