# Crie um programa que faça o computador jogar JOKENPÔ com você

import random

ask = str(input('Vamos jogar pedra, papel, tesoura? ')).strip().upper()

lista = ['PEDRA', 'PAPEL', 'TESOURA']

pc = random.choice(lista)

if ask == 'SIM':
    print('Já é, parça. Manda tua jogada!')
escolha = str(input('Escolha sua jogada: ')).upper()

if escolha == 'PEDRA' and pc == 'TESOURA':
    print('Você VENCEU')
    print('Você jogou PEDRA e o Computador TESOURA')

elif escolha == 'PAPEL' and pc == 'PEDRA':
    print('Você VENCEU')
    print('Você jogou PAPEL e o Computador PEDRA')

elif escolha == 'TESOURA' and pc == 'PAPEL':
    print('Você VENCEU')
    print('Você jogou TESOURA e o Computador PAPEL')

elif escolha == pc:
    print('Ninguém venceu: EMPATE')

else:
    print('Você jogou {} e o Computador {}, portanto, o COMPUTADOR venceu'.format(escolha, pc))
