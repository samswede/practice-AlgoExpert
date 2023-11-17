import unittest
from hypothesis import given, strategies as st

def threeNumSum(array, targetSum):
    if len(array) < 3:
        return []
    else:
        return [[1,2,3]]



def threeNumSum(array, targetSum):
    tripletList = []
    array.sort()  # O(n log n) time

    for i in range(len(array) - 2): # O(n) time
            num = array[i]
            currTargetSum = targetSum - num
            leftIndex = i + 1
            rightIndex = len(array) - 1

            #print(f"num: {num} | currTargetSum: {currTargetSum}")
                
            while leftIndex < rightIndex:
                    currentSum = array[leftIndex] + array[rightIndex]
                    
                    #print(f"currentSum: {currentSum} | leftIndex: {leftIndex} | rightIndex: {rightIndex}")
                    
                    if currentSum == currTargetSum:
                            triplet = [num, array[leftIndex], array[rightIndex]]
                            triplet.sort()

                            if triplet not in tripletList:
                                    tripletList.append(triplet)

                            # Update indices to find next possible triplet
                            leftIndex += 1
                            rightIndex -= 1

                    elif currentSum < currTargetSum:
                            leftIndex += 1
                    else:
                            rightIndex -= 1

    return tripletList


# Why does list.sort() return None?
# Because it modifies the list in-place. sorted(list) returns a new list and leaves the original alone.
# Therefore, 

class Tests(unittest.TestCase):

    def test_base_cases(self):
        
        # check that function returns list
        self.assertIsInstance(threeNumSum([1,2,3], 6), list)

        # check that if the list is not empty, that each list in the list has 3 elements
        self.assertEqual(len(threeNumSum([1,2,3], 6)[0]), 3)


    def test_known_value_1(self):
        
        self.assertEqual(threeNumSum([1,2,3], 6), [[1,2,3]])
     
    @given(st.lists(st.integers()))
    def test_sorted_list(self, array):
        if len(array) < 3:
            answer = []
            randint = st.integers(min_value=0, max_value=100)
            self.assertEqual(threeNumSum(array, randint), answer)
        else:
            num1, num2, num3 = array[0], array[1], array[2]
            sum1 = num1 + num2 + num3

            tripletList = threeNumSum(array, sum1)
            self.assertTrue(sorted([num1, num2, num3]) in tripletList)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)