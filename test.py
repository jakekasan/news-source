import unittest


class Import_Main(unittest.TestCase):
    def test_main_exists(self):
        from main import main

        self.assertIsInstance(main,object)

if __name__ == '__main__':
    unittest.main()