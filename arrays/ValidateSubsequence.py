import unittest

def isValidSubsequence(array, sequence):
    currentIndex = len(array) - 1
    while len(sequence):
        currentElement = sequence.pop()
        #print(f'currentElement: {currentElement}')
        found = False
        while currentIndex >= 0:
            if array[currentIndex] == currentElement:
                found = True
                break
            currentIndex -= 1
        if not found:
            return False
        currentIndex -= 1  # Start the next search one position before the found element
        if currentIndex < 0 and len(sequence) > 0:
            return False
        
    return True

def isValidSubsequence(array, sequence):
    """
    This solution is from AlgoExpert. It is a bit more elegant than mine.
    """
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)



class TestProgram(unittest.TestCase):

    def test_types(self):
        self.assertEqual(type(isValidSubsequence([1, 2], [1])), bool)

    def test_base_case(self):
        self.assertEqual(isValidSubsequence([1, 2], [1]), True)
        self.assertEqual(isValidSubsequence([1, 2], [2]), True)
        self.assertEqual(isValidSubsequence([1, 2], [3]), False)
    
    def test_case_1(self):
        self.assertEqual(isValidSubsequence([1, 2], [1, 2]), True)
        self.assertEqual(isValidSubsequence([1, 2], [2, 1]), False)

    def test_case_2(self):
        self.assertEqual(isValidSubsequence([1, 2, 3], [1, 2]), True)
        self.assertEqual(isValidSubsequence([1, 2, 3], [1, 3]), True)
        self.assertEqual(isValidSubsequence([1, 2, 3], [2, 3]), True)
        self.assertEqual(isValidSubsequence([1, 2, 3], [1, 2, 3]), True)
        self.assertEqual(isValidSubsequence([1, 2, 3], [1, 2, 3, 4]), False)
        self.assertEqual(isValidSubsequence([1, 2, 3], [1, 2, 4]), False)
        self.assertEqual(isValidSubsequence([1, 2, 3], [1, 4, 3]), False)
        self.assertEqual(isValidSubsequence([1, 2, 3], [4, 2, 3]), False)
        self.assertEqual(isValidSubsequence([1, 2, 3], [1, 2, 3, 4, 5]), False)
        self.assertEqual(isValidSubsequence([1, 2, 3], [1, 2, 4, 5]), False)

    def test_case_3(self):
        self.assertEqual(isValidSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8]), True)
        self.assertEqual(isValidSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 5, 7, 9]), True)
        self.assertEqual(isValidSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 7, 6, 9]), False)

    def test_case_4(self):
        self.assertEqual(isValidSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), False)
        self.assertEqual(isValidSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 10]), False)

    def test_case_5(self):
        self.assertEqual(isValidSubsequence([1, 1, 6, 1], [1, 1, 1, 6]), False)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)