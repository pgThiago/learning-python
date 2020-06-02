# Faça um programa que leia duas notas de um aluno e calcule a sua média
# mostrando uma mensagem no final de acordo com a média atingida

n = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n + n2)/2
if média < 5.0:
    print('Reprovado')
elif média >= 5.0 or média <=6.9:
    print('Recuperação')
elif média >= 7.0:
    print('Aprovado')
