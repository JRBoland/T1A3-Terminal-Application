from datetime import datetime
import os
import unittest


class TestDayMethods(unittest.TestCase):

    def test_check_if_new_day(self):
        is_new_day = True
        message = "Tally reset"
        self.assertTrue(is_new_day, message)

    def test_check_if_new_day(self):
        is_new_day = False
        message = "Tally recovered"
        self.assertTrue(is_new_day, message)
#

def test_get_current_directory(monkeypatch):
    given a monkeypatch version of os.getcwd()
    when example1() is called
    then check the current working directory returned

    def mock_getcwyd():
        return 'data/user/directory123'

    monkeypatch.setattr(os,'getcwd', mock_getcwd)
    assert example1() == '/data/user/directory123'
if __name__ == '__main__':
    unittest.main()