# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# só que agora o jogador vai tentar adivinhar até acertar.
# Mostre no final quantos palpites foram necessários para vencer. 

from random import randint
from time import sleep
print('\033[;35mMY NAME IS THIAGO MACHINE...\033[m')
sleep(2)
pc = randint(0, 10)
print('\033[;35mAcabei de pensar em um número entre 0 e 10\033[m')
sleep(2)
print('\033[;35mSerá que você consegue adivinhar?\033[m')
sleep(2)
nome = str(input('\033[;36mQual o seu nome?\033[m')).strip().capitalize()
eu = ''
tentativas = 0
while pc != eu:
    eu = int(input('\033[;33mQual o seu chute? '))
    tentativas += 1
    if pc == eu:
        sleep(2)
        print('PARABÉNS, {}! Você acertou, também pensei no número {}'.format(nome, pc))
        print('Você acertou com {} tentativas'.format(tentativas))
    if pc > eu:
        sleep(2)
        print('Mais... Tente novamente.')
    if pc < eu:
        sleep(2)
        print('Menos... Tente novamente.')


