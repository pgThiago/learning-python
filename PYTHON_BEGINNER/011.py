# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pinta-lá.
# Sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input("A largura da parede: "))
altura = float(input("A altura da parede: "))
área = largura * altura
tinta = área / 2
print(tinta)
