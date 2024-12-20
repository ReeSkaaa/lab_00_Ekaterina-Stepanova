from Lab_7.Task_3.src.main import edit_dist
import timeit
import tracemalloc
import unittest


class TestEditDistance(unittest.TestCase):
    def test_should_performance_edit_dist_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 1
        data = ['fb', 'fb']
        expected_data = 0

        # when
        # time test
        start_time = timeit.default_timer()
        result = edit_dist(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = edit_dist(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_edit_dist_example_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 1
        data = ['short', 'ports']
        expected_data = 3

        # when
        # time test
        start_time = timeit.default_timer()
        result = edit_dist(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = edit_dist(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_edit_dist_big_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 1
        data = ['editing', 'distance']
        expected_data = 5

        # when
        # time test
        start_time = timeit.default_timer()
        result = edit_dist(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = edit_dist(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
