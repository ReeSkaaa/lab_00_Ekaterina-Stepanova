import timeit
from memory_profiler import profile
from lab_1.Task_1.utils import read_f, write_f


@profile()
def insertion_sort(a, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break

    return a
def main():
    read_res = read_f('../txtf/input.txt')
    n = read_res[0]
    if (1 <= n <= 10 ** 3):
        a = read_res[1]
        write_f('../txtf/output.txt', str(insertion_sort(a, n)))

