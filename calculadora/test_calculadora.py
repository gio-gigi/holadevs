import unittest
from calculadora import Calculadora

class testCalculadora(unittest.TestCase):
    def test_sumar_dos_mas_dos(self):
        cal = Calculadora()
        resultado = cal.sumar(2, 2)
        self.assertEqual(resultado, 4, "La suma de 2 + 2 debería ser 4")

if __name__ == '__main__':
    unittest.main()