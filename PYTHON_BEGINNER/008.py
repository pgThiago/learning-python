# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
print('=+' * 10)
print('\033[;34mCONVERSOR DE MEDIDAS\033[m')
print('=+' * 10)
valor = float(input("Digite o valor em metros: "))
kilometro = valor / 1000
hectometro = valor / 100
decametro = valor / 10
decimetro = valor * 10
centímetro = valor * 100
milímetro = valor * 1000
print(f"O valor em kilometro {kilometro}")
print(f"O valor em hectometro {hectometro}")
print(f"O valor em decametro {decametro}")
print(f"O valor em decimetro {decimetro}")
print(f"O valor em centímetro {centímetro}")
print(f"O valor em milímetro {milímetro}")
