import unittest
from hypothesis import given, strategies as st 

# O(n) time | O(n) space
""" def getNthFib(n):
    F = [0, 1]
    for i in range(0, n-2):
        F.append(F[i] + F[i+1])
    return F[n-1]

# O(n) time | O(1) space
def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
    
# recursive solution
# O(2^n) time | O(n) space
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)

 """
# recursive solution with memoization
def getNthFib(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]



class Tests(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(getNthFib(1), 0)
        self.assertEqual(getNthFib(2), 1)

    def test_known_value(self):
        self.assertEqual(getNthFib(6), 5)

    @given(st.integers(min_value=3, max_value=25))
    def test_fibonacci_property(self, n):
        fib_n = getNthFib(n)
        fib_n_minus_1 = getNthFib(n-1)
        fib_n_minus_2 = getNthFib(n-2)
        self.assertEqual(fib_n, fib_n_minus_1 + fib_n_minus_2)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)