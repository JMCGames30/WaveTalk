#WaveTalk v1.0.0 Codigo Fuente en Espanol
print("WaveTalk v1.0.0.")

#Variables

local_lastSentMessage = ("DEFAULTLASTSENTMESSAGE") #Indica el string del ultimo mensaje enviado para enviar a otros clientes de WaveTalk
local_lastReceivedMessage = ("DEFAULTLASTRECEIVEDMESSAGE") #Indica el string del ultimo mensaje recibido para que el cliente lo obtenga
local_username = ("DEFAULTUSER") #Indica el nombre de usuario
local_connectedUsers = [] #Indica los nombres de usuario de los clientes conectados
local_userIdentifier = 0000 #Numero identificador del cliente en la red
local_networkIdentifiers = [] #Numeros identificadores en la red


#Modulos

import os
import random

#Funciones

def getIdentifier():
	global local_userIdentifier
	local_userIdentifier = random.randint(1,4444)

def login(temp_username):
	global local_username
	global local_connectedUsers
	global local_userIdentifier
	global local_networkIdentifiers

	if not local_username in local_connectedUsers:
		local_connectedUsers.append(temp_username)
		local_networkIdentifiers.append(local_userIdentifier)
	else:
		print("El nombre de usuario ya esta en uso")