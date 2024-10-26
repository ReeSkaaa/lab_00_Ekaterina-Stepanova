from memory_profiler import profile
from lab_1.Task_8.utils import write_f, read_f
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


def main():
    read_res = read_f('../txtf/input_Task8.txt')
    n = read_res[0]
    if (3 <= n <= 5 * 10 ** 3):
        a = read_res[1]
        f2 = open('../txtf/output_Task8.txt', 'w')
        mister_swap(a, n, f2)
        f2.write('No more swaps needed.')
        f2.close()
    else:
        print('Error.Try again')