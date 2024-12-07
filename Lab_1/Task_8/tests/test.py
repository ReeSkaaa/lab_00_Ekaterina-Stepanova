from Lab_1.Task_8.src.main import mister_swap
import tracemalloc
import timeit
import unittest


class TestMisterSwap(unittest.TestCase):
    def test_should_performance_mister_swap_example(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [3, 1, 4, 2, 2]
        n = 5
        expected_data = ['Swap elements at indices 1 and 2.\n', 'Swap elements at indices 2 and 4.\n',
                         'Swap elements at indices 3 and 5.\n']

        # when
        # time test
        start_time = timeit.default_timer()
        result = mister_swap(data, n)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = mister_swap(data, n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
