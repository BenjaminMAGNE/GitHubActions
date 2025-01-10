import unittest\nfrom exemple import addition\n\nclass TestAddition(unittest.TestCase):\n    def test_addition(self):\n        self.assertEqual(addition(2, 3), 5)
