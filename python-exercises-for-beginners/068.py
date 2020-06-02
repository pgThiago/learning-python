# Faça um programa que jogue par ou ímpar com o computador
# o jogo só será interrompido quando o jogador perder
# mostre o total de vitórias consecutivas que ele conquistou no final do jogo

print('\033[;34mTHIAGO MACHINE: jogo do par ou ímpar\033[m')
from random import randint
cont = 0
while True:
    eu = int(input('Qual sua jogada? '))
    pc = randint(1, 10)
    pi = str(input('[P/I]: ')).upper()
    if 'P' in pi and (eu + pc) % 2 == 0 or 'I' in pi and (eu + pc) % 2 != 0:
        cont += 1
        print(f'\033[;35mVocê jogou {eu} e o THIAGO MACHINE {pc}, portanto, você venceu por ter escolhido {pi}\033[m')
    if 'P' in pi and (eu + pc) % 2 != 0 or 'I' in pi and (eu + pc) % 2 == 0:
       print('\033[;35mTHIAGO MACHINE venceu\033[m')
       break
print(f'\033[;35mVocê venceu {cont} vezes\033[m')
print(f'\033[;34mTHIAGO MACHINE jogou {pc}')
