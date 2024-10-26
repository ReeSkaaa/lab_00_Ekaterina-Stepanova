import unittest
import sys
from Task_1.src.task_1 import insertion_sort

class calcTest(unittest.TestCase):
    def test_power(self):
        self.assertEqual(insertion_sort(5, 2), 25)




if __name__ == "__main__":
    unittest.main()
