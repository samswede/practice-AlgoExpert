
def levenshteinDistance(str1, str2):

    # Create a 2D array of size (len(str1)+1) * (len(str2)+1)
    # +1 is for the empty string
    edits = [[0 for j in range(len(str1)+1)] for i in range(len(str2)+1)]

    return edits

if __name__ == "__main__":
    str1 = "abc"
    str2 = "yabd"
    print(levenshteinDistance(str1, str2))