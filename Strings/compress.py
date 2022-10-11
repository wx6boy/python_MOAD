# title squares
# description String compress. Example: from aabbbcccc to a2b3c4
# code
def compress(elems):

    result = []
    if len(elems) > 0:
        result.append(elems[0])
        cur_sum = 1
    for i in range(1, len(elems)):
        if elems[i] == elems[i-1]:
            cur_sum += 1
        else:
            if cur_sum > 1:
                result.append(str(cur_sum))
                cur_sum = 1
            result.append(elems[i])

    if(cur_sum > 1):
        result.append(str(cur_sum))

    return "".join(result)