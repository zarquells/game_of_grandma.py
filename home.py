#  jogo da velha no console com dois players
#  exercicio de introdução a python
import numpy as np

map_grandma = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

while True:
    player = input('Bem-vindo ao game of grandma, qual vai ser seu personagem? X ou O?')
    if player.lower() != 'o' and player.lower() != 'x' and player.upper() != 'O' and player.upper() != 'X':
        print('Ops, esta não é uma opção válida. Tente novamente.')

    play = int(input(f'Escolha uma coordenada no mapa: \n {map_grandma[0]} \n {map_grandma[1]} \n {map_grandma[2]} \n'))
    # colocar try catch aqui para detectar quando a resposta não for int posteriormente
    if play < 1 or play > 10:
        print('Ops, esta não é uma opção válida. Tente novamente.')
        
    else:
        for i in range(len(map_grandma)):
            for y in range(len(map_grandma[i])):
                if str(play) == map_grandma[i][y]:
                    map_grandma[i][y] = player.upper()

        print(map_grandma)