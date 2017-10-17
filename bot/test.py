import funciones
import unittest

class RealizaTest(unittest.TestCase):
    def comprobarFunciones(self):
        self.assertEqual(len(funciones.cargarWeb("PQ48K20440124700118006G")), 1) #Comprobar que la longitud de lo que devuelve la funcion es 1
        self.assertEqual(len(funciones.nombreEmpresa(documento)), 1) #Comprobar que la longitud de lo que devuelve la funcion es 1
        self.assertEqual(len(funciones.informacionMensaje(documento)), 2) #Comprobar que la longitud de lo que devuelve la funcion es 2
        self.assertEqual(len(funciones.fechaMensaje(documento)), 1) #Comprobar que la longitud de lo que devuelve la funcion es 1
        self.assertEqual(funciones.comprobarTrack(documento), -1)

if __name__ == '__main__':
    unittest.main()
