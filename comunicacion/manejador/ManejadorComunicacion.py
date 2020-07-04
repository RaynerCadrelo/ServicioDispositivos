# coding=UTF-8
from comunicacion.interfaz.MedioComunicacion import *

class ManejadorComunicacion (MedioComunicacion):

    def __init__(self, medioComunicacion):
        """
        @param interfaces.MedioComunicacion medioComunicacion : 
        @return  :
        """
        self._medioComunicacion=medioComunicacion
        self._medioComunicacion.iniciar()

    def existeSolicitud(self):
        """
         Verificación de si existe alguna solicitud por los medios de comunicación

        @return bool :
        """
        return self._medioComunicacion.existeSolicitud()

    def leerSolicitud(self):
        """
        @return string :
        """
        return self._medioComunicacion.leerSolicitud()

    def escribirRespuesta(self,solicitud, respuesta):
        """
        @param string respuesta : 
        @return  :
        """
        self._medioComunicacion.responderSolicitud(solicitud, respuesta)




