# Refaça o exercicio 051 lendo o primeiro termo e a razão de uma PA.
# mostre os 10 primeiros termos da progressão usando a estrutura while

print('==== GERADOR DE PA ====')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
c = 1
while c <= 10:
    print(termo, end=' ')
    c += 1
    termo += r
print('FIM')
