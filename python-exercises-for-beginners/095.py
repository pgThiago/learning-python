jogadores = []
jogador = {}
cod = 0
while True:
    gols = []
    total_de_gols = []
    jogador['Código'] = cod
    jogador['Nome'] = input('Nome do jogador: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Partidas'] = partidas
    for i in range(1, partidas + 1):
        gol = int(input(f'      Quantos gols na partida {i}? '))
        gols.append(gol)
    jogador['Gols'] = gols
    jogador['Total'] = sum(gols) # Total de gols
    jogadores.append(jogador.copy())
    cod += 1
    cont = input('Quer continuar? [S/N]: ').upper().strip()
    if cont == 'N':
        break
string = ''
print('=-=' * 33)
print('{:<30}{:<30}{:<30}{:<30}'.format('Código', 'Nome', 'Gols', 'Total'))
for jog in jogadores:
    string += '{:<30}{:<30}{:<30}{:<30}\n'.format(str(jog['Código']), str(jog['Nome']), str(jog['Gols']), str(jog['Total']))
print(string)
print('=-=' * 33)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? (Digite o código) 999 para sair: '))
    print('=-=' * 12)
    for jogador in jogadores:
        if jogador["Código"] == mostrar:
            print(f'--LEVANTAMENTO DO JOGADOR {jogador["Nome"]}:')
            for g in range(len(jogador['Gols'])):
                print(f'No jogo {g + 1} fez {jogador["Gols"][g]} gols.')
            break
    else:
        print(f'Não existe jogador com o código {mostrar}.')
    print('=-=' * 12)
    if mostrar == 999:
        print('Volte sempre!')
        break
