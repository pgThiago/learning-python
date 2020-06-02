# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# No final do programa mostre:
# - A média de idade do grupo
# - Nome do homem mais velho
# - Número de mulheres com menos de 20 anos 

media = 0
hmaisvelho = 0
velho = ''
novas = 0
for n in range(1, 5):
    print('*==== {} PESSOA ====*'.format(n))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    media += idade
    if idade == 1 and 'MASCULINO' in sexo:
        hmaisvelho = idade
        velho = nome
    if 'MASCULINO' in sexo and idade > hmaisvelho:
        hmaisvelho = idade
        velho = nome
    if 'FEMININO' in sexo and idade < 20:
        novas += 1
midade = media / 4
print('a media é {} a idade do mais velho {} e o nome dele {}'.format(midade, hmaisvelho, velho))
print('{} mulheres menores de 20 anos'.format(novas))

