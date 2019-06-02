# Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado
#  e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#  sabendo que o carro custa R$:60 por dia e R$:0,15 por Km rodado.
km = float(input("Quantos KM rodados?"))
dias = float(input("Quantos dias de aluguel?"))
preço_1 = dias * 60
preço_2 = km * 0.15
valor_total = preço_1 + preço_2
print(f"O valor a pagar é de R$:{valor_total}")
