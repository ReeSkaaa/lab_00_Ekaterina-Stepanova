from lab_2.Task_1.src.task_1 import merge_sort
import timeit
from lab_1.Task_9.utils import read_f, write_f

def main():
    if __name__ == '__main__':
        read = read_f('../txtf/input.txt')
        n = read[0]
        A = read[1]
        a = A.copy()
        write_f('../txtf/output.txt', A, a, 0, n - 1)


def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)