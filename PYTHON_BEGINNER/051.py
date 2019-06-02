# Desenvolva um programa que leia o primeiro termo e a razão de uma PA
# no final mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
n = a1 + (10 - 1) * r
for c in range(a1, n, r):
    print('{} > '.format(c), end='')
print('Acabou')
