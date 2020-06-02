# Faça um programa que leia o nome de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se aalistar no serviço militar, se é a hora de se alistar, ou seja, 
# passou do tempo do alistamento. Seu programa também deverá informar o tempo que falta ou o tempo que passou do prazo.

from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
atraso = idade - 18
ano_atraso = ano - atraso
alistar = 18 - idade
futuro = ano + alistar
print('Quem nasceu em {} tem {} anos'.format(nascimento, idade))
if idade < 18:
    print('Você deverá se alistar daqui a {} anos'.format(alistar))
    print('Seu alistamento será em {}'.format(futuro))
elif idade == 18:
    print('Você está no ano de alistamento. Compareça a junta militar mais próxima de sua residência!')
elif idade > 18:
     print('Você deveria ter se alistado há {} anos'.format(atraso))
     print('Seu alistamento foi em {}'.format(ano_atraso))
