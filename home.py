#  jogo da velha no console com dois players
#  exercicio de introdução a python
import numpy as np

map_grandma = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

while True:
    # player escolhe seu avatar
    player = input('Bem-vindo ao game of grandma, qual vai ser seu personagem? X ou O?')

    # valida se é uma das opções
    if player.lower() != 'o' and player.lower() != 'x' and player.upper() != 'O' and player.upper() != 'X':
        print('Ops, esta não é uma opção válida. Tente novamente.')

    # rastreia cada objeto dentro da matriz (9 objetos na matriz)
    for i in range(len(map_grandma)):
        for y in range(len(map_grandma[i])):
            # pede a jogada do player em relação aquele round (9 rounds : 9 objetos)
            play = int(input(f'Escolha uma coordenada no mapa: \n {map_grandma[0]} \n {map_grandma[1]} \n {map_grandma[2]} \n'))
#error: criar validação que previna caso o usuário coloque algo diferente de 'int'

            # mapeia cada objeto na matriz e compara com a jogada do player
            for i in range(len(map_grandma)):
                for y in range(len(map_grandma[i])):
                    # caso seja correspondente ao objeto encontrado, lança a jogada
                    if str(play) == map_grandma[i][y]:
                        map_grandma[i][y] = player.upper()
#error: criar 'break' para o 'for' quando encontrar a coordenada
#error: criar validação caso o usuário coloque coordenada já ocupada

            # troca de player
            if i % 2 == 0 and player.upper() == 'O':
                player = 'X'
            elif player.upper() == 'X':
                player = 'O'

#update: criar validação de vitória e para o 'while'