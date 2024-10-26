import random
from memory_profiler import profile
from lab_2.Task_7.utils import read_f, write_f

@profile
def find_max_subarray(a, n):
    max_sum = 0
    start = 0
    end = 0
    sums = 0
    for i in range(n):
        if sums == 0:
            start = i
        sums += a[i]
        if max_sum < sums:
            max_sum = sums
            end = i
        if sums < 0:
            sums = 0

    return max_sum, start, end


if __name__ == '__main__':
    read = read_f('../txtf/input.txt')
    n = read[0]
    a = [random.randint(-10 ** 3, 10 ** 3) for i in range(n)]
    res = find_max_subarray(a, n)
    write_f('../txtf/output.txt', res)

