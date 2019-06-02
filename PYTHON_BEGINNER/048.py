# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
# e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for t in range(1, 501, 2):
    if t % 3 == 0:
        soma = soma + t
        cont = cont + 1
print('A soma de todos os {} valores é = {}'.format(cont, soma))
