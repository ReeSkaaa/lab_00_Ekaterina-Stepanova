import time
from memory_profiler import profile
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

t_start = time.perf_counter()
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
    f = open('../txtf/input.txt', 'r')
    n = int(f.readline())
    A = list(map(int, f.readline().split()))
    f.close()
    a = A.copy()
    f = open('../txtf/output.txt', 'w')
    f.write(str(merge_sort(A, a, 0, n - 1)) + "\n")
    f.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
