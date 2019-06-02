# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
from time import sleep
print('=' * 35)
print('{:^35}'.format('JOGA NA MEGA SENA'))
print('=' * 35)
n = int(input('Quantos jogos você quer que eu sorteie? '))
c = list(range(1, 61))
for i in range(n):
    sleep(1)
    print(f'Jogo [{i + 1}]: {random.sample(c, 6)}')
sleep(2)
print('=' * 35)
print('{:^30}'.format('BOA SORTE!'))
print('=' * 35)
