import unittest
from polynomial import Polynomial


class TestPolynomicalMethods(unittest.TestCase):
    
    def setUp(self):
        self.polynomial1 = Polynomial([3, 2, 1])
        self.polynomial2 = Polynomial([1, 2])
        self.polynomial3 = Polynomial((3, -1, 10))
        self.polynomial4 = Polynomial((-2, 4, 5, -8))

    def test_init(self):
        self.assertEqual(self.polynomial1.variables, [3, 2, 1], "Неправильный конструктор!!!")
        self.assertEqual(self.polynomial2.variables, [1, 2], "Неправильный конструктор!!!")
        self.assertEqual(self.polynomial3.variables, (3, -1, 10), "Неправильный конструктор!!!")
        self.assertEqual(self.polynomial4.variables, (-2, 4, 5, -8), "Неправильный конструктор!!!")

    def test_str(self):
        self.assertTrue(str(self.polynomial1) == "Polynomial([3, 2, 1])","Неправильный вывод на экран!!!")
        self.assertTrue(str(self.polynomial2) == "Polynomial([1, 2])","Неправильный вывод на экран!!!")
        self.assertTrue(str(self.polynomial3) == "Polynomial((3, -1, 10))","Неправильный вывод на экран!!!")
        self.assertTrue(str(self.polynomial4) == "Polynomial((-2, 4, 5, -8))","Неправильный вывод на экран!!!")

    def test_string_polynomial(self):
        self.assertTrue(self.polynomial1.string_polynomial() == "3x^2 + 2x + 1", "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial2.string_polynomial() == "1x + 2", "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial3.string_polynomial() == "3x^2 - 1x + 10", "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial4.string_polynomial() == "-2x^3 + 4x^2 + 5x - 8", "Неправильный вывод на экран!!!")

    def test_addition(self):
        self.assertTrue(self.polynomial1.addition(self.polynomial2) == "Polynomial([4, 4, 1])", "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial2.addition((1, -2, 3)) == [2, 0, 3], "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial3.addition([5, -2]) == [8, -3, 10], "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial4.addition(6) == [-2, 4, 5, -2], "Неправильный вывод на экран!!!")
        
    def test_substitution(self):
        self.assertTrue(self.polynomial1.subtraction(self.polynomial2) == "Polynomial([2, 0, 1])", "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial2.subtraction((1, -2, 3))== [0, 4, -3], "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial3.subtraction([5, -2]) == [-2, 1, 10], "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial4.subtraction(6) == [-2, 4, 5, -14], "Неправильный вывод на экран!!!")

    def test_multiplication(self):
        self.assertTrue(self.polynomial1.multiplication(self.polynomial2) == [3, 8, 5, 2], "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial2.multiplication((1, -2, 3)) == [1, 0, -1, 6], "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial3.multiplication([5, -2]) == [15, -11, 52, -20], "Неправильный вывод на экран!!!")

    def test_isequals(self):
        self.assertTrue(self.polynomial1.isequals(self.polynomial2) == False, "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial2.isequals((1, -2, 3)) == False, "Неправильный вывод на экран!!!")
        self.assertTrue(self.polynomial3.isequals([5, -2]) == False, "Неправильный вывод на экран!!!")


if __name__ == '__main__':
    unittest.main()
