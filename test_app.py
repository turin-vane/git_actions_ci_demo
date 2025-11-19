# test_app.py

import unittest
from app import calcular_precio_con_descuento

class TestDescuentos(unittest.TestCase):
    
    # Prueba 1: Verificar un descuento estándar del 10%
    def test_descuento_valido_10_porciento(self):
        # Precio: 100.00, Descuento: 10% (Esperado: 90.00)
        self.assertEqual(calcular_precio_con_descuento(100.00, 10), 90.00)

    # Prueba 2: Verificar descuento del 50%
    def test_descuento_valido_50_porciento(self):
        # Precio: 200.00, Descuento: 50% (Esperado: 100.00)
        self.assertEqual(calcular_precio_con_descuento(200.00, 50), 100.00)

    # Prueba 3: Verificar que la función maneje entradas no válidas
    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            calcular_precio_con_descuento(-10, 10) # Precio negativo

if __name__ == '__main__':
    unittest.main()