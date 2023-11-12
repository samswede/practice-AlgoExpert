# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for num_1 in array:
        for num_2 in array:
            if num_1 is not num_2 and (num_1 + num_2) is targetSum:
                return [num_1, num_2]
    return []

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

# O(nLog(n)) | O(1) space

def twoNumberSum(array, targetSum):
    array.sort() #this is efficient O(log(n)) time

    leftIndex = 0
    rightIndex = len(array) - 1
    
    while leftIndex < rightIndex:
        currentSum = array[leftIndex] + array[rightIndex]
        if currentSum == targetSum:
            return [array[leftIndex], array[rightIndex]]
        elif currentSum < targetSum:
            leftIndex += 1
        elif currentSum > targetSum:
            rightIndex -= 1

    return []