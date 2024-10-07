import random
import sys
import time
from memory_profiler import profile

sys.setrecursionlimit(30000)


@profile()
def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L, R = [0] * n1, [0] * n2
    for i in range(0, n1):
        L[i] = (a[p + i])
    for j in range(0, n2):
        R[j] = (a[q + j + 1])

    k, i, j = p, 0, 0
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


t_start = time.perf_counter()
if __name__ == '__main__':
    f1 = open('../txtf/input.txt', 'r')
    n = int(f1.readline())
    if (1 <= n <= 2 * 10 ** 4):
        a = list(map(int, f1.readline().split()))
        f2 = open('../txtf/output.txt', 'w')
        f2.write(str(merge_sort(a, 0, len(a) - 1)))
        f2.close()

    else:
        print('Error.Try again')
    f1.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
