import time
from memory_profiler import profile


@profile()
def insertion_sort(a, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break

    return a


t_start = time.perf_counter()
if __name__ == '__main__':
    f1 = open('../txtf/input.txt', 'r')
    n = int(f1.readline())
    if (1 <= n <= 10 ** 3):
        a = list(map(int, f1.readline().split()))
        f2 = open('../txtf/output.txt', 'w')
        f2.write(str(insertion_sort(a, n)))
        f2.close()

    else:
        print('Error.Try again')
    f1.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
