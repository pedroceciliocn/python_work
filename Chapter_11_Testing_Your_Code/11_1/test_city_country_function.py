import unittest
from city_functions import get_formatted_location

class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'"""

	def test_city_country(self):
		"""Do cities like 'Santiago, Chile' work?"""
		formatted_location = get_formatted_location('santiago', 'chile')
		self.assertEqual(formatted_location, 'Santiago, Chile')

if __name__ == '__main__':
	unittest.main()