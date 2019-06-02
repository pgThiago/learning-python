# Faça um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na seqência
# no final mostre uma listagem e preços organizando os dados de forma tabular  


print('=' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
p = ('lapis', 1.75,
     'borracha', 2,
     'caderno', 15.90,
     'estojo', 25.00,)
print('=' * 40)

for pos in range(0, len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<30}', end=' ')
    else:
        print(f'RS:{p[pos]:>.2f}')
print('=' * 40)


#print('=' * 32)
#print('{:^32}'.format('LISTAGEM DE PREÇOS'))
#print('=' * 32)
#print('LISTAGEM DE PREÇOS')
#print('Lápis.................R$: 1.75 ')
#print('Borracha..............R$: 2.00')
#print('Caderno...............R$: 15.90')
#print('Estojo................R$: 25.00')
#print('Transferidor..........R$: 4.20')
#print('Compasso..............R$: 9.99')
#print('Mochila...............R$: 120.32')
#print('canetas...............R$: 22.30')
#print('livro.................R$: 34.90')
#print('=' * 32)
