import unittest
from making_change import making_change

class Test(unittest.TestCase):

  def setUp(self):
    self.denominations = [1, 5, 10, 25, 50]

  def test_making_change_small_amount(self):
    self.assertEqual(making_change(0, self.denominations), 1)
    self.assertEqual(making_change(1, self.denominations), 1)
    self.assertEqual(making_change(5, self.denominations), 2)
    self.assertEqual(making_change(10, self.denominations), 4)
    self.assertEqual(making_change(20, self.denominations), 9)
    self.assertEqual(making_change(30, self.denominations), 18)
    self.assertEqual(making_change(100, self.denominations), 292)
    self.assertEqual(making_change(200, self.denominations), 2435)
    self.assertEqual(making_change(300, self.denominations), 9590)


if __name__ == '__main__':
  unittest.main()
