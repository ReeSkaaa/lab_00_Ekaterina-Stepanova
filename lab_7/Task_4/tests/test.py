from lab_7.Task_4.src.main import lcs
import timeit
import tracemalloc
import unittest


class TestLCS(unittest.TestCase):
    def test_should_performance_lcs_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 1
        data = ['275', '25', 3, 2]
        expected_data = 2

        # when
        # time test
        start_time = timeit.default_timer()
        result = lcs(data[0], data[1], data[2], data[3])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = lcs(data[0], data[1], data[2], data[3])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")
    def test_should_performance_lcs_with_single_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 1
        data = ['7', '1234', 1, 4]
        expected_data = 0

        # when
        # time test
        start_time = timeit.default_timer()
        result = lcs(data[0], data[1], data[2], data[3])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = lcs(data[0], data[1], data[2], data[3])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")
    def test_should_performance_lcs_big_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 1
        data = ['2783', '5287', 4, 4]
        expected_data = 2

        # when
        # time test
        start_time = timeit.default_timer()
        result = lcs(data[0], data[1], data[2], data[3])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = lcs(data[0], data[1], data[2], data[3])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")



if __name__ == '__main__':
    unittest.main()
