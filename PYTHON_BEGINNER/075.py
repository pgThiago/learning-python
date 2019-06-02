# Desenvolva um program que leia 4 valores pelo teclado e guarde-os em uma tupla.
# no final mostre:
# a) quantas vezes apareceu o valor 9
# b) em que posição foi digitado o valor 3
# c) quais foram os números pares

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último númeroro: ')))
print(f'Você digitou os números {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)}° posição')
else:
    print('Número 3 não existe nessa tupla')
for par in n:
    if par % 2 == 0:
        print(f'Os números pares digitados {par}')
