# import random


# def ObtenerOpciones():
#   opcionJugador = input("Eliga una opcion (Piedra,Papel,Tijera)")
#   opciones = ["piedra", "papel", "tijera"]
#   opcionComputador = random.choice(opciones)
#   resultado = VerificarGanador(opcionJugador, opcionComputador)
#   return resultado


# def VerificarGanador(jugador,computador):
#   print(f"Jugador: {jugador} --- Computador: {computador}")
#   if (jugador==computador):
#     return "Es un Empate"
#   elif(jugador == "piedra" and computador == "tijera"):
#     return "Jugador Gana"
#   elif(jugador == "papel" and computador == "piedra"):
#     return "Jugador Gana"
#   elif(jugador == "tijera" and computador == "papel"):
#     return "Jugador Gana"
#   elif(jugador !="papel" and jugador !="piedra" and jugador != "tijera"):
#     return "Debe ingresar una opcion valida"
#   else:
#     return "Computador gana"
      
# print(ObtenerOpciones())


# print(type("asd")==str)
# print(isinstance("asd",str))
# print(isinstance(3,float))
# print(isinstance(float(3),float))
# print("Seba" in "Sebastian") # Sebastian
# print("Sebnastian"[1]) #devuelve la posision 1 es decir la e
# print("Sebnastian"[0:4]) #Sebn

# libro1 = True
# libro2 = False

# existeLibro = any([libro1,libro2])
# print(existeLibro) # true


# from enum import Enum


# class Estado(Enum):
#   INACTIVO =0 #son constantes que no cambian
#   ACTIVO= 1


# print(Estado.ACTIVO.value) #1
# print(Estado.ACTIVO) #Estado.ACTIVO
# print(Estado(1)) #Estado.ACTIVO


lista = ["agustin","toby",1,False]

print(lista[0]) #agustin
print("agustin" in lista) #true
lista.append("Seba") #agrega un nuevo elemento a la lista
print(lista[-1]) # devuelve el ultimo en la lista

