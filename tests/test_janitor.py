import unittest
import os
from src.janitor import Janitor

test_path = os.path.join(os.getcwd() + '/a')

class TestJanitorMethods(unittest.TestCase):

	def setUp(self):
		self.cleaner = Janitor(test_path)

	def tearDown(self):
		self.cleaner = None

	def testSearchDirectory(self):
		self.assertEqual(test_path, self.cleaner.directory, 'Incorect directory initialisation')

if __name__ == '__main__':
  unittest.main()