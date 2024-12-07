from Lab_2.Task_4.src.main import binary_search
import timeit
import tracemalloc
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_should_performance_binary_search_no_right_answer(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[1, 1, 2], 6]
        expected_data = -1

        # when
        # time test
        start_time = timeit.default_timer()
        result = binary_search(data[0], int(data[1]))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = binary_search(data[0], int(data[1]))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_binary_search_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[1, 1, 2], 1]
        expected_data = 1

        # when
        # time test
        start_time = timeit.default_timer()
        result = binary_search(data[0], int(data[1]))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = binary_search(data[0], int(data[1]))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_binary_search_big_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[1, 3, 3, 4, 5, 6, 6, 6], 4]
        expected_data = 3

        # when
        # time test
        start_time = timeit.default_timer()
        result = binary_search(data[0], int(data[1]))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = binary_search(data[0], int(data[1]))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
