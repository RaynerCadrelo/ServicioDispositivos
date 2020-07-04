# coding=UTF-8
import configparser
from comunicacion.interfaz.MedioComunicacion import *
import socket
import threading
import time


class Socket (MedioComunicacion):

        ###################  SERVIDOR SOCKET  ###############################
    def servidorSocket(self, solicitud, respuesta):
        try:
            s = socket.socket()
            s.bind((self._ip, self._puerto))
            s.listen(1)            
            while True:
                print("esperando cliente...")
                sc, addr = s.accept()
                print("cliente encontrado desde:",addr)
                self._solicitud = sc.recv(1024).decode()          #recibido contiene: [dispositivo] [funcion]. Siempre se retornará al cliente
                a=0
                while self._respuesta=="" and a<100:
                    time.sleep(0.2)
                    a=a+1
                sc.send((self._respuesta+'\n').encode('utf8'))
                self._respuesta=""
                sc.close()
            s.close()
        except:
            pass 

    def __init__(self, config):
        
        self._ip = config['SOCKET']['DIRECCION_IP']
        self._puerto = int(config['SOCKET']['PUERTO'])
        print(self._puerto)
        print(self._ip)
        self._solicitud=""
        self._respuesta=""
        

    
    def iniciar(self):
        t = threading.Thread(target=self.servidorSocket, args=(self._solicitud , self._respuesta))
        t.daemon = True
        t.start()
        return True


    def leerSolicitud(self):
        """
        @return string : leer la solicitud que entregan por el medio comunicación
        """
        solicitud=self._solicitud
        self._solicitud=""
        return solicitud

    def responderSolicitud(self, solicitud, respuesta):
        """
        @param string solicitud : solicitud que le habían hecho
        @param string respuesta : respuesta a esa solicitud
        @return bool :
        """
        self._respuesta=respuesta
        return True

    def existeSolicitud(self):
        """
         Verificación de si existe alguna solicitud por los medios de comunicación

        @return bool :
        """
        if self._solicitud == "":
            return False
        else:
            return True
