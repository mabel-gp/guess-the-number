import unittest
from unittest.mock import patch
import main

class testFunciones(unittest.TestCase):

    @ patch('builtins.input', return_value = '30')
    def test_adivina_jugadora(self, mock_input):
        """Verifica que el intento es True cuando la jugadora acierta"""

        numero_aleatorio = 30
        conato_jugadora = main.jugadora(numero_aleatorio)
        self.assertTrue(conato_jugadora)
    

    @ patch('builtins.input', return_value = '35')
    def test_no_adivina_jugadora(self, mock_input):
        """Verifica que el intento es False cuando la jugadora no acierta"""

        numero_aleatorio = 15
        tentativa_jugadora = main.jugadora(numero_aleatorio)
        self.assertFalse(tentativa_jugadora)


    @patch('main.random.randint', return_value = 25)
    def test_adivina_computadora(self, mock_randint):
        """Verifica que el intento es True cuando la computadora acierta"""

        numero_aleatorio = 25
        conato_computadora = main.computadora(numero_aleatorio)
        self.assertTrue(conato_computadora)


    @patch('main.random.randint', return_value = 45)
    def test_no_adivina_computadora(self, mock_randint):
        """Verifica que el intento es False cuando la computadora no acierta"""
        
        numero_aleatorio = 55
        tentativa_computadora = main.computadora(numero_aleatorio)
        self.assertFalse(tentativa_computadora)


if __name__ == '__main__':
    unittest.main()
