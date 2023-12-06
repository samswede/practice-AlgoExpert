import unittest


# O(nk) time | O(nk) space
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if not len(prices):
        return 0

    profits = [[0 for d in prices] for t in range(k +1)]

    for t in range(1, k+1):
        # store max formula
        maxThusFar = float("-inf")

        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, profits[t-1][d-1] - prices[d-1])
            profits[t][d] = max(profits[t][d -1], maxThusFar + prices[d])

    return profits[-1][-1]


# O(nk) time | O(n) space
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if not len(prices):
        return 0

    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]
    
    
    for t in range(1, k+1):
        # store max formula
        maxThusFar = float("-inf")

        if t % 2 == 1:
            currentProfits = oddProfits
            previousProfits = evenProfits

        else:
            currentProfits = evenProfits
            previousProfits = oddProfits

        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, previousProfits[d -1] - prices[d -1])
            currentProfits[d] = max(currentProfits[d -1], maxThusFar + prices[d])
       
    return evenProfits[-1] if k%2 == 0 else oddProfits[-1]


# O(n) time |  O(2*m) space  where m is the number of strictly increasing contiguous sections in the array.

# In the worst-case scenario, O(n) space.
# where every two elements form an increasing section (e.g., [1, 2, 1, 2, 1, 2, ...]), 
# the length of the result list can approach n. However, this is an extreme case.

def ExtractBoundariesOfIncreasingSubsequences(arr):
    """
    Extracts the boundaries of strictly increasing contiguous sections of an array. 
    Each section's first and last elements are captured, effectively summarizing 
    the increasing trends in the array.

    Args:
    arr (list of int): The array of integers.

    Returns:
    list of int: A list containing the first and last elements of each strictly increasing section.

    Complexity Analysis:
    Average Time Complexity: O(n), where n is the length of the array. The function iterates through 
                             each element of the array once to determine the boundaries of increasing sections.

    Worst-Case Time Complexity: Also O(n), as the function must examine each element of the array, 
                                regardless of the specific arrangement of the data.

    Average Space Complexity: O(m), where m represents the number of increasing subsections found in the array.
                              On average, m is less than n, especially in arrays where increasing sections 
                              are less frequent or longer in length.

    Worst-Case Space Complexity: O(n), which occurs in highly oscillating scenarios where every two 
                                 consecutive elements form an increasing section (e.g., [1, 2, 1, 2, 1, 2, ...]).
                                 In such cases, the function ends up storing boundaries for almost every pair of elements,
                                 leading to a space complexity that approaches n.
    """
    # Edge case: No elements
    if not arr:
        return []

    boundaries = []
    start = arr[0]

    for i in range(1, len(arr)):
        # If the current element is not greater than the previous one, it marks the end of an increasing section.
        if arr[i] <= arr[i - 1]:
            # Add boundaries of the increasing section, if it is strictly increasing
            if start != arr[i - 1]:
                boundaries.extend([start, arr[i - 1]])
            # Set the start of the next increasing section
            start = arr[i]

    # Add the last section's boundaries if it is strictly increasing
    if start != arr[-1]:
        boundaries.extend([start, arr[-1]])

    return boundaries


def maxProfitWithKTransactions(prices, k):
    """
    Calculates the maximum profit achievable with at most k transactions.

    Args:
    prices (list of int): List of stock prices.
    k (int): Maximum number of transactions allowed.

    Returns:
    int: The maximum profit achievable.

    Complexity Analysis:

    Average Time Complexity: O(n + 2mk), where n is the number of days (length of the prices array),
                             m is the number of increasing subsections in the prices array,
                             and k is the number of transactions.
                             The time complexity comprises two parts:
                             1. O(n) for extracting the boundaries of increasing subsections.
                             2. O(2mk) for calculating the maximum profit, as the algorithm iterates
                                k times over the 2m boundaries of increasing subsections.
                             
    Worst-Case Time Complexity: O(nk), where n is the number of days and k is the number of transactions.
                                This occurs when the number of increasing subsections m approaches n,
                                such as in a highly volatile stock price scenario where prices frequently oscillate.
                                In such cases, the time complexity for the profit calculation dominates.

    Average Space Complexity: O(2m), where m is the number of increasing subsections.
                              This space is used to store the profits for even and odd transactions,
                              with each array having a size proportional to the number of subsections (m).
                              
    Worst-Case Space Complexity: O(n), this occurs when the number of increasing subsections m is equal to n.
                                 In such a scenario, the profit arrays will have to accommodate as many elements
                                 as there are days, thus consuming space proportional to n.
    """
    # Edge case: No prices available
    if not len(prices):
        return 0

    # Extract boundaries of increasing price sections
    boundaryPrices = ExtractBoundariesOfIncreasingSubsequences(prices)

    # Edge case: No increasing sections, hence no profit
    if not boundaryPrices:
        return 0

    # Initialize profit arrays for even and odd transactions
    evenProfits = [0 for _ in boundaryPrices]
    oddProfits = [0 for _ in boundaryPrices]
    
    for t in range(1, k + 1):
        maxThusFar = float("-inf")
        # Alternate between using evenProfits and oddProfits arrays
        if t % 2 == 1:
            currentProfits, previousProfits = oddProfits, evenProfits
        else:
            currentProfits, previousProfits = evenProfits, oddProfits

        for d in range(1, len(boundaryPrices)):
            maxThusFar = max(maxThusFar, previousProfits[d - 1] - boundaryPrices[d - 1])
            currentProfits[d] = max(currentProfits[d - 1], maxThusFar + boundaryPrices[d])
       
    # Final profit is in evenProfits or oddProfits, depending on the parity of k
    return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]

# Test with the provided array
test_array = [1, 2, 3, 4, 5, 10, 20, 25, 24, 23, 22, 21, 30, 40, 50, 1, 2, 3, 4, 5]

boundaries = ExtractBoundariesOfIncreasingSubsequences(test_array)
print(f'Sequence: {test_array}')
print(f'The boundaries are: {boundaries}')