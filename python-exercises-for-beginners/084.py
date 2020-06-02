# Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista.
# no final mostre:
# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com as pessoas mais leves

temp = []
prc = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(prc) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    prc.append(temp[:])
    temp.clear()

    resp = str(input('Deseja continuar? [s/n]: '))
    if resp in 'n':
        break
print('~' * 50)
print(f'Ao todo você cadastrou {len(prc)} pessoas!')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for gordo in prc:
    if gordo[1] == maior:
        print(f'[{gordo[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de', end=' ')
for magro in prc:
    if magro[1] == menor:
        print(f'[{magro[0]}]', end=' ')
