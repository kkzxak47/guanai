# coding: utf-8

def max_and_status(l, r):
    """
    l: left values of dominos
    r: right values of dominos
    example: s1 = (5, 8), s2 = (4, 2), s3 = (9, 6),
             s4 = (7, 7), s5 = (3, 9), s6 = (11, 10)
    l = [5, 4, 9, 7, 3, 11]
    r = [8, 2, 6, 7, 9, 10]

    return: max_value and status of dominos
    """
    num = len(l)
    l = [0] + l
    r = [0] + r
    partial_max = [[0 for _ in range(num+1)] for _ in range(2)]
    previous_status = [[0 for _ in range(num+1)] for _ in range(2)]
    res = [0 for _ in range(num+1)]
    for i in range(1, num):
        a, b = sorted([l[i], r[i]])
        c, d = sorted([l[i+1], r[i+1]])
        if partial_max[0][i] + b*c >= partial_max[1][i] + a*c:
            partial_max[0][i+1] = partial_max[0][i] + b*c
            previous_status[0][i+1] = 0
        else:
            partial_max[0][i+1] = partial_max[1][i] + a*c
            previous_status[0][i+1] = 1
        if partial_max[0][i] + b*d >= partial_max[1][i] + a*d:
            partial_max[1][i+1] = partial_max[0][i] + b*d
            previous_status[1][i+1] = 0
        else:
            partial_max[1][i+1] = partial_max[1][i] + a*d
            previous_status[1][i+1] = 1

    if partial_max[0][num] > partial_max[1][num]:
        maxval = partial_max[0][num]
        res[num] = 0
    else:
        maxval = partial_max[1][num]
        res[num] = 1
    for i in range(num, 1, -1):
        if res[i] == 0:
            res[i-1] = previous_status[0][i]
        else:
            res[i-1] = previous_status[1][i]
    return maxval, res[1:]


def test():
    l = [5, 4, 9, 7, 3, 11]
    r = [8, 2, 6, 7, 9, 10]
    print(max_and_status(l, r))


if __name__ == '__main__':
    test()
