# Desenvolva um programa que pergunte a distância de uma viagem em Km
# Calcule o preço da passagem cobrando R$:0,50 por Km para viagens de até 200Km
# e R$:0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}KM'.format(distancia))
if distancia <= 200:
    print('A sua viagem custará R${:.2f}'.format(distancia * 0.50))
else:
    print('A sua viagem custará R${:.2f}'.format(distancia * 0.45))
