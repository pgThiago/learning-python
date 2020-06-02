# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequÊncia de FIBONACCI.

# 0 1 1 2 3 5 8 13 21...
print('=' * 22)
print('SEQUENCIA DE FIBONACCI')
print('=' * 22)
n = int(input('Digite um número: '))
c = 3
p = 0
s = 1
t = p + s
print(p, s, end=' ')
while c <= n:
    t = p + s
    p = s
    s = t
    c += 1
    print(t, end=' ')

