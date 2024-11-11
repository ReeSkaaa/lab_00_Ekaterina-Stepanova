from memory_profiler import profile
from lab_1.Task_6.utils import read_f, write_f


@profile()
def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def main():
    read_res = read_f('../txtf/input_Task9.txt')
    a = read_res[0]
    ans = [*map(str, bubble_sort(a))]
    res = ''
    for i in ans:
        res += i + ' '
    write_f('../txtf/output_Task9.txt', res)
