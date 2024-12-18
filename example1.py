import unittest


def add(a, b):
    if a == "0":
        raise TypeError("ERROR")
    return a + b


class TestMathFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add((-1), (-1)), -2)
        self.assertEqual(add(-1.9, 2.4), 0.5)
        self.assertTrue((1.999 - 2.444) - (-0.445) < 0.000001)
        self.assertAlmostEqual(1.999 - 2.444, -0.445, places=3)
        #with self.assertRaises(TypeError) as context:
        #    self.assertEqual(add("1", 1), 1)
        #self.assertEqual(str(context.exception), "TypeError")"""

if __name__ == '__main__':
    unittest.main()