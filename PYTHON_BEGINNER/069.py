# Crie um programa que leia a idade e o sexo de várias pessoas.
# a cada pessoa cdastrada o programa deverá perguntar se a pessoa quer ou não continuar.
# no final mostre:
# a) Quantas pessoas tem mais de 18 anos
# b) Quantos homens foram cadastrados
# c) Quantas mulheres tem menos de 20 anos

machu = femi = maiores = femi_novas = 0
while True:
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if 'M' in sexo:
        machu += 1
    if 'F' in sexo:
        femi += 1
    if 'F' in sexo and idade < 20:
        femi_novas += 1
    if idade >= 18:
         idade += 1
    if 'N' in continuar:
        break
print(f'{idade} Maiores de 18 anos')
print(f'{machu} Homens cadastrados')
print(f'{femi} Mulheres cadastradas')
print(f'{femi_novas} Mulheres com idade menor de 20 anos')
