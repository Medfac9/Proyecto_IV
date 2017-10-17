import funciones
import unittest

class Testeador(unittest.TestCase):
    def Comprobador(self):
        self.assertEqual(len(funciones.comprobarTrack("PQ48K20440124700118006G")), 4) #Comprobar que la longitud de lo que devuelve la funcion es 4
        self.assertEqual(funciones.comprobarTrack("234"), -1)

if __name__ == '__main__':
    unittest.main()
