import unittest
import functions


class TestTheFunction(unittest.TestCase):
	def testMyFxn(self):
		self.assertTrue(functions.isEmpty([]))
		self.assertFalse(functions.isEmpty([1,2]))
		
if __name__ == "__main__":
	unittest.main()