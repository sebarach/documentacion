import random

def ObtenerOpciones():
  opcionJugador = input("Eliga una opcion (Piedra,Papel,Tijera)")
  opciones = ["piedra","papel","tijera"]
  opcionComputador = random.choice(opciones)
  resultado = VerificarGanador(opcionJugador,opcionComputador)
  return resultado


def VerificarGanador(jugador,computador):
  print(f"Jugador: {jugador} --- Computador: {computador}")
  if (jugador==computador):
    return "Es un Empate"
  elif(jugador == "piedra" and computador == "tijera"):
    return "Jugador Gana"
  elif(jugador == "papel" and computador == "piedra"):
    return "Jugador Gana"
  elif(jugador == "tijera" and computador == "papel"):
    return "Jugador Gana"
  elif(jugador !="papel" and jugador !="piedra" and jugador != "tijera"):
    return "Debe ingresar una opcion valida"
  else:
    return "Computador gana"
      
print(ObtenerOpciones())