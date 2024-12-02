import unittest
from day1 import main

class TestDay1(unittest.TestCase):

    def test_calculate_total_distance_and_similarity(self):
        total_distance, similarity = main()
        self.assertEqual(total_distance, 2000468)
        self.assertEqual(similarity, 18567089)

if __name__ == '__main__':
    unittest.main()