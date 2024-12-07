from Lab_1.Task_4.src.main import lin_searh
import timeit
import tracemalloc
import unittest


class TestLinSearch(unittest.TestCase):
    def test_should_performance_lin_search_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        data = [[1, 2, 3], 3, 1]
        expected_data = (1, [0])

        # when
        # time test
        start_time = timeit.default_timer()
        result = lin_searh(data[0], data[1], data[2])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = lin_searh(data[0], data[1], data[2])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_lin_search_big_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        data = [[1, 2, 3, 7, 7, 5], 6, 7]
        expected_data = (2, [3, 4])

        # when
        # time test
        start_time = timeit.default_timer()
        result = lin_searh(data[0], data[1], data[2])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = lin_searh(data[0], data[1], data[2])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
