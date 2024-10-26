from memory_profiler import profile
from lab_1.Task_5.utils import read_f, write_f


@profile()
def selection_sort(a, n):
    for i in range(n - 1):
        min_elem = i
        for j in range(i + 1, n):
            if a[j] < a[min_elem]:
                min_elem = j
        a[i], a[min_elem] = a[min_elem], a[i]
    return a

def main():
    read_res = read_f('../txtf/input_Task_5.txt')
    n = read_res[0]
    a = read_res[1]
    res = selection_sort(a, n)
    write_f('../txtf/output_Task_5.txt', str(res))
