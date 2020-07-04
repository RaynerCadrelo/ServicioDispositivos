# coding=UTF-8

import configparser

from comunicacion.manejador.ManejadorComunicacion import *
from dispositivos.manejador.ManejadorDispositivos import *

from comunicacion.Socket import *

from controladores.RPiGPIO import *

from dispositivos.Turbina import *
from dispositivos.RiegoUno import *

import time
import os

directorio = os.path.dirname(os.path.abspath(__file__))

class Inicio(object):

    def ejecutar(self):

        time.sleep(5)

        config = configparser.ConfigParser()
        config.read(directorio+'/config.ini')  

        #DISPOSITIVOS ELECTRÓNICOS

        #Crear los dispositivos
        turbina=Turbina('Turbina',config)
        riegoUno=RiegoUno('RiegoUno',config)

        #Crear controladores
        rpiGpio = RPiGPIO(config)

        #Crear el manejador de dispositivos
        manejadorDispositivos=ManejadorDispositivos()

        #Añadiendo los dispositivos creados y el microcontrolador al que está conectado el dispositivo
        manejadorDispositivos.anadirDispositivo(turbina, rpiGpio)
        manejadorDispositivos.anadirDispositivo(riegoUno, rpiGpio)



        #COMUNICACIÓN
        
        #Crear el objeto de comunicación se empleará
        comunicacionSocket=Socket(config)
        

        #Crear el manejador de Comuncicación y entregarle el medio de comunicación en específico
        manejadorComunicacionSocket=ManejadorComunicacion(comunicacionSocket)

        #Comienza el ciclo infinito para hacer funcionar los dispositivos y vincularlos con la comunicación
        manejadoresComunicacion=[manejadorComunicacionSocket]

        while True:
            for mc in manejadoresComunicacion:
                if mc.existeSolicitud():
                    print("solicitud encontrada")
                    solicitud = mc.leerSolicitud()
                    respuesta = manejadorDispositivos.ejecutarSolicitud(solicitud)
                    mc.escribirRespuesta(solicitud, respuesta)
                
            manejadorDispositivos.refrescar()
            time.sleep(0.5)










def main(argv):
    
#    config = configparser.ConfigParser()
#    config.read('config.ini')  
    Inicio().ejecutar()
    
	
if __name__ == '__main__':
    import sys
    
    sys.exit(main(sys.argv))
