import unittest
from hypothesis import given, strategies as st



class Tests(unittest.TestCase):

    def test_base_cases(self):
        pass

    def test_known_value(self):
        pass

    @given(st.integers(min_value=3, max_value=25))
    def test_fibonacci_property(self, n):
        fib_n = getNthFib(n)
        fib_n_minus_1 = getNthFib(n-1)
        fib_n_minus_2 = getNthFib(n-2)
        self.assertEqual(fib_n, fib_n_minus_1 + fib_n_minus_2)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)