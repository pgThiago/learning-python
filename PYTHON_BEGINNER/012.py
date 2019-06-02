# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preço = float(input("Qual o preço do produto? "))
desconto = (5 * preço) / 100
valor_final = preço - desconto
print(f"O seu produto que custava R$:{preço}, na promoção com desconto de 5% vai custar R${valor_final}")
