from lab_1.Task_9.src.task_9 import binary_addition
import timeit
from lab_1.Task_9.utils import read_f, write_f

def main():
    read = read_f('../txtf/input_Task9.txt')
    n1, n2 = read[0][0], read[0][1]
    n1 = [*map(int, n1)]
    n2 = [*map(int, n2)]
    write_f('../txtf/output_Task9.txt', binary_addition(n1, n2))


def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

def test_binary():
    assert binary_addition([1, 0, 0], [0, 0, 0]) == '100'
    assert binary_addition([1, 0], [0, 1]) == '11'
    assert  binary_addition([1], [1]) == '10'
    assert binary_addition([1, 1, 1, 0], [0, 0, 0, 1]) == '1111'