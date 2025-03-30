#  jogo da velha no console com dois players
#  exercicio de introdução a python
import numpy as np
import os

# limpa a linha de comando Windows
os.system('cls')
while True: 
    map_grandma = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

    # player escolhe seu avatar
    player = input('\nBem-vindo ao game of grandma, qual vai ser seu personagem? X ou O?\n')

    if player.lower() != 'o' and player.lower() != 'x' and player.upper() != 'O' and player.upper() != 'X':
        # valida se é uma das opções de avatar
        print('\nOps, esta não é uma opção válida. Tente novamente.')
        continue

    # variáveis utilizadas por partida
    count = 0
    again = 's'

    # inicia uma partida
    while True:
        try:
            # pede a jogada do player
            play = int(input(f'\nEscolha uma coordenada no mapa: \n {map_grandma[0]} \n {map_grandma[1]} \n {map_grandma[2]} \n'))
        except Exception:
            # trata erros caso insira texto, etc.
            print('\nOps, esta não é uma opção válida. Tente novamente.')
            continue

        if str(play) not in map_grandma:
            # valida se é um valor existente na matriz
            print('\nOps, esta não é uma opção válida. Tente novamente.')
            continue

        # localiza e armazena o índice onde este valor é presente
        ind = np.where(map_grandma == str(play))

        #  substitui pela jogada
        map_grandma[ind] = player.upper()

        # contabiliza o round
        count += 1

        if np.any(np.all(map_grandma == player, axis=1)):
        # verifica se existe uma linha preenchida pelo player do round atual
            print(f'\n {map_grandma[0]} \n {map_grandma[1]} \n {map_grandma[2]} \nO jogador {player} venceu a partida!')
            ask = input('\nDeseja jogar novamente? s/n\n')
            again = ask
            break
        elif np.any(np.all(map_grandma == player, axis=0)):
        # verifica se existe uma coluna preenchida pelo player do round atual
            print(f'\n {map_grandma[0]} \n {map_grandma[1]} \n {map_grandma[2]} \nO jogador {player} venceu a partida!')
            ask = input('\nDeseja jogar novamente? s/n\n')
            again = ask
            break
        elif np.any(np.all(np.diag(map_grandma) == player)):
        # verifica se a diagonal está preenchida pelo player do round atual
            print(f'\n {map_grandma[0]} \n {map_grandma[1]} \n {map_grandma[2]} \nO jogador {player} venceu a partida!')
            ask = input('\nDeseja jogar novamente? s/n\n')
            again = ask
            break
        elif count == 9:
        # caso nenhuma condição seja verdadeira, encerra a partida
            ask = input('\nJogo Encerrado. Deu velha! \nDeseja jogar novamente? s/n\n')
            again = ask
            break

        # troca de player
        if player.upper() == 'O':
            player = 'X'
        elif player.upper() == 'X':
            player = 'O'

    # verifica se o jogador reiniciou o jogo
    if again.lower() == 's':
        continue
    elif again.lower() == 'n':
        print('\nObrigada por jogar :D')
        break
    else:
        print('\nOps, esta não é uma opção válida. Mas ainda assim, jogo encerrado :D')
        break