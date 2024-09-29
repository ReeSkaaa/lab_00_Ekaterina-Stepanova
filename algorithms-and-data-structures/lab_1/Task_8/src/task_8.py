import time
from memory_profiler import profile

t_start = time.perf_counter()


@profile()
def mister_swap(a, n, f2):
    for i in range(n - 1):
        min_id = i
        min = a[i]
        for j in range(i + 1, n):
            if a[j] < min:
                min = a[j]
                min_id = j
        if min_id != i:
            a[i], a[min_id] = a[min_id], a[i]
            f2.write(f'Swap elements at indices {i + 1} and {min_id + 1}.\n')


if __name__ == '__main__':
    f1 = open('../txtf/input_Task8.txt', 'r')
    n = int(f1.readline())
    if (3 <= n <= 5 * 10 ** 3):
        a = list(map(int, f1.readline().split()))
        f2 = open('../txtf/output_Task8.txt', 'w')
        mister_swap(a, n, f2)
        f2.write('No more swaps needed.')
        f2.close()

    else:
        print('Error.Try again')
    f1.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
