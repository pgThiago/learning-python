# Faça um programa que leia 3 números e mostre na tela qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
# verificando quem é o menor

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor é o {}'.format(menor))
# verificando quem é o maior

maior = n3
if n2>n3 and n2>n1:
     maior = n2
if n1>n2 and n1>n3:
     maior = n1
print('O maior é o {}'.format(maior))
