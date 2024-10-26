from lab_2.Task_4.src.task_4 import binary_search
import timeit
from lab_1.Task_9.utils import read_f, write_f

def main():
    if __name__ == '__main__':
        read = read_f('../txtf/input.txt')
        n = read[0]
        a = read[1]
        k = read[2]
        b = read[3]
        if (1 <= n, k <= 10 ** 5):
            result = ''
            for i in range(k):
                result += str(binary_search(a, b[i])) + ' '
        write_f('../txtf/input.txt', result)
def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

def test_binary():
    assert binary_search([1, 1, 2], 6) == -1
    assert binary_search([0, 1], 0) == 0
    assert binary_search([1, 2, 3], 2) == 1
    assert binary_search([10, 10, 1, 11, 11], 11) == 3