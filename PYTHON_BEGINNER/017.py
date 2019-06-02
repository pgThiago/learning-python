# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retâncgulo
# calcule e mostre o comprimento da hipotenusa

import math
cateto_posto = float(input("Qual a medida do cateto oposto? "))
cateta_djacente = float(input("Qual a medida do cateto adjacente? "))
hipotenusa = math.hypot(cateto_posto, cateta_djacente)
print(f"A medida da hipotenusa é = {hipotenusa:.1f}")
