import unittest
from hypothesis import given, strategies as st


def longestPeak(array):
    """
    Finds the length of the longest peak in an array. A peak is defined as a sequence
    of consecutive elements strictly increasing up to a point (the peak), and then
    strictly decreasing. At least three elements are required to form a peak.

    Args:
    array (list of int): The input array in which to find the longest peak.

    Returns:
    int: The length of the longest peak in the array.
    """

    # Initialize the maximum peak length found so far.
    longestPeakLength = 0

    # Start from the second element and go up to the second-to-last element.
    i = 1
    while i < len(array) - 1:
        # Check if the current element forms a peak with its neighbors.
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]

        # If it's not a peak, move to the next element.
        if not isPeak:
            i += 1
            continue

        # Explore the left side of the peak to find where the peak starts.
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        # Explore the right side of the peak to find where the peak ends.
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        # Calculate the current peak's length.
        currentPeakLength = rightIdx - leftIdx - 1

        # Update the longest peak length if the current peak is longer.
        longestPeakLength = max(longestPeakLength, currentPeakLength)

        # Move the index to the end of the current peak to start checking for the next peak.
        i = rightIdx

    return longestPeakLength



class Tests(unittest.TestCase):
    def test_base_cases(self):
        self.assertIsInstance(longestPeak([1,2,3]), int)


    def test_known_values(self):
        self.assertEqual(longestPeak([1,2,3]), 0)

    @given(st.lists(st.integers()))
    def test_sorted_list(self, array):
        array.sort()
        if len(array) < 3:
                answer = 0
                self.assertEqual(longestPeak(array), answer)
        else:
                answer = 0
                self.assertEqual(longestPeak(array), answer)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)