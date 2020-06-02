# Crie um programa que leia vários números inteiros pelo teclado
# no final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos
# o programa deve perguntar ao usuário se ele quer ou nõ continuar a digitar valores novos.

valor = int(input("Digite um valor: "))
resp = str(input("Deseja digitar novos valores? [S/N]: ")).upper()
c = media = maior = menor = soma = 0
maior = valor
menor = valor
while resp != 'N':    
    valor = int(input("Digite um valor: "))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    resp = str(input("Deseja digitar novos valores? [S/N]: ")).upper()
    c += 1
    soma += valor
    media = soma / c
print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
