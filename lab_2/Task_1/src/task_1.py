import sys
from memory_profiler import profile
from lab_2.Task_1.utils import read_f, write_f
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

if __name__ == '__main__':
    read = read_f('../txtf/input.txt')
    n = read[0]
    if (1 <= n <= 2 * 10 ** 4):
        a = read[1]
        write_f('../txtf/output.txt', str(merge_sort(a, 0, len(a) - 1)))
