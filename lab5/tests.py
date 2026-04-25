import unittest
from calc import calculate_consumption, calculate_energy_bill


class TestElectricityCalculator(unittest.TestCase):

    def test_calculate_consumption_normal(self):
        self.assertEqual(calculate_consumption(100.0, 150.0), 50.0)

    def test_calculate_consumption_zero(self):
        self.assertEqual(calculate_consumption(150.0, 150.0), 0.0)

    def test_calculate_consumption_error(self):
        with self.assertRaises(ValueError):
            calculate_consumption(200.0, 150.0)

    def test_calculate_energy_bill_normal(self):
        self.assertEqual(calculate_energy_bill(50.0, 4.32), 216.0)

    def test_calculate_energy_bill_zero(self):
        self.assertEqual(calculate_energy_bill(0.0, 4.32), 0.0)

    def test_calculate_energy_bill_error(self):
        with self.assertRaises(ValueError):
            calculate_energy_bill(-10.0, 4.32)


if __name__ == "__main__":
    unittest.main()
