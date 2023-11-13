
# This product sum function takes a special array as input which contains either
# integers or other special arrays. The product sum of a special array is the sum
# of its elements, where special arrays inside it are summed themselves and then
# multiplied by their level of depth. 

# The depth of a special array is how far nested it is. For instance, the depth
# of [] is 1; the depth of the inner array in [[]] is 2; the depth of the innermost
# array in [[[]]] is 3.

# Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]]
# is x + 2 * (y + z); the product sum of [x, [y, [z]]] is x + 2 * (y + 3z).

# Sample input: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# Sample output: 12 (calculated as: 5 + 2 + 2*(7 - 1) + 3 + 2*(6 + 3*(-13 + 8) + 4))


def specialProductSum(specialArray, depth=1):
    sum = 0
    for element in specialArray:
        
        if isinstance(element, list):
            sum += specialProductSum(element, depth+1)
        elif isinstance(element, int):
            sum += element
        else: 
            raise Exception("Invalid element type")

    return sum * depth

def test(testInput, testOutput):
    print(f"Testing with input {testInput}")
    print(f"Expected output: {testOutput}")
    print(f"Actual output: {specialProductSum(testInput)}")
    print(f"Passed test: {specialProductSum(testInput) == testOutput}")


testInput = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
testOutput = 12

test(testInput, testOutput)