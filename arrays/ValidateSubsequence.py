import unittest

def isValidSubsequence(array, sequence):

    return True


class TestProgram(unittest.TestCase):

    def test_types(self):
        self.assertEqual(type(isValidSubsequence([1, 2], [1])), bool)

    def test_base_case(self):
        self.assertEqual(isValidSubsequence([1, 2], [1]), True)
        self.assertEqual(isValidSubsequence([1, 2], [2]), True)
        self.assertEqual(isValidSubsequence([1, 2], [3]), False)
    
    """ def test_case_1(self):
        self.assertEqual(validateSubsequence([1, 2], [1, 2]), True)
        self.assertEqual(validateSubsequence([1, 2], [2, 1]), False) """

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)