import unittest

class Import_News_Wrangler(unittest.TestCase):
    """
        Tests that you can set config
    """
    def test_file_exists(self):
        from sources import guardian
        self.assertIsInstance(guardian,object)

    def test_file_has_guardian(self):
        from sources.guardian import Guardian

        self.assertIsInstance(Guardian,object)

    def test_guardian_is_class(self):
        from sources.guardian import Guardian

        g = Guardian()
        
        self.assertIsInstance(g,Guardian)

if __name__ == '__main__':
    unittest.main()