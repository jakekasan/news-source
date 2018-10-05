import unittest

class Import_Guardian(unittest.TestCase):
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

    def test_guardian_instance_has_name_attr(self):
        from sources.guardian import Guardian

        g = Guardian()

        self.assertIsInstance(g.name,str)

    def test_guardian_instance_name_is_guardian(self):
        from sources.guardian import Guardian

        g = Guardian()

        self.assertEqual(g.name,"guardian")

    def test_guardian_instance_has_attr_set_api_address(self):
        from sources.guardian import Guardian

        g = Guardian()

        cond = hasattr(g,"set_api_address")

        self.assertTrue(cond)

    def test_guardian_instance_has_attr_set_api_key(self):
        from sources.guardian import Guardian

        g = Guardian()

        cond = hasattr(g,"set_api_key")

        self.assertTrue(cond)

    def test_guardian_instance_has_attr_api_search(self):
        from sources.guardian import Guardian

        g = Guardian()

        cond = hasattr(g,"api_search")

        self.assertTrue(cond)
    
     

if __name__ == '__main__':
    unittest.main()