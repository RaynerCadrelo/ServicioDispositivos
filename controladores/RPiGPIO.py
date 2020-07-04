# coding=UTF-8
import configparser
from controladores.interfaz.Controlador import *
import RPi.GPIO as gpio
import sys
import time
import io

class RPiGPIO (Controlador):
    def __init__(self, config):      

        #board pin in/out description
        gpio.setmode(gpio.BCM)

        #set pin as output
        #gpio.setup(self.pinActivation5, gpio.OUT)
        #set pin to initial low level
        #gpio.output(self.pinActivation5, False)

        self._pinesSalida=[]



    def enviarRecibirDato(self, dato):
        if dato[0:4]=="alto":
            if self._pinesSalida.count(int(dato[4:])) == 0:
                gpio.setup(int(dato[4:]), gpio.OUT)
                self._pinesSalida.append(int(dato[4:]))
            gpio.output(int(dato[4:]), True)
        elif dato[0:4]=="bajo":
            if self._pinesSalida.count(int(dato[4:])) == 0:
                gpio.setup(int(dato[4:]), gpio.OUT)
                self._pinesSalida.append(int(dato[4:]))
            gpio.output(int(dato[4:]), False)
        else:
            return "error"
        return dato
            


#Probar funcionamiento
def main(argv):
    rpi = RPiGPIO() 
    print(rpi.enviarRecibirDato("gpio5_alto"))
	
if __name__ == '__main__':
    import sys
    
    sys.exit(main(sys.argv))
