"""sample tests"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """test the module"""

    def test_add_numbers(self):
        """test add numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """test sub numbers"""
        res = calc.substract(10, 15)

        self.assertEqual(res, 5)