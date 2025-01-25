import unittest
from src.__math_operations import addition, soustraction, multiplication, division
from src.string_operations import concatener, mettre_en_majuscules

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)# Vérifier que 2 + 3 = 5
        self.assertEqual(addition(-1, 1), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2) # Vérifier que 5 - 3 donne = 2
        self.assertEqual(soustraction(0, 3), -3)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 5), 20) # Vérifier que 4 * 5 donne = 20
        self.assertEqual(multiplication(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5) # Vérifier que 10 / 2 =  5
        with self.assertRaises(ValueError):  # Vérifier qu'une division par 0 soulève une exception ValueError
            division(10, 0)

class TestStringOperations(unittest.TestCase):
    def test_concatener(self):
        self.assertEqual(concatener("Hello, ", "World!"), "Hello, World!") # Vérifier que la concaténation de "Hello, " et "World!" donne bien "Hello, World!"
        self.assertEqual(concatener("", "Test"), "Test")

    def test_mettre_en_majuscules(self):
        self.assertEqual(mettre_en_majuscules("test"), "TEST") # Vérifier que "test" devient "TEST"
        self.assertEqual(mettre_en_majuscules("Python"), "PYTHON")

if __name__ == "__main__":
    unittest.main()
