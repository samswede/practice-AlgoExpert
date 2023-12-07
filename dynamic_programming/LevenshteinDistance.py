import time


# O(nm) time | O(nm) space
def levenshteinDistance_slow(str1, str2):

    # Create a 2D array of size (len(str1)+1) * (len(str2)+1)
    # +1 is for the empty string
    edits = [[0 for j in range(len(str1)+1)] for i in range(len(str2)+1)]

    # Initialize the first row and column
    for i in range(len(str2)+1):
        # All deletes
        edits[i][0] = i
    for j in range(len(str1)+1):
        # All inserts
        edits[0][j] = j
    
    start_time = time.time()

    # Fill the rest of the array
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            edits[i][j] = formula_slow(str1, str2, edits, i, j)

    end_time = time.time()
    print("Time taken: ", end_time - start_time)
    return edits[-1][-1]

def formula_slow(str1, str2, edits, i, j):

    # If the characters are the same, then the edit distance is the same as the previous
    if str1[j-1] == str2[i-1]:
        edits[i][j] = edits[i-1][j-1]
    else:
        # If the characters are different, then the edit distance is the minimum of up, left, and diagonal + 1
        edits[i][j] = 1 + min(edits[i-1][j-1], edits[i-1][j], edits[i][j-1])

    return edits[i][j]


# O(nm) time | O(min(n, m)) space
def levenshteinDistance_fast(str1, str2):
    """
    I need to understand this even odd thing. I don't get it.
    Why will it currentEdits be evenEdits if i is even? My issue is that evenEdits is always [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ...]
    But I thought that we would have to switch previousEdits = currentEdits on each iteration. But we don't. Why?
    
    It works because previousEdits and currentEdits are just pointers to the evenEdits and oddEdits arrays.
    That means that evenEdits and oddEdits are overwritten on each iteration. So we don't need to switch them.
    This is a very clever solution.

    
    """

    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2

    evenEdits = [x for x in range(len(small)+1)]
    oddEdits = [None for x in range(len(small)+1)]

    start_time = time.time()

    for i in range(1, len(big)+1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        
        currentEdits[0] = i

        for j in range(1, len(small)+1):
            if big[i-1] == small[j-1]:
                currentEdits[j] = previousEdits[j-1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j-1], previousEdits[j], currentEdits[j-1])

    end_time = time.time()
    print("Time taken: ", end_time - start_time)

    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]


str1 = "abcjkeanaaaaaadkjanwaaaamnbvqwertabdjfkeajdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkztreayxcvbnjkwaaaamnbvqwertabdjfkeajdaaaaaaaaaamnbrtabdjfkeajdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkztreayxcvbnjkwaaaamnbvqwertabdjfkeajdaaabcjkeanaaaaaadkjanwaaaamnbvqwercqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbqwertzuiopasdfghjkztreayxcvbnjkwaaaamabcjkeanaaaaaadkjanwaaaamnbvqwertabdjfkeajdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkztreayxcvbnjkwaaaamabcjkeanaaaaaadkjanwaaaamnbvqwertabdjfkeajdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkztreayxcvbnjkwaaaamabcjkeanaaaaaadkjanwaaaamnbvqwertabdjfkeajdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkztreayxcvbnjkwaaaamabcjkeanaaaaaadkjanwaaaamnbvqwertabdjfkeajdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkztreayxcvbnjkwaaaamcqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbcqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbcqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbcqwertzuioqwertzuiopasdfghjkljhgfdsyxcvb"
str2 = "yabdjfkeajdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbnm,sdfgabdjfkeajdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkdaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbndaaaaaaaaaamnbvcqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbncqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbcqwertzuioqwertzuiopasdfghjkljhgfdsyxcvbaamnbvqwercqwertzuioqwertzuiopasdfghjkljhaamnbvqwercqwertzuioqwertzuiopasdfghjkljh"
print(levenshteinDistance(str1, str2))
print(levenshteinDistance_fast(str1, str2))
