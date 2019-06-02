# Crie uma tupla prenchida com os vinte primeiros colocados da Tbaela do campeonato Brasileiro de futebol
# na ordem de colocação. Depois mostre:
# a) os 5 primeiros
# b) os últimos 4 colocados
# c) os times em ordem alfabética
# d) em que posição está o time da Chapecoense

times = ('Palmeiras', 'Internacional', 'São Paulo', 'Grêmio', 'Flamengo', 'Atlético', 'Cruzeiro', 'Santos','Corinthians',
         'Fluminense', 'Atlético PR', 'Botafogo', 'América MG', 'Bahia', 'Ceará SC', 'Vasco da Gama',
         'EC vitória', 'Chapecoense', 'Sport Recife', 'Paraná',)
print(f'Os 5 primeiros colocados são: {times[: 5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
p = (times.index('Chapecoense')+1)
print('O time da CHAPE encontra-se na {}° posição'.format(p))
