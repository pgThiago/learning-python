# Crie um programa que leia vários números inteiros pelo teclado.
# o programa só vai parar quando o usuário digitar o valor 999.
# no final mostre quantos números foram digitados e a soma entre eles, desconsiderando o flag 

'''Somar todos os valores digitados, exceto o 999'''
n = soma = c = 0
while n != 999:
    soma += n
    n = int(input('Digite um número [999 para sair]: '))
    c += 1
print(f'Você digitou {c - 1} números e a soma entre els é igual a {soma}')

# idêntica a 64