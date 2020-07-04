# coding=UTF-8
import configparser
from dispositivos.interfaz.Dispositivo import *
import os
import time
import datetime

class RiegoUno (Dispositivo):

    def __init__(self, nombre, config):
        
        super().__init__()
        self._nombre=nombre
        self._solicitudEncendido="alto"+ config['RIEGO_UNO']['PIN_ENCENDIDO_APAGADO']
        self._solicitudApagado="bajo"+ config['RIEGO_UNO']['PIN_ENCENDIDO_APAGADO']
        self._horaEncendido = time.time()
        self._tiempoMaxEncendido = int(config['RIEGO_UNO']['TIEMPO_MAX_ENCENDIDO'])

        self._horasEncender = config['RIEGO_UNO']['HORAS_ENCENDER'].split()
        self._horaUltimaEncendido = "25"
        
        self._estado="apagado"
        self._intervaloRefrescar=int(config['RIEGO_UNO']['INTERVALO_REFRESCAR']) # intervalo en segundos en que se llamará la función refrescar()


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
        self._horaEncendido = time.time()
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
        if self._horasEncender.count(str(datetime.datetime.now().hour)) != 0 and self._horaUltimaEncendido != str(datetime.datetime.now().hour):
            self._horaUltimaEncendido = str(datetime.datetime.now().hour)
            self.encender()
            intervaloRefrescar = 2

        if self._estado=="encendido":
            intervaloRefrescar = 2
            if self._tiempoMaxEncendido<(time.time()-self._horaEncendido):
                self.apagar()
            

        print("refrescando Riego 1")
        return str(int(tiempoActual)+intervaloRefrescar)

    def modificarControlador(self, controlador):
        """
        @param dispositivos.interfaz.Controlador controlador : microcontrolador que está conectado este dispositivo
        @return bool : Retorna True si es correcto, False en caso contrario
        """
        self._controlador = controlador
        return True


