import unittest
from store.coupon_calculations import calculate_price


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(calculate_price(8, 5, 10), 8.28, places=2)
        self.assertAlmostEqual(calculate_price(8, 5, 15), 7.86, places=2)
        self.assertAlmostEqual(calculate_price(8, 5, 20), 7.43, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 10), 2.98, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 15), 2.56, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 20), 2.13, places=2)

    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(calculate_price(25, 5, 10), 26.50, places=2)
        self.assertAlmostEqual(calculate_price(25, 5, 15), 25.18, places=2)
        self.assertAlmostEqual(calculate_price(25, 5, 20), 23.85, places=2)
        self.assertAlmostEqual(calculate_price(25, 10, 10), 21.20, places=2)
        self.assertAlmostEqual(calculate_price(25, 10, 15), 19.88, places=2)
        self.assertAlmostEqual(calculate_price(25, 10, 20), 18.55, places=2)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(calculate_price(45, 5, 10), 49.58, places=2)
        self.assertAlmostEqual(calculate_price(45, 5, 15), 47.19, places=2)
        self.assertAlmostEqual(calculate_price(45, 5, 20), 44.81, places=2)
        self.assertAlmostEqual(calculate_price(45, 10, 10), 44.28, places=2)
        self.assertAlmostEqual(calculate_price(45, 10, 15), 41.89, places=2)
        self.assertAlmostEqual(calculate_price(45, 10, 20), 39.51, places=2)

if __name__ == '__main__':
    unittest.main()
