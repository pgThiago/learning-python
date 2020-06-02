# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
# aluno individualmente

lista = []
boletim = []
while True:
    print('=' * 30)
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))  
    nota2 = float(input('Nota 2: '))
    print('=' * 30)
    resp = str(input('Quer continuar [S / N]? ').upper())
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    boletim.append(lista[:])
    lista.clear()
    if 'N' in resp:
        break
print('=' * 30)
print('{}'.format('N°.'), end='    ')
print('{}'.format('NOME'), end='    ')
print('{}'.format('MEDIA'))
print('=' * 30)
for n in boletim:
    print('{}'.format(boletim.index(n)), end='')
    print('{:^15}'.format(n[0]), end='')
    print('{}'.format((n[1] + n[2]) / 2))
    print('=' * 30)
while True:
    deseja = int(input('Deseja ver a nota de qual aluno? [999 para sair]: '))
    if deseja == 999:
        break
    print('==' * 30)
    print(f'O aluno {boletim[deseja][0]} tirou {boletim[deseja][1]} na 1° avaliação e {boletim[deseja][2]} na 2° avaliação.')
    print('=' * 30)
print('Programa finalizado!')
print('==' * 30)

