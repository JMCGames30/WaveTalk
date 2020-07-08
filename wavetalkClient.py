#Cliente de WaveTalk, hecho por BrodaCode (Juan Manuel Camarasa)

#Importacion de modulos

import socket #Este modulo es el corazon del programa, sirve para conectarse al servidor y viceversa

#Importacion de variables

local_userName = ("DEFAULT_USERNAME") #Define el nombre que sera ingresado por el usuario
local_lastSentMessage = ("DEFAULT_LASTSENTMESSAGE") #Define el ultimo mensaje emitido
local_lastReceivedMessage = ("DEFAULT_LASTRECEIVEDMESSAGE") #Define el ultimo mensaje recibido

#Objeto Socket

socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creal el objeto Socket

#Main

try:
    socketObject.connect( ('localhost',8000) )
except:
    print("No se ha podido establecer una conexion al servidor especificado")

socketObject.send("Hola desde el cliente!".encode())
respuesta = mi_socket.recv(1024)

print (respuesta)
socketObject.close()
