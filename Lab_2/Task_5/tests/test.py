from Lab_2.Task_5.src.main import majority_element
import tracemalloc
import timeit
import unittest


class TestMajorityElement(unittest.TestCase):
    def test_should_performance_majority_element_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[7, 1, 1], 3]
        expected_data = 1

        # when
        # time test
        start_time = timeit.default_timer()
        result = majority_element(data[0], int(data[1]))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = majority_element(data[0], int(data[1]))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
