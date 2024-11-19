import random
from lab_2.utils import read_f, write_f
PATH = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

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
    read = read_f(7)
    n = int(read[0])
    a = [random.randint(-10 ** 3, 10 ** 3) for i in range(n)]
    res = find_max_subarray(a, n)
    answer = ["Max subarray: " + str(res[0]), "Subarray index: " + str(res[1]) + ' ' + str(res[2])]
    write_f(7, *answer)

