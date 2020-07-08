#Software de servidores de WaveTalk

print("WaveTalk Server Software")

#Importacion de modulos

import socket

#Variables

#Objeto Socket

socketObject = socket.socket() #Crea el objeto socket
socketObject.bind(("localhost", 65519)) #Le da una direccion al servidor para que se pueda acceder con un cliente
socketObject.listen(5) #Hace la funcion de servidor

while True:
	conexion, addr = socketObject.accept() #Acepta la conexion entrante automaticamente
	print("Se ha establecido una conexion de la direccion: ") #Indica que se establecio la conexion
	print (addr) #Muestra la direccion de la que viene la conexion entrante

	conexion.send("Bienvenido al servidor de prueba de WaveTalk!".encode())
	conexion.close()

