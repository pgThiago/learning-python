# Escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado
# a multa vai custar R$:7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('O valor da multa:R${:.2f}'.format(multa))
else:
    print('Dirija com segurança. Tenha uma boa viagem!')
