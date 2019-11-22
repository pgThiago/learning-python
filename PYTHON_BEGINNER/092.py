# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) 
# em um dicionário se por acaso a ctps for diferente de zero, o dicionáio receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
data_atual = date.today()
ano_atual = data_atual.year
cadastro = {}
cadastro['Nome'] = input('Nome: ')
cadastro['Ano de nascimento'] = int(input('Ano de nascimento: '))
cadastro['Carteira de trabalho'] = int(input('Carteira de trabalho (0 caso não tenha): '))
if cadastro['Carteira de trabalho'] == 0:
    cadastro['Idade'] = ano_atual - cadastro['Ano de nascimento']
    for trabaiador, valor in cadastro.items():
        if trabaiador != 'Ano de nascimento':
            print(f'- {trabaiador} tem o valor {valor}')
        
else:
    cadastro['Idade'] = ano_atual - cadastro['Ano de nascimento']
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = (cadastro['Ano de contratação'] - cadastro['Ano de nascimento'] + 35)
for trabaiador, valor in cadastro.items():
    print(f'- {trabaiador} tem o valor {valor}')
