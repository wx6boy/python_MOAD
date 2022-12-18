# title merge
# description Merge two sorted arrays
# code
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