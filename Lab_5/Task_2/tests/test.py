from Lab_5.Task_2.src.main import find_tree_height
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_performance_find_tree_height_example_first(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 3
        n = 5
        data = [4, -1, 4, 1, 1]
        expected_data = 3

        # when
        # time test
        start_time = timeit.default_timer()
        result = find_tree_height(n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time


        # memory test
        tracemalloc.start()
        result = find_tree_height(n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()


        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")
    def test_should_performance_find_tree_height_example_second(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 3
        n = 5
        data = [-1, 0, 4, 0, 3]
        expected_data = 4

        # when
        # time test
        start_time = timeit.default_timer()
        result = find_tree_height(n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time


        # memory test
        tracemalloc.start()
        result = find_tree_height(n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

if __name__ == '__main__':
    unittest.main()
