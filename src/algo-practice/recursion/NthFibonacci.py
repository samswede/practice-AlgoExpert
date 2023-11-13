

#O(n) time | O(n) space
def getNthFib(n):

    F = [0, 1]
    for i in range(0, n):
        F.append(F[i] + F[i+1])
        print(f'i: {i} | F: {F}')
        # Write your code here.
    return F[n-1]

class Tests:

    def test1():
        n = 6
        expected = 5
        actual = getNthFib(n)
        passed = expected == actual
        print(f"Passed test: {passed}")

    def test2():
        n = 2
        expected = 0
        actual = getNthFib(n)
        passed = expected == actual
        print(f"Passed test: {passed}")