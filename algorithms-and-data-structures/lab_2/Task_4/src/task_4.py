import time
from memory_profiler import profile


@profile
def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


t_start = time.perf_counter()
if __name__ == '__main__':
    f1 = open('../txtf/input.txt', 'r')
    n = int(f1.readline())
    a = [int(x) for x in f1.readline().split()]
    k = int(f1.readline())
    b = [int(x) for x in f1.readline().split()]
    f1.close()
    if (1 <= n, k <= 10 ** 5):
        f2 = open('../txtf/output.txt', 'w')
        for i in range(k):
            f2.write(str(binary_search(a, b[i])) + ' ')
        f2.close()
    else:
        print('Error.Try again')
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
