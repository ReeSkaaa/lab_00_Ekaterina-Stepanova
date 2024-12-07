from Lab_5.Task_1.src.main import check_heap
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_performance_check_heap_uncorrect(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 5
        data = ['0', '1', '0', '1', '2', '0']
        expected_data = 'NO'

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_heap(n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_heap(n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_check_heap_correct(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 5
        data = ['0', '1', '3', '2', '5', '4']
        expected_data = 'YES'

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_heap(n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_heap(n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
