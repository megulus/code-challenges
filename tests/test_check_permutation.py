import unittest

import check_permutation

class Test(unittest.TestCase):
  str1 = 'grump'
  str2 = 'rpgmu'
  str3 = 'gprmw'
  str4 = 'prGum'

  def test_is_permutation(self):
    self.assertTrue(check_permutation.is_permutation(self.str1, self.str2))
    self.assertFalse(check_permutation.is_permutation(self.str1, self.str3))
    self.assertTrue(check_permutation.is_permutation(self.str1, self.str4))


if __name__ == '__main__':
  unittest.main()
