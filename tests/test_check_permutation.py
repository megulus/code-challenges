import unittest
import sys
import os

my_path = '/Users/megdahlgren/src/code-challenges/src/cracking_code_interview'
sys.path.append(my_path)
check_permutation = os.path.join(my_path, 'check_permutation.py')

from check_permutation import check_permutation
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
