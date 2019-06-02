# Faça um programa que leia o comprimento de 3 retas e informe o usuário se elas podem formar um triângulo

print('=='* 12)
print('ANALISADOR DE TRIANGULOS')
print('=='* 12)
a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))
if a < (b + c):
    if b < (a + c):
        if c < (b + a):
            print('Essas medidas podem formar um triangulo')
        else:
            print('Essas medidas NÃO podem formar um triangulo')
