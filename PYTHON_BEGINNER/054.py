# Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores.

from datetime import date
ano = date.today().year
velho = 0
novo = 0
for c in range(1, 8):
    nasceu = int(input('Em que ano a {}° pessoa nasceu: '.format(c)))
    if ano - nasceu >= 18:
        velho = velho + 1
    if ano - nasceu < 18:
        novo = novo + 1
print('Tivemos um total de {} pessoas novas'.format(novo), end='')
print(', e também {} pessoas maiores de idades'.format(velho))
