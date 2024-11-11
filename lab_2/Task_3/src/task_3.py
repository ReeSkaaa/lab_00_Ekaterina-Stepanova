from memory_profiler import profile
from lab_2.Task_3.utils import read_f, write_f
@profile
def merge(A, a, l, mid, r):
    k = i = l
    j = mid + 1
    invCount = 0
    while i <= mid and j <= r:
        if A[i] <= A[j]:
            a[k] = A[i]
            i += 1
        else:
            a[k] = A[j]
            j += 1
            invCount += mid - i + 1
        k += 1
    while i <= mid:
        a[k] = A[i]
        k += 1
        i += 1
    for i in range(r + 1):
        A[i] = a[i]
    return invCount


def merge_sort(A, a, l, r):
    if l >= r:
        return 0
    mid = (l + r) // 2
    invCount = 0
    invCount += merge_sort(A, a, l, mid)
    invCount += merge_sort(A, a, mid + 1, r)
    invCount += merge(A, a, l, mid, r)
    return invCount

if __name__ == '__main__':
    read = read_f('../txtf/input.txt')
    n = read[0]
    A = read[1]
    a = A.copy()
    write_f('../txtf/output.txt', A, a, 0, n-1)
