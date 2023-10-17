import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Elije: 1->Piedra 2->Papel 3->Tijera ')
  user_option = user_option.lower()
  
  if user_option not in options:
    print('Opción inválida')
    #continue lo vamos a rremplazar con none
    return None, None
  
  pc_option = random.choice(options)
  
  print('Selección de jugador -> ', user_option)
  print('Selección del PC -> ', pc_option)

  return user_option, pc_option

def game_rules(user_option, pc_option, user_w, pc_w):
  if user_option == pc_option:
    print('Es un empate')
  elif user_option == 'piedra':
    if pc_option == 'papel':
      print('Has perdido! papel sobre piedra')
      pc_w +=1
    else:
      print('Has ganado! piedra sobre tijera')
      user_w += 1
  elif user_option == 'papel':
    if pc_option == 'piedra':
      print('Has ganado! papel sobre piedra')
      user_w += 1
    else:
      print('Has perdido! tijera sobre papel')
      pc_w +=1
  else:
    if pc_option == 'piedra':
      print('Has perdido! piedra sobre tijera')
      pc_w +=1
    else:
      print('Has ganado! tijera sobre papel')
      user_w += 1
  return user_w, pc_w


def run_game():
  user_w = 0
  pc_w = 0
  round = 1

  while True:
  
    print('~' * 10)
    print('ROUND', round)
    print('~' * 10)
    
    user_option, pc_option = choose_options()
    
    user_w, pc_w = game_rules(user_option, pc_option, user_w, pc_w)
        
    round += 1
    print('User ->', user_w)
    print('Pc ->', pc_w)
  
    if user_w > 1:
      print('Has derrotado al pc!!! :)')
      break
  
    if pc_w > 1:
      print('Has sido derrotado por el pc :(')
      break
  
  print('Resultado Final')
  print('User ->', user_w)
  print('Pc ->', pc_w)

run_game()