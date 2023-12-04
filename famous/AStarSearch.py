import unittest
from typing import List

def aStarSearch(graph=[[0, 0], [0, 0]], start=[0,0], goal=[1,1]):
    return [[0,0], [0, 1], [1,1]]



class Tests(unittest.TestCase):
    def test_base_cases(self):
        self.assertIsInstance(aStarSearch(), List)


""" def test_known_values(self):
    self.assertEqual(longestPeak([1,2,3]), 0)
 """


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)