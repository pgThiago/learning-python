# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
valor = float(input("Digite um valor: "))
inteira = valor // 1
print("Sua porção inteira é {:.0f}".format(math.trunc(valor))) # ou .format(inteira)