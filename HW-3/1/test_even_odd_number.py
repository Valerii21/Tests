# *Задание 1.
# Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли переданное число четным или нечетным.

import unittest
from even_odd_number import even_odd_number


class EvenOddNumber(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(even_odd_number(6))

    def test_odd_number(self):
        self.assertFalse(even_odd_number(3))
