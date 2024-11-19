from lab_3.Task_2.src.main import antiQuickSortPermutation
import timeit
import time
import tracemalloc
from lab_3.utils import read_f
import unittest


def test_time():
    "Функция для проверки времени при данных, взятых пользователем из файла"
    # given

    read = read_f(2)
    n = int(read[0])

    # when

    start_time = timeit.default_timer()

    result = antiQuickSortPermutation(n)
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)

def test_memory():
    "Функция для проверки затрат памяти при данных, взятых пользователем из файла"
    # given

    read = read_f(2)
    n = int(read[0])
    # when
    tracemalloc.start()
    result = antiQuickSortPermutation(n)
    # then
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()
class TestStringMethods(unittest.TestCase):

    def test_should_single_antiQuick(self):
        # given
        expected_result = [1]
        data = 1

        # when
        start_time = timeit.default_timer()
        result = antiQuickSortPermutation(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)
    def test_should_antiQuick(self):
        # given
        expected_result = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 25, 51, 13, 53, 27, 55, 7, 57, 29, 59, 15, 61, 31, 63, 2, 65, 33, 67, 17, 69, 35, 71, 9, 73, 37, 75, 19, 77, 39, 79, 5, 81, 41, 83, 21, 85, 43, 87, 11, 89, 45, 91, 23, 93, 47, 95, 3, 97, 49, 99]

        data = 100

        # when
        start_time = timeit.default_timer()
        result = antiQuickSortPermutation(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = [1, 3, 2]
        data = 3

        # when
        start_time = timeit.default_timer()
        result = antiQuickSortPermutation(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
