from lab_3.Task_7.src.main import get_answer
import timeit
import time
import tracemalloc
from lab_3.utils import read_f
import unittest


def test_time():
    "Функция для проверки времени при данных, взятых пользователем из файла"
    # given

    data = read_f(7)


    # when

    start_time = timeit.default_timer()

    result = get_answer(data)
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)

def test_memory():
    "Функция для проверки затрат памяти при данных, взятых пользователем из файла"
    # given

    data = read_f(7)

    # when
    tracemalloc.start()
    result = get_answer(data)
    # then
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()
class TestStringMethods(unittest.TestCase):

    def test_should_check_get_answer(self):
        # given
        expected_result = '2 3 1\n'
        data = ['3 3 1', 'bab', 'bba', 'baa']

        # when
        tracemalloc.start()
        start_time = timeit.default_timer()
        result = get_answer(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_result)


        # given
        expected_result = '3 2 1\n'
        data = ['3 3 2', 'bab', 'bba', 'baa']

        # when
        tracemalloc.start()
        start_time = timeit.default_timer()
        result = get_answer(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = '2 3 1\n'
        data = ['3 3 3', 'bab', 'bba', 'baa']

        # when
        tracemalloc.start()
        start_time = timeit.default_timer()
        result = get_answer(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
