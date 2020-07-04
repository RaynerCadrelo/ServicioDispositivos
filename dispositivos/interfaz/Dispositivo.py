# coding=UTF-8
from controladores.interfaz.Controlador import *

class Dispositivo(object):

    def leerNombre(self):
        pass

    def cambiarNombre(self, nombre):
        pass

    def encender(self):
        pass

    def apagar(self):
        pass

    def leerValor(self):
        pass

    def escribirValor(self, valor):
        pass

    def estado(self):
        pass

    def refrescar(self, tiempoActual):
        """
         Parámetro: Tiempo actual del sistema
         Retorna: Tiempo a la que desea que se vuelva a refrescar.
        """
        pass

    def modificarControlador(self, controlador):
        pass



