from lab_2.Task_1.src.task_1 import merge_sort
import timeit
from lab_1.Task_9.utils import read_f, write_f

def main():
    if __name__ == '__main__':
        read = read_f('../txtf/input.txt')
        n = read[0]
        if (1 <= n <= 2 * 10 ** 4):
            a = read[1]
            write_f('../txtf/output.txt', str(merge_sort(a, 0, len(a) - 1)))


def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

def test_merge_sort():
    assert merge_sort([1, 2, 3], 0, 2) == [1, 2, 3]
    assert merge_sort([9, 3], 0, 1) == [3, 9]
    assert merge_sort([100, 100, 100], 0, 2) == [100, 100, 100]
    assert merge_sort([1, 1], 0, 1) == [1, 1]