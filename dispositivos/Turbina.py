# coding=UTF-8
import configparser
from dispositivos.interfaz.Dispositivo import *
import os

class Turbina (Dispositivo):

    def __init__(self, nombre, config):
        
        super().__init__()
        self._nombre=nombre
        self._solicitudEncendido="alto"+ config['TURBINA']['PIN_ENCENDIDO_APAGADO']
        self._solicitudApagado="bajo"+ config['TURBINA']['PIN_ENCENDIDO_APAGADO']
        
        self._pinAnalogico=config['TANQUE_ELEVADO']['PIN_ANALOGICO']       #involucrar con el tanque elevado para condicionar el apagado de la turbina`
        self._pinActivacion=config['TANQUE_ELEVADO']['PIN_ACTIVACION']
        
        self._estado="apagado"
        self._intervaloRefrescar=int(config['TURBINA']['INTERVALO_REFRESCAR']) # intervalo en segundos en que se llamará la función refrescar()


    def leerNombre(self):
        """
        @return string : retorna el nombre del dispositivo
        """
        return self._nombre

    def cambiarNombre(self, nombre):
        """
        @param string nombre :  cambia el nombre del dispositivo
        @return  : True si cambió el nombre del dispositivo, False y no pudo cambiarlo
        """
        self._nombre=nombre
        return True

    def encender(self):
        """
        @return bool : retorna True si se ha encendido, False si ha habido algún error.
        """
        respuesta = self._controlador.enviarRecibirDato(self._solicitudEncendido)
        if respuesta==self._solicitudEncendido:
            self._estado="encendido"
            return True
        else:
            return False
        

    def apagar(self):
        """
         

        @return bool : retorna True si se ha cumplido la orden de apagar, False si ha habido algún error
        """
        respuesta = self._controlador.enviarRecibirDato(self._solicitudApagado)
        if respuesta==self._solicitudApagado:
            self._estado="apagado"
            return True
        else:
            return False

    def leerValor(self):
        """
        @return string : Esta función carece de interés para esta clase
        """
        return "True"

    def escribirValor(self, valor):
        """
        @param string valor : Esta función carece de interés para esta clase
        @return bool : Esta función carece de interés para esta clase
        """
        return True


    def estado(self):
        """
        @return string : Retorna "encendido" si la turbina está encendida o retorna "apagado" si la turbina está apagada
        """
        return self._estado


    def refrescar(self, tiempoActual):
        """
        @param string tiempoActual : Tiempo actual del sistema
        @return string : Tiempo a la que desea que se vuelva a refrescar.
        """
        intervaloRefrescar=self._intervaloRefrescar


        print("refrescando turbina")
        return str(int(tiempoActual)+intervaloRefrescar)


    def modificarControlador(self, controlador):
        """
        @param dispositivos.interfaces.Controlador controlador : controlador que está conectado este dispositivo
        @return bool : Retorna True si es correcto, False en caso contrario
        """
        self._controlador = controlador
        return True


