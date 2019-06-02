# Faça um programa que leia o sexo de uma pessoa, mas só aceite "M" ou "F".
# caso esteja errado peça a digitação novamente até ter um valor correto. 

genero = ''
masculino = ''
feminino = ''
while genero != 'M' and genero != 'F':
    genero = str(input('Digite o seu genero: ')).strip().upper()
    if genero == 'M':
        masculino = genero
    if genero == 'F':
        feminino = genero
if genero == 'M':
    print('O seu genero é MASCULINO!')
if genero == 'F':
    print('O seu genero é FEMININO!')
