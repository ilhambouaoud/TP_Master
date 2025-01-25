import unittest 
from conversion import (
    dollars_to_dirhams,
    meters_to_kilometers
)
class test_conversion(unittest.TestCase):
    def dollars_to_dirhams(self):
        self.assertAlmostEqual(dollars_to_dirhams(99))
    def meters_to_kilometers(self):
        self.assertAlmostEqual(meters_to_kilometers(20))
if __name__ == "__main__":
    unittest.main()