import random
import sys

sys.setrecursionlimit(30000)


def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L, R = [0] * n1, [0] * 2
    for i in range(0, n1):
        L[i] = (a[p + i])
    for j in range(0, n2):
        R[j] = (a[q + j + 1])
    L.append(float('inf'))
    R.append(float('inf'))
    print(R)
    print(L)
    i, j = 0, 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
    return a


def merge_sort(a, p, r):
    if p < r:
        q = p + (r - p) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
        return a


a = [random.randint(0, 100) for i in range(10)]
print(a)
print(merge_sort(a, 0, 3))
