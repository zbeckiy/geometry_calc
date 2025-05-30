import unittest
from math import pi

from geometry_calc.geometry_calc import Triangle, Circle, calculate_area, LessThanZeroError, IrregularFigureError

class TestSFigures(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(1)
        self.assertEquals(c._calculate_area(), pi)

        c = Circle(2)
        self.assertNotEquals(c._calculate_area(), pi * 2)

        with self.assertRaises(LessThanZeroError):
            Circle(0)

    def test_triangle_area(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t._calculate_area(), 6)
        self.assertTrue(t.check_right_triangle())

        t2 = Triangle(5, 5, 6)
        self.assertFalse(t2.check_right_triangle())

        with self.assertRaises(IrregularFigureError):
            Triangle(1, 1, 3)

    def test_calculate_area(self):
        c = Circle(3)
        t = Triangle(3, 4, 5)
        self.assertEqual(calculate_area(c), c._calculate_area())
        self.assertEqual(calculate_area(t), t._calculate_area())

if __name__ == "__main__":
    unittest.main()