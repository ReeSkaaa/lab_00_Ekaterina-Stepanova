import time
import random
from memory_profiler import profile


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


t_start = time.perf_counter()
if __name__ == '__main__':
    f1 = open('../txtf/input.txt', 'r')
    n = int(f1.readline())
    a = [random.randint(-10 ** 3, 10 ** 3) for i in range(n)]
    print(a)
    f2 = open('../txtf/output7.txt', 'w')
    max_sum, start, end = find_max_subarray(a, n)
    f2.write("Max subarray: " + str(max_sum) + '\n')
    f2.write("Subarray index: " + str(start) + ' ' + str(end))
    f2.close()
f1.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
