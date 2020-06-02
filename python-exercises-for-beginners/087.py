#            RESUMI A QUESTÃO 86 E 87 EM UMA, POR ISSO ESTÃO IGUAIS.
# Crie uma matriz de dimensão 3 X 3 e preencha com valores lidos pelo teclado
# No final mostre a matriz na tela com a formatação correta.

''' Mais sobre matriz em python 087'''

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma_terceira = []
soma_terceira_coluna = 0
maior_linha2 = []
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = (input(f'Digite o valor para [{l}, {c}]: '))
        if l == 0 and c == 2:
            soma_terceira.append(m[l][c])
        if l == 1 and c == 2:
            soma_terceira.append(m[l][c])
        if l == 2 and c == 2:
            soma_terceira.append(m[l][c])
        if l == 1:
            maior_linha2.append(m[1][c])
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {m[l][c]:^5} ]', end=' ')
    print()
par = 0
for i in m:
    for n in i:
        if int(n) % 2 == 0:
            par += int(n)
for t in soma_terceira:
    soma_terceira_coluna += int(t)
print(f'A soma dos números pares desta matriz é igual a: {par}')
print(f'A soma dos valores da terceira coluna desta matrix é igual a: {soma_terceira_coluna}')
print(f'O maior valor da 2° linha desta matriz é: {max(maior_linha2)}')
