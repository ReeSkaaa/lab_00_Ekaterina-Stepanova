import time
from memory_profiler import profile

t_start = time.perf_counter()


@profile()
def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


if __name__ == '__main__':
    f1 = open('../txtf/input_Task9.txt', 'r')
    a = list(map(int, f1.readline().split()))
    f2 = open('../txtf/output_Task9.txt', 'w')
    ans = [*map(str, bubble_sort(a))]
    for i in ans:
        f2.write(f'{i} ')
    f2.close()
    f1.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
