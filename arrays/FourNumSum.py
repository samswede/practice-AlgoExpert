import unittest


# O(n^3) time | O(n) space
def fourNumSum(array, targetSum):
    quadrupletList = []

    if len(array) < 4:
        return quadrupletList

    array.sort()

    for i in range(len(array) - 3): # O(n) time
          redIndex = i

          for j in range(redIndex+1, len(array)-2): # O(n) time
                greenIndex= j
                currentTargetSum = targetSum - array[redIndex] - array[greenIndex]
                leftIndex = greenIndex + 1
                rightIndex = len(array) - 1
                while leftIndex < rightIndex: # O(n) time worst case
                        currentSum = array[leftIndex] + array[rightIndex]
                        if currentSum == currentTargetSum:
                                quadruplet = [array[redIndex], array[greenIndex], array[leftIndex], array[rightIndex]]
                                if quadruplet not in quadrupletList:
                                    quadrupletList.append(quadruplet)
                                leftIndex += 1
                                rightIndex -= 1
                        elif currentSum < currentTargetSum:
                                leftIndex += 1
                        else:
                                rightIndex -= 1
    
    return quadrupletList

# O(n^2) time | O(n^2) space
# Worst case: O(n^3) time | O(n^2) space
def fourNumberSum(array, targetSum):
    """
    This solution is from AlgoExpert. It is a bit more elegant than mine.

    The idea is to use a hash table to store all the pair sums. Then, we can
    iterate through the array and check if the difference between the target sum
    and the current sum is in the hash table. If it is, then we can append the
    pair sum to the current sum to get the target sum.

    The reason why this is O(n^2) time is because we are iterating through the
    array twice. The first time is to create the hash table, and the second time
    is to check if the difference is in the hash table.

    Key ideas:
        - a quadruplet is just two pairs of sums.
                [x, y, z, w] = [x, y] + [z, w]
        - a pair sum is just two numbers added together.
                [x, y] = x + y
        - we can iterate in an interesting way to avoid duplicates.
                for i in range(1, len(array) - 1):
                    for j in range(i+1, len(array)):
                        # do stuff
                    for k in range(0, i):
                        # do stuff

    """
    allPairSums = {}
    quadruplets = []

    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum -currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets

class TestProgram(unittest.TestCase):

    def test_types(self):
        self.assertEqual(type(fourNumSum([1, 2, 3, 4, 5, 6, 7], 10)), list)

    def test_base_case(self):
        self.assertEqual(fourNumSum([1, 2, 3, 4, 5, 6, 7], 10), [[1, 2, 3, 4]])

    def test_known_value_1(self):
        self.assertEqual(fourNumSum([7, 6, 4, -1, 1, 2], 16), [[-1, 4, 6, 7], [1, 2, 6, 7]])
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)