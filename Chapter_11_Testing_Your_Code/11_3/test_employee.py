import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""."""

	def setUp(self):
		"""
		.
		"""
		self.employed = Employee('pedro', 'neto', 36_000)

	def test_give_default_raise(self):
		"""."""
		self.employed.give_raise()
		self.assertEqual(self.employed.salary, 41_000)

	def test_give_custom_raise(self):
		"""."""
		self.employed.give_raise(10_000)
		self.assertEqual(self.employed.salary, 46_000)

if __name__ == '__main__':
	unittest.main()

