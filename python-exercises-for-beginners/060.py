# Faça um programa que leia um número qualquer e mostre o seu fatorial

numero = int(input('Digite o numero: '))
fatorial = numero
while numero >= 1:
    print(f"{numero}", end = " ")
    print(" = " if numero == 1 else " x ", end = " ")
    numero -= 1
    fatorial = fatorial * numero
    if numero == 1:
        print("1 = ", end = "")
        break
    
print(f"{fatorial}")
