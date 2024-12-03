from lab_5.Task_4.src.main import MinHeap
import timeit
import tracemalloc
import unittest


class TestMinHeap(unittest.TestCase):
    def test_should_performance_minheap_sorted_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 5
        data = [1, 2, 3, 4, 5]
        expected_data = (0, [])

        # when
        # time test
        start_time = timeit.default_timer()
        result = MinHeap(n, data).do_heap_sort()
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = MinHeap(n, data).do_heap_sort()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_minheap_sorted_reverse_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 5
        data = (5, [5, 4, 3, 2, 1])
        expected_data = (3, [(1, 4), (0, 1), (1, 3)])

        # when
        # time test
        start_time = timeit.default_timer()
        result = MinHeap(data[0], data[1]).do_heap_sort()
        res = result
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = MinHeap(data[0], data[1]).do_heap_sort()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(current, time)
        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
