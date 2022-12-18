# Arrays

+ [merge](#merge)
+ [squares](#squares)

## merge

 Merge two sorted arrays

```python
def merge(first, second):

    new_list = []
    iter1 = 0
    iter2 = 0

    while (iter1 < len(first)) and (iter2 < len(second)):

        if (first[iter1] < second[iter2]):
            new_list.append(first[iter1])
            iter1 += 1

        else:
            new_list.append(second[iter2])
            iter2 += 1

    if iter2 < len(second):
        while (iter2 < len(second)):
            new_list.append(second[iter2])
            iter2 += 1

    else:
        while (iter1 < len(first)):
            new_list.append(first[iter1])
            iter1 += 1

    return new_list
```

## squares

 Returning a sorted array consisting of the elements of the initial array outer squared in O(n)

```python
from Arrays.merge import merge

def squares(s):

    i = 0
    while (i < len(s) and s[i] < 0):
        i += 1
    s1 = [s[cur] ** 2 for cur in range(i - 1 , -1, -1)]
    s2 = [s[cur] ** 2 for cur in range(i, len(s))]

    return merge(s1, s2)
```
