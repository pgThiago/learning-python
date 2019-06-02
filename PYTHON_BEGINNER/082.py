# Crie um programa que vai ler vários números e colocar em uma lista.
# depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# ao final mostre o conteúdo das 3 listas geradas

lista = []
pares = []
impares = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    resp = input('Quer continuar? [S / N] ').upper()
    if 'N' in resp:
        break
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores da lista são {lista}')
print(f'Os valores pares são {pares}')
print(f'Os valores ímpares são {impares}')
