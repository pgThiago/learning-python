# Faça um programa que leia umnúmero de 0 a 9999 e mostre na tela cadaa um dos dígitos separados.

numero = int(input('DIGITE UM NÚMERO: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
