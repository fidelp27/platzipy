import random

#Variables
choice = ""
eleccion = ""
pc = ""
intentos = ""
puntos_user = 0
puntos_pc = 0
contador = 0


#Obtener opción del usuario
def get_choice():
  global choice
  choice = int(input(
  """Elije una  opción: 
  1 - piedra
  2 - papel
  3 - tijera
  """
  ))
  get_selection(choice)

def get_selection(number):
  global eleccion
  global intentos
  if number == 1:
    eleccion =  "piedra"
  elif number == 2:
    eleccion =  "papel"
  elif number == 3: 
    eleccion =  "tijera"
  else:
    print("Opción errada, vuelve a intentarlo")
    get_choice()


#Obtener opción de PC  
def get_pc_option():
  global pc
  options_array = ["piedra", "papel", "tijera"]
  random_number = random.randint(0, 2)
  pc = options_array[random_number]
  return pc


#Mensajes por ronda y ganador del juego
def message(type,winner):
  global puntos_pc
  global puntos_user
  if(type == "round"):
    print('-'*50)
    print(f"User eligió {eleccion} y pc eligió {pc} - {winner}")
    print('-'*50)
  elif(type == "endgame"):
    print('*-'*30)
    print(f"PC tiene {puntos_pc} puntos y user {puntos_user} puntos {winner}")    
    print('*-'*30)


#Definir ganador por ronda
def winner():
  global pc
  global eleccion
  global puntos_user
  global puntos_pc
  if(eleccion == pc):
    message("round", "Empate")
  elif((eleccion == "piedra" and pc == "tijera") or (eleccion == "tijera" and pc == "papel") or (eleccion == "papel" and pc == "piedra")):
    message("round","Ganó user")
    puntos_user += 1
  else:
    message("round","Ganó PC")
    puntos_pc += 1

#Definir ganador del juego
def winner_game():
  global puntos_pc
  global puntos_user
  if(puntos_pc > puntos_user):
    message("endgame","El ganador es PC")
  elif(puntos_pc < puntos_user):
    message("endgame","El ganador es USER")
  else:
    message("endgame","Es un Empate")


#Separador de rounds
def print_round():
  global contador
  print('*'*20)
  print('ROUND ', contador + 1)
  print('*'*20)


#Inicio del juego
def start_game():
  global intentos
  global contador
  intentos = int(input("¿Cuántos intentos deseas jugar?"))
  
  while contador < intentos:
    print_round()
    contador += 1
    get_choice()
    get_pc_option()
    winner()
    continue
    
  winner_game()

#Ejecución  
start_game()
  




