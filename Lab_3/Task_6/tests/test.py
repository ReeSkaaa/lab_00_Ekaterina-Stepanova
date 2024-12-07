from Lab_3.Task_6.src.main import get_result, quickSort, multiplication
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_performance_quick_sort_big_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data1 = [7, 1, 4, 9]
        data2 = [2, 7, 8, 11]
        expected_data = 51
        # when
        # time test
        start_time = timeit.default_timer()
        c = multiplication(data1, data2)
        quickSort(c, 0, len(c) - 1)
        result = get_result(c)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        c = multiplication(data1, data2)
        quickSort(c, 0, len(c) - 1)
        result = get_result(c)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_quick_sort_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data1 = [7, 1]
        data2 = [2, 1]
        expected_data = 1
        # when
        # time test
        start_time = timeit.default_timer()
        c = multiplication(data1, data2)
        quickSort(c, 0, len(c) - 1)
        result = get_result(c)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        c = multiplication(data1, data2)
        quickSort(c, 0, len(c) - 1)
        result = get_result(c)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
