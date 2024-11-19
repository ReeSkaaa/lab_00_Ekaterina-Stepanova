from lab_3.Task_5.src.main import h_index
import timeit
import time
import tracemalloc
from lab_3.utils import read_f
import unittest


def test_time():
    "Функция для проверки времени при данных, взятых пользователем из файла"
    # given

    read = read_f(5)
    a = read[0]
    a = list(map(int, a.split()))

    # when

    start_time = timeit.default_timer()

    result = h_index(a, len(a))
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)

def test_memory():
    "Функция для проверки затрат памяти при данных, взятых пользователем из файла"
    # given

    read = read_f(5)
    a = read[0]
    a = list(map(int, a.split()))
    # when
    tracemalloc.start()
    result = h_index(a, len(a))
    # then
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()
class TestStringMethods(unittest.TestCase):

    def test_should_h_index(self):
        # given
        expected_result = 1
        data = [1, 3, 1]

        # when
        start_time = timeit.default_timer()
        result = h_index(data, len(data))
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = 1
        data = [1, 3, 1]

        # when
        start_time = timeit.default_timer()
        result = h_index(data, len(data))
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
