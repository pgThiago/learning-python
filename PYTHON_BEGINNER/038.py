# Escreva um programa que leia dois números inteiros e compare-os mostrando na telauma mensagem:
# - o primeiro vloré maior
# - o segundo valor é maior
# - não existe valor maior, os dois são iguais 

n = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n > n2:
    print('O primeiro valor é maior')
elif n < n2:
    print('O segundo valor é maior')
elif n == n2:
    print('Não existe valor maior. São valores iguais.')
