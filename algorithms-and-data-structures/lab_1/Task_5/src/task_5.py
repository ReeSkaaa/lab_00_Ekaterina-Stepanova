import time
from memory_profiler import profile

t_start = time.perf_counter()


@profile()
def selection_sort(a, n):
    for i in range(n - 1):
        min_elem = i
        for j in range(i + 1, n):
            if a[j] < a[min_elem]:
                min_elem = j
        a[i], a[min_elem] = a[min_elem], a[i]

    return a


if __name__ == '__main__':
    f1 = open('../txtf/input_Task_5.txt', 'r')
    n = int(f1.readline())
    a = list(map(int, f1.readline().split()))
    f2 = open('../txtf/output_Task_5.txt', 'w')
    f2.write(str(selection_sort(a, n)))
    f2.close()

    f1.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
