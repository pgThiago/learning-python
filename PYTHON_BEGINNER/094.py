# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
# cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas 
# B) A média de idade
# C) Uma lista com mulheres
# D) Uma lista com idade acima da média
cadastro = []
pessoa = {}

while True:
    pessoa['Nome'] = input('Nome: ').strip().upper()
    pessoa['Sexo'] = input('Sexo [M/F]: ').strip().upper()
      
    if pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = input('Sexo [M/F]: ').strip().upper() 
    pessoa['Idade'] = int(input('Idade: '))

    cadastro.append(pessoa.copy())
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    else:
        if continuar != 'N' and continuar != 'S':
            print('Digite apenas N ou S')
            continuar = input('Quer continuar? [S/N] ').strip().upper()
            if continuar == 'N':
                break

print('==' * 30)
soma = 0
mulheres = []
acima_da_media = []

for pessoa in cadastro:
    for key, value in pessoa.items():
        if value == 'F':
            mulheres.append(pessoa['Nome'])
        if key == 'Idade':
            soma += value
media = soma / len(cadastro)
for pessoa in cadastro:
    for key, value in pessoa.items():
        if key == 'Idade' and value > media:
            acima_da_media.append(pessoa['Nome'])
molieres = acima = ''
for m in mulheres:
    molieres += f'{m}, '
    if molieres[-2] == ',':
        molieres = molieres.replace(molieres[-2], '.')

if len(acima_da_media) == 0:
    acima = 'ninguém está acima da média!'
else:
    for old in acima_da_media:
        acima += f'{old}, '

print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram {molieres}')
print(f'D) Lista das pessoas que estão acima da média: {acima}')
