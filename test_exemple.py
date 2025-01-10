import unittest
from exemple import addition
class TestAddition(unittest.TestCase):
  def test_addition(self):        
    self.assertEqual(addition(2, 3), 5)
