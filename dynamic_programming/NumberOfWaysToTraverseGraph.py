import unittest

def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    if width == 1 or height == 1:
        return 1
    return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)


