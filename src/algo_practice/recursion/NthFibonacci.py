import unittest
from hypothesis import given, strategies as st 

def getNthFib(n):
    F = [0, 1]
    for i in range(0, n-2):
        F.append(F[i] + F[i+1])
    return F[n-1]

class Tests(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(getNthFib(1), 0)
        self.assertEqual(getNthFib(2), 1)

    def test_known_value(self):
        self.assertEqual(getNthFib(6), 5)

    @given(st.integers(min_value=3, max_value=100))
    def test_fibonacci_property(self, n):
        fib_n = getNthFib(n)
        fib_n_minus_1 = getNthFib(n-1)
        fib_n_minus_2 = getNthFib(n-2)
        self.assertEqual(fib_n, fib_n_minus_1 + fib_n_minus_2)

if __name__ == "__main__":
    unittest.main()
