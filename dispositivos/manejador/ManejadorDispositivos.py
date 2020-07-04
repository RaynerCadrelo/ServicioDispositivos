# coding=UTF-8
from dispositivos.interfaz.Dispositivo import *
from controladores.interfaz.Controlador import *
import time

class ManejadorDispositivos(object):

    def __init__(self):
        self._dispositivos=[]
        self._tiemposRefrescar=[]

    def anadirDispositivo(self, dispositivo, controlador):

        dispositivo.modificarControlador(controlador) #entregarle el controlador correspondiente a ese dispositivo
        self._dispositivos.append(dispositivo)
        self._tiemposRefrescar.append(str(int(time.time())))


    def ejecutarSolicitud(self, solicitud):
        """
         Se envía la solicitud y se espera una respuesta, esta respuesta podría ser el valor
         de algún dispositivo. solicitud está compuesto por "nombreDelDispositivo acción valor"
         retorno "nombreDelDispositivo valor"

        @param string solicitud : 
        @return string :
        """
        solicitud=str(solicitud)
        if len(solicitud.split())<3:
            return "error"

        nombreDispositivo, accion, valor = ss.split()[0], ss.split()[1], ss.split()[2:]

        for a in self._dispositivos:
            if str(a.leerNombre()) == nombreDispositivo:
                if accion == "encender":
                    return str(a.leerNombre()) + " " + str(a.encender())
                elif accion == "apagar":
                    return str(a.leerNombre()) + " " + str(a.apagar())
                elif accion == "leerValor":
                    return str(a.leerNombre()) + " " + str(a.leerValor())
                elif accion == "escribirValor":
                    return str(a.leerNombre()) + " " + str(a.escribirValor(valor))
                elif accion == "estado":
                    return str(a.leerNombre()) + " " + str(a.estado())
                else:
                    return "error"
        return "error"       


    def refrescar(self):

        for a in self._dispositivos:
            indice=self._dispositivos.index(a)
            if int(self._tiemposRefrescar[indice]) <= int(time.time()):
                self._tiemposRefrescar[indice] = a.refrescar(str(int(time.time())))



