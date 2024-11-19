from lab_3.Task_3.src.main import scarecrow_sort
import timeit
import time
import tracemalloc
from lab_2.utils import read_f
import unittest

class TestStringMethods(unittest.TestCase):
    def test_should_no_scarecrow(self):
        # given
        expected_result = False
        data = [2, 1, 3]
        n, k = 3, 2

        # when
        tracemalloc.start()
        start_time = timeit.default_timer()
        result = scarecrow_sort(n, k, data)
        end_time = timeit.default_timer()
        print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
        tracemalloc.stop()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

    def test_should_scarecrow(self):
        # given
        expected_result = False
        data = [1, 5, 3, 4, 1]
        n, k = 5, 3

        # when
        start_time = timeit.default_timer()
        result = scarecrow_sort(n, k, data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
