# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e menor peso lidos.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior {maior}')
print(f'O menor {menor}')
