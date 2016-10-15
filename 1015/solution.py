# coding: utf-8

import itertools

def median5_cmp6(a, b, c, d, e):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if a < c:
        a = e
        if a > b:
            a, b = b, a
    else:
        c = e
        if c > d:
            c, d = d, c
    if a < c:
        if c < b:
            return c
        return b
    else:
        if a < d:
            return a
        return d


def sort5_cmp7(l):
    assert len(l) == 5
    result = []
    a, b, c, d, e = l
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if b > d:
        result.extend([c, d, b])
    else:
        result.extend([a, b, d])
        a = c
    # result == sorted(result) and len(result) == 3 and a < result[2]
    if e < result[1]:
        if e < result[0]:
            result.insert(0, e)
        else:
            result.insert(1, e)
    else:
        if e < result[2]:
            result.insert(2, e)
        else:
            result.insert(3, e)
    # result == sorted(result) and len(result) == 4 and a < result[3]
    if a < result[1]:
        if a < result[0]:
            result.insert(0, a)
        else:
            result.insert(1, a)
    else:
        if a < result[2]:
            result.insert(2, a)
        else:
            result.insert(3, a)
    return result


def test1():
    l = list(range(5))
    for perm in itertools.permutations(l):
        median = median5_cmp6(*perm)
        print(median, perm)
        assert(2 == median)
    print('median5_cmp6 ok')


def test2():
    l = list(range(5))
    for perm in itertools.permutations(l):
        sorted_perm = sort5_cmp7(perm)
        print(perm, sorted_perm)
        assert(sorted(perm) == sorted_perm)
    print('sort5_cmp7 ok')


if __name__ == '__main__':
    test1()
    test2()
