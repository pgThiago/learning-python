# Faça um programa que leia um ângulo qualquer e mostre na tela o seno, cosseno e tangente

import math
angulo = float(input("Digite o angulo que deseja conhecer: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
secante = 1 / cosseno
cossecante = 1 / seno
cotangente = 1 / tangente
print(f"Ângulo: {angulo}")
print(f"Seno: {seno}")
print(f"Cosseno: {cosseno}")
print(f"Tangente: {tangente}")
print(f"Secante: {secante}")
print(f"Cossecante: {cossecante}")
print(f"Cotangente: {cotangente}")
