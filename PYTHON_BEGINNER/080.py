# Faça um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista
# já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela. 

valor = []
for c in range(5):
    v = input('Digita a porra de um valor ae: ')
    if not valor or v > max(valor):
        valor.append(v)
        print('Valor adicionado ao final da lista...')
    elif v < valor[0]:
        valor.insert(0, v)
        print('Valor adicionado na posição 0 da lista...')
    elif valor[0] < v < valor[1]:
        valor.insert(1, v)
        print('Valor adicionado na posição 1 da lista...')
    elif valor[1] < v < valor[2]:
        valor.insert(2, v)
        print('Valor adicionado na posição 2 da lista...')
    elif valor[2] < v < max(valor):
        valor.insert(3, v)
        print('Valor adicionado na posição 3 da lista...')
print('==' * 30)
print(f'Os valores digitados em ordem são {valor}')

'''lista = []
for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('O número foi adicionado no final da lista.')
    else:
        for i in range(5):
            if n <= lista[i]:
                lista.insert(i, n)
                print(f'O número foi adicionado na posição {i}.')
                break
print(lista)'''
