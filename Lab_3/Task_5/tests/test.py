from Lab_3.Task_5.src.main import h_index
import timeit
import tracemalloc
import unittest


class TestHindex(unittest.TestCase):
    def test_should_performance_h_index_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [1, 3, 1]
        expected_data = 1

        # when
        # time test
        start_time = timeit.default_timer()
        result = h_index(data, len(data))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = h_index(data, len(data))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_h_index_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [1, 3, 40, 1, 2, 4, 6, 7, 8]
        expected_data = 4

        # when
        # time test
        start_time = timeit.default_timer()
        result = h_index(data, len(data))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = h_index(data, len(data))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
