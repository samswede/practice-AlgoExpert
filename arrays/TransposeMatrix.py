import unittest


def transposeMatrix(matrix):
    transposedMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposedMatrix


class TestProgram(unittest.TestCase):

    def test_types(self):
        self.assertEqual(type(transposeMatrix([[1, 2], [3, 4]])), list)

    def test_shape(self):
        self.assertEqual(len(transposeMatrix([[1, 2, 3], [4, 5, 6]])), 3)
        self.assertEqual(len(transposeMatrix([[1, 2, 3], [4, 5, 6]])[0]), 2)

    def test_base_case(self):
        self.assertEqual(transposeMatrix([[1, 2], [3, 4]]), [[1, 3], [2, 4]])
    
    def test_case_1(self):
        self.assertEqual(transposeMatrix([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_case_2(self):
        self.assertEqual(transposeMatrix([[1, 2, 3, 4], [5, 6, 7, 8]]), [[1, 5], [2, 6], [3, 7], [4, 8]])
    
    def test_case_3(self):
        self.assertEqual(transposeMatrix([[1, 2], [3, 4], [5, 6], [7, 8]]), [[1, 3, 5, 7], [2, 4, 6, 8]])

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)