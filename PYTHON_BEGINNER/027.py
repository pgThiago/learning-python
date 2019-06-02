# Faça um programa que leia o nome compleyo de uma pessoa
# Em seguida mostre o primeiro e o último nome separadamente

nome = str(input('Digite seu nome completo: ')).upper().strip()
print('Muito prazer em te conhecer, {}!'.format(nome))
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))
