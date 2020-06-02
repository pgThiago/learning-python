# Crie um programa que gerencie o aproveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
gols = []
jogador['Nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for i in range(1, partidas + 1):
    numero_de_gols = int(input(f'    Quantos gols na partida {i}: '))
    gols.append(numero_de_gols)
    jogador['Gols'] = gols
jogador['Total'] = sum(gols) 
print(jogador)
for jog, atributo in jogador.items():
    print(f'O campo {jog} tem valor {atributo}')
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas:')
for pos, gol in enumerate(gols):
    print(f'    => Na partida {pos + 1}, fez {gol} gols')
for value in jogador.values():
    if value == sum(gols):
        print(f'Foi um total de {value} gols')