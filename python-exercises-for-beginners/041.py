# A Federação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria.
# de acordo com a sua idade
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SENIOR
# Acima: MASTER

from datetime import date
ano = date.today().year
nascimento = int(input('Ano de nascimento: '))
if ano - nascimento <= 9:
    print('Categoria Mirim')
if ano - nascimento > 9 and ano - nascimento <= 14:
    print('Categoria Infantil')
if ano - nascimento > 14 and ano - nascimento <= 19:
    print('Categoria Junior')
if ano - nascimento > 19 and ano - nascimento <= 20:
    print('Categoria Sênior')
if ano - nascimento >= 20:
    print('Categoria Master')