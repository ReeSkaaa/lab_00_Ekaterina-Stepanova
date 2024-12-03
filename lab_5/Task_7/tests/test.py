from lab_5.Task_7.src.main import do_heapSort, get_answer
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_performance_heap_sort_single_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 3
        data = [1]
        expected_data = '1 '

        # when
        # time test
        start_time = timeit.default_timer()
        do_heapSort(data)
        result = get_answer(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        do_heapSort(data)
        result = get_answer(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_heap_sort_small_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 3
        data = [1, 2, 3]
        expected_data = '3 2 1 '

        # when
        # time test
        start_time = timeit.default_timer()
        do_heapSort(data)
        result = get_answer(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        do_heapSort(data)
        result = get_answer(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_heap_sort_empty_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 3
        data = []
        expected_data = ''

        # when
        # time test
        start_time = timeit.default_timer()
        do_heapSort(data)
        result = get_answer(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        do_heapSort(data)
        result = get_answer(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_heap_sort_big_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 3
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_data = '10 9 8 7 6 5 4 3 2 1 '

        # when
        # time test
        start_time = timeit.default_timer()
        do_heapSort(data)
        result = get_answer(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        do_heapSort(data)
        result = get_answer(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_heap_sort_ssimilar_elem_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 3
        data = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected_data = '1 1 1 1 1 1 1 1 1 '

        # when
        # time test
        start_time = timeit.default_timer()
        do_heapSort(data)
        result = get_answer(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        do_heapSort(data)
        result = get_answer(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_heap_sort_huge_elem(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 3
        data = [1000000, 200, 30000, 292929, 10100101010101010]
        expected_data = '10100101010101010 1000000 292929 30000 200 '

        # when
        # time test
        start_time = timeit.default_timer()
        do_heapSort(data)
        result = get_answer(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        do_heapSort(data)
        result = get_answer(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
