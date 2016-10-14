# coding: utf-8

def reverse(l, start, end):
    for step in range(0, (start+end+1) // 2 - start):
        tmp = l[start+step]
        l[start+step] = l[end-step]
        l[end-step] = tmp


def shift_right_k_times(l, n, k):
    k %= n
    reverse(l, 0, n-k-1)
    reverse(l, n-k, n-1)
    reverse(l, 0, n-1)
    return l


def test():
    l = list(range(10))
    print(shift_right_k_times(l, 10, 3))


if __name__ == '__main__':
    test()
