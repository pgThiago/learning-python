# Crie um programa que leia o nome e o preço de vários produtos 
# o programa deverá perguntar se o usuário vai continuar
# no final mostre:
# a) qual é o total gasto na compra
# b) quantos produtos custaram mais de R$:1000
# c) qual é o nome do produto mais barato

total = 0
mais = 0
cont = 0
barato = 0
nome_barato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto R$: '))
    cont += 1
    if cont == 1 or preco < barato:
        barato = preco
        nome_barato = nome
        if preco < barato:
            barato = preco
        if barato < preco:
            barato = preco
    if preco > 1000:
        mais += 1
    total += preco
    resp = ' '
    while resp not in 'SIMNÃONAO':
        resp = str(input('Deseja continuar [SIM / NÃO]? ')).strip().upper()
    if resp == 'NÃO' or resp == 'NAO':
        break
print(f'O total da compra foi de R$: {total}')
print(f'{mais} produtos custaram mais de R$:1000')
print(f'O produto mais barato foi o(a){nome_barato} que custou R$:{barato}')
