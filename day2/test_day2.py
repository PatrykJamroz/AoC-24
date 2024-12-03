import unittest
from day2 import check_safety

class TestDay2(unittest.TestCase):

    def test_check_safety(self):
        self.assertEqual(check_safety([7, 6, 4, 2, 1]), 'safe')
        self.assertEqual(check_safety([1, 2, 7, 8, 9]), 'unsafe')
        self.assertEqual(check_safety([9, 7, 6, 2, 1]), 'unsafe')
        self.assertEqual(check_safety([1, 3, 2, 4, 5]), 'safe')
        self.assertEqual(check_safety([8, 6, 4, 4, 1]), 'safe')
        self.assertEqual(check_safety([1, 3, 6, 7, 9]), 'safe')


if __name__ == '__main__':
    unittest.main()