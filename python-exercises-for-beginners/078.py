# Faça um programa que leia 5 valores numéricos e guarde os em uma lista
# no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valores = []
for c, v in enumerate(range(0, 5)):
    valores.append(int(input('Digite o valor na Posição {}: '.format(v))))
    a = max(valores)
    b = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor da lista foi o {a} na posição {valores.index(a)}')
print(f'O menor valor da lista foi o {b} na posição {valores.index(b)}')
