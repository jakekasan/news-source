import unittest
import main

class Main_Tests(unittest.TestCase):
    def test_if_single_lookup_exists(self):
        self.assertIsNotNone(main.single_lookup)

    def test_if_range_lookup_exists(self):
        self.assertIsNotNone(main.range_lookup)

    def test_if_single_lookup_returns_none(self):
        self.assertIsNone(main.single_lookup())

    def test_if_range_lookup_returns_none(self):
        self.assertIsNone(main.range_lookup())

        
def run_tests():
    unittest.main()

if __name__ == '__main__':
    run_tests()