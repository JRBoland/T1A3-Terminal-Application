from datetime import datetime
import os
import unittest

class TestDayMethods(unittest.TestCase):

    def test_check_if_new_day(self):
        is_new_day = True
        message = "Tally reset"
        self.assertTrue(is_new_day, nessage)

    def test_check_if_new_day(self):
        is_new_day = False
        message = "Tally recovered"
        self.assertTrue(is_new_day, message)
#
if __name__ == '__main__':
    unittest.main()