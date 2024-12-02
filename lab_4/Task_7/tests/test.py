from lab_4.Task_7.src.main import sequence_maximum
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_performance_do_queue(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        data = [8, 4, [2, 7, 3, 1, 5, 2, 6, 2]]
        expected_data = [7, 7, 5, 6, 6]

        # when
        # time test
        start_time = timeit.default_timer()
        result = sequence_maximum(data[0], data[2], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = sequence_maximum(data[0], data[2], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
