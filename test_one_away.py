import unittest
import one_away

class Test(unittest.TestCase):

  def test_one_away(self):
    self.assertFalse(one_away.is_one_away('pale', 'spales'))
    self.assertTrue(one_away.is_one_away('pale', 'ple'))
    self.assertTrue(one_away.is_one_away('pales', 'pale'))
    self.assertTrue(one_away.is_one_away('pale', 'bale'))
    self.assertFalse(one_away.is_one_away('pale', 'bake'))
    self.assertTrue(one_away.is_one_away('pale', 'pale'))
    self.assertFalse(one_away.is_one_away('bale', 'pales'))


if __name__ == '__main__':
  unittest.main()
