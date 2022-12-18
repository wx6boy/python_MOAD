# title squares
# description Returning a sorted array consisting of the elements of the initial array outer squared in O(n)
# code
from Arrays.merge import merge

def squares(s):

    i = 0
    while (i < len(s) and s[i] < 0):
        i += 1
    s1 = [s[cur] ** 2 for cur in range(i - 1 , -1, -1)]
    s2 = [s[cur] ** 2 for cur in range(i, len(s))]

    return merge(s1, s2)