import unittest
from unittest.mock import patch
import main

class TestTurnoJugadora(unittest.TestCase):
    """Tests que evalúan la función turno_computadora"""
    def setUp(self):
        """Variables comunes"""
        self.intentos_jugadora = []
        self.numero_aleatorio = 30

    @patch('builtins.input', return_value = '30')
    def test_adivina_jugadora(self, mock_input):
        """Verifica que la jugadora acierta"""
 
        tentativa_jugadora = main.turno_jugadora(self.numero_aleatorio, self.intentos_jugadora)
        self.assertEqual(tentativa_jugadora, True)

    @patch('builtins.input', return_value = '35')
    def test_no_adivina_jugadora(self, mock_input):
        """Verifica que la jugadora no acierta"""

        tentativa_jugadora = main.turno_jugadora(self.numero_aleatorio, self.intentos_jugadora)
        self.assertFalse(tentativa_jugadora)

    @patch('builtins.input', return_value = '- 8')
    def test_numero_fuera_de_rango(self, mock_input):
        """Verifica que el valor está fuera del rango"""

        tentativa_jugadora = main.turno_jugadora(self.numero_aleatorio, self.intentos_jugadora)
        self.assertFalse(tentativa_jugadora)

    @patch('builtins.input', return_value = 'hola')
    def test_entrada_inválida(self, mock_input):
        """Verifica el intento como una entrada inválida"""

        tentativa_jugadora = main.turno_jugadora(self.numero_aleatorio, self.intentos_jugadora)
        self.assertFalse(tentativa_jugadora)

    
class TestTurnoComputadora(unittest.TestCase):
    """Tests que evalúan la función turno_computadora"""

    def setUp(self):
        """Variables comunes"""
        self.intentos_computadora = []
        self.numero_aleatorio = 25 

    @patch('main.random.randint', return_value = 25)
    def test_adivina_computadora(self, mock_randint):
        """Verifica que la computadora acierta"""

        tentativa_computadora = main.turno_computadora(self.numero_aleatorio, self.intentos_computadora)
        self.assertTrue(tentativa_computadora)

    @patch('main.random.randint', return_value = 45)
    def test_no_adivina_computadora(self, mock_randint):
        """Verifica que la computadora no acierta"""
        
        tentativa_computadora = main.turno_computadora(self.numero_aleatorio, self.intentos_computadora)
        self.assertFalse(tentativa_computadora)

if __name__ == '__main__':
    unittest.main()
