from Lab_4.Task_13.src.main_13_2 import Queue
import timeit
import tracemalloc
import unittest


class TestQueue(unittest.TestCase):

    def test_should_performance_test_empty_queue(self):
        "Тест затрат времени, памяти и проверка корректного ответа"
        # given
        expected_time = 2
        self.queue = Queue()
        expected_data = True

        # when
        # time test
        start_time = timeit.default_timer()
        result = self.queue.isEmpty()
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = self.queue.isEmpty()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_full_queue(self):
        "Тест затрат времени, памяти и проверка корректного ответа"
        # given
        expected_time = 2
        self.queue = Queue()
        for i in range(3):
            self.queue.enqueue('value')
        expected_data = True

        # when
        # time test
        start_time = timeit.default_timer()
        result = self.queue.isFull()
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = self.queue.isFull()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
