
def jump_next(array, index):
    index += array[index]

    if index < 0:
        return len(array) - (index % len(array))
    else:
        return index % (len(array))

def BellmanFord(array):
    fastIndex = 0
    slowIndex = 0

    i = 0

    #have fastIndex make one move
    fastIndex = jump_next(array, fastIndex)
    print(f'fastIndex {i}: {fastIndex} | array[fastIndex]: {array[fastIndex]}')
    print(f'slowIndex {i}: {slowIndex} | array[slowIndex]: {array[slowIndex]}')
    while fastIndex is not slowIndex:
        i+=1
        fastIndex = jump_next(array, fastIndex)
        fastIndex = jump_next(array, fastIndex)
        print(f'fastIndex {i}: {fastIndex} | array[fastIndex]: {array[fastIndex]}')

        slowIndex = jump_next(array, slowIndex)
        print(f'slowIndex {i}: {slowIndex} | array[slowIndex]: {array[slowIndex]}')

        if i > 100:
            return False
    return True


def test():
    arr = [2, 3, 1, -4, -4, 2]
    hasCycle = BellmanFord(arr)

    passedTest = hasCycle == True
    print(f"Passed test: {passedTest}")

    pass

test()

def hasSingleCycle(array):

    elementsVisited = set()

    fastIndex = 0
    slowIndex = 0

    i = 0

    #have fastIndex make one move
    fastIndex = jump_next(array, fastIndex)
    print(f'fastIndex {i}: {fastIndex} | array[fastIndex]: {array[fastIndex]}')
    print(f'slowIndex {i}: {slowIndex} | array[slowIndex]: {array[slowIndex]}')
    while fastIndex is not slowIndex:
        i+=1
        fastIndex = jump_next(array, fastIndex)
        fastIndex = jump_next(array, fastIndex)
        print(f'fastIndex {i}: {fastIndex} | array[fastIndex]: {array[fastIndex]}')

        slowIndex = jump_next(array, slowIndex)
        print(f'slowIndex {i}: {slowIndex} | array[slowIndex]: {array[slowIndex]}')

        if i > 100:
            return False
    return True

# O(n) time | O(1) space

def hasSingleCycle(array):

    jumps = 0
    position = 0

    while True:
        position += array[position]
        position = position % len(array)
        jumps += 1

        if position == 0 or array[position] == 0 or jumps > len(array):
            break

    return jumps == len(array)
