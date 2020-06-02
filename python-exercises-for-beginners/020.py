# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos de seus alunos
# Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.
import random
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(lista)
