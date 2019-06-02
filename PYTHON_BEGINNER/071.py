# Crie um programa que simule o funcionamento de um caixa eletrônico.
# no inicio pergunte ao usuário qual saera´o valor a ser sacado (numero inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregue 

from math import trunc
print('=' * 30)
print('{:^30}'.format('BANCO ROUBA MAS FAZ'))
print('=' * 30)
cinq = vint = dez = real = 0
while True:
    saque = float(input('Quanto deseja sacar? R$: '))
    if saque // 50:
        cinq = saque // 50
        resto1 = saque % 50
        if cinq > 0.99:
            print(f'{trunc(cinq)} cédulas de R$:50')
        if resto1 / 20:
            vint = resto1 / 20
            resto2 = resto1 % 20
            if vint > 0.99:
                print(f'{trunc(vint)} cédulas de R$:20')
            if resto2 / 10:
                dez = resto2 / 10
                resto3 = resto2 % 10
                if dez > 0.99:
                    print(f'{trunc(dez)} cédulas de R$:10')
                if resto3 / 1:
                    real = resto3 / 1
                    if real > 0.99:
                        print(f'{trunc(real)} cédulas de R$:1')
                        if 1 < 2:
                            break
