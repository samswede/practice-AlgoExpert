import unittest

def validateSubsequence(array, sequence):
    return False


class TestProgram(unittest.TestCase):

    def test_types(self):
        self.assertEqual(type(validateSubsequence([1, 2], [1])), bool)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)