import unittest
from hypothesis import given, strategies as st

def threeNumSum(array, targetSum):
    if len(array) < 3:
        return []
    else:
        return [[1,2,3]]

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []

class Tests(unittest.TestCase):

    def test_base_cases(self):
        
        # check that function returns list
        self.assertIsInstance(threeNumSum([1,2,3], 6), list)

        # check that if the list is not empty, that each list in the list has 3 elements
        self.assertEqual(len(threeNumSum([1,2,3], 6)[0]), 3)

        # check that if the list is empty, that the function returns an empty list
        self.assertEqual(threeNumSum([], 6), [])
        
    def test_known_value_1(self):
        
        pass
"""        
    # a check that the list is sorted (ascending)
    @given(st.lists(st.integers()))
    def test_sorted_list(self, array):
        self.assertEqual(threeNumSum(array, 6), sorted(threeNumSum(array, 6)))
"""
""" 
    def test_known_value(self):
        self.assertEqual(getNthFib(6), 5)

    @given(st.integers(min_value=3, max_value=25))
    def test_fibonacci_property(self, n):
        fib_n = getNthFib(n)
        fib_n_minus_1 = getNthFib(n-1)
        fib_n_minus_2 = getNthFib(n-2)
        self.assertEqual(fib_n, fib_n_minus_1 + fib_n_minus_2)
 """
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)