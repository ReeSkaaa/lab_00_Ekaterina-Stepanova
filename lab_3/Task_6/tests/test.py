from lab_3.Task_6.src.main import get_result, quickSort, multiplication
import timeit
import time
import tracemalloc
from lab_3.utils import read_f
import unittest


def test_time():
    "Функция для проверки времени при данных, взятых пользователем из файла"
    # given

    _, a_, b_ = read_f(6)
    a = list(map(int, a_.split()))
    b = list(map(int, b_.split()))
    c = multiplication(a, b)
    quickSort(c, 0, len(c) - 1)

    # when

    start_time = timeit.default_timer()

    result = get_result(c)
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)

def test_memory():
    "Функция для проверки затрат памяти при данных, взятых пользователем из файла"
    # given

    _, a_, b_ = read_f(6)
    a = list(map(int, a_.split()))
    b = list(map(int, b_.split()))
    c = multiplication(a, b)
    quickSort(c, 0, len(c) - 1)

    # when
    tracemalloc.start()
    result = get_result(c)
    # then
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()
class TestStringMethods(unittest.TestCase):

    def test_should_sort(self):
        # given
        expected_result = 51
        data1 = [7, 1, 4, 9]
        data2 = [2, 7, 8, 11]

        # when
        start_time = timeit.default_timer()
        c = multiplication(data1, data2)
        quickSort(c, 0, len(c)-1)
        result = get_result(c)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()
