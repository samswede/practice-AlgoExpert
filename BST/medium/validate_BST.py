

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, minValue= float("-inf"), maxValue= float("inf")):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False

    # If our current node is valid, we need to check the left and right subtrees
    leftIsValid = validateBst(tree.left, minValue, tree.value)

    # If the left subtree is valid, we need to check the right subtree
    if leftIsValid:
        treeIsValid = leftIsValid and validateBst(tree.right, tree.value, maxValue)
        return treeIsValid
    else:
        return False
    

# Here we have a divide and conquer approach. We are checking the left and right subtrees
# and then combining the results to check the current node.

# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(d) where d is the depth of the tree (the number of frames on the call stack)
# This is because we are making recursive calls on the left and right subtrees. The number of frames
# on the call stack is equal to the depth of the tree.

