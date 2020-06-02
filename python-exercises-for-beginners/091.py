# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em
# um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado
from random import randint
from time import sleep
import operator
jogadores = {}
for i in range(1, 5):
    dado = randint(1, 6)
    aux = f'jogador{i}'
    jogadores[aux] = dado
print('Valores sorteados:')
for jogador, dado in jogadores.items():
    sleep(2)
    print(f'{jogador} tirou {dado} no dado.')
jogadores_invertido = sorted(jogadores.items(),key=operator.itemgetter(1), reverse=True)
print('=-' * 20)
sleep(2)
print('{:^40}'.format('== RANKING  DOS JOGADORES =='))
sleep(2)
i = 1
for jogador, dado in jogadores_invertido:
    sleep(2)
    print(f'{i}° Lugar: {jogador} com {dado} pontos.')
    i += 1
