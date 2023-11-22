import unittest
from hypothesis import given, strategies as st



""" def maxSubsetSumNoAdjacent(array, memo={'': 0}):

    stringArray = stringifyArray(array)
    if stringArray in memo:
        return memo[stringArray]
    largestSumsArray = array

    for index in range(len(array)):
        subarray = array[:(index-1)].append(array[(index+1):])
        indexLargestSum = largestSumsArray[index] + maxSubsetSumNoAdjacent(array)

    largestSum = max(largestSumsArray)
    memo[stringArray] = largestSum
    return largestSum

def stringifyArray(array):
    string = ''
    for num in array:
        string += ','+str(num) #this is super inefficient

    return string
 """

# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):

    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    
    maxSums= array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])

    return maxSums[-1]

# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    currentMax= 0
    prevMax = 0
    for num in array:
        tmp =  prevMax
        prevMax =  currentMax
        currentMax = max(currentMax, tmp + num)
        
    return currentMax

# Cleaner equivalent of above
def maxSubsetSumNoAdjacent(array):
    currentMax, previousMax = 0, 0
    for number in array:
        previousMax, currentMax = currentMax, max(currentMax, previousMax + number)
    return currentMax

class Tests(unittest.TestCase):

    def test_base_types(self):
        self.assertIsInstance(maxSubsetSumNoAdjacent([]), int)
        self.assertIsInstance(maxSubsetSumNoAdjacent([1]), int)
        
    def test_base_cases(self):
        self.assertEqual(maxSubsetSumNoAdjacent([]), 0)
        self.assertEqual(maxSubsetSumNoAdjacent([1]), 1)
        self.assertEqual(maxSubsetSumNoAdjacent([1,2]), 2)
        self.assertEqual(maxSubsetSumNoAdjacent([1,2,3]), 4)
        
""" 
    def test_known_value(self):
        self.assertEqual(maxSubsetSumNoAdjacent([1,2,3]), 4)
 """
if __name__ == "__main__":

    unittest.main(argv=['first-arg-is-ignored'], exit=False)