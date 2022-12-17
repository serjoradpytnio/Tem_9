import unittest
from circle import circle_area
from cmath import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(3),pi*3**2)
        self.assertEqual(circle_area(1),pi)
        self.assertEqual(circle_area(0),0)
        self.assertEqual(circle_area(2,5),pi*2,5**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, -1)