from Lab_3.Task_3.src.main import scarecrow_sort
import timeit
import tracemalloc
import unittest


class TestScarecrowSort(unittest.TestCase):
    def test_should_screcrow_sort_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [2, 1, 3]
        n, k = 3, 2
        expected_data = False

        # when
        # time test
        start_time = timeit.default_timer()
        result = scarecrow_sort(n, k, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = scarecrow_sort(n, k, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_screcrow_sort_big_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [2, 1, 3, 10, 2, 3, 3]
        n, k = 7, 2
        expected_data = False

        # when
        # time test
        start_time = timeit.default_timer()
        result = scarecrow_sort(n, k, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = scarecrow_sort(n, k, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
