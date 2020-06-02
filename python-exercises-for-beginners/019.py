# Um professor quer sotear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele lendo o nome de cada aluno e escrevendo o nome do escolhido.

import random
primeiro_aluno = (input('Digite o nome do primeiro aluno: '))
segundo_aluno = (input('Digite o nome do segundo aluno: '))
terceiro_aluno = (input('Digite o nome do terceiro aluno: '))
sorteado = (primeiro_aluno, segundo_aluno, terceiro_aluno)
print(random.choice(sorteado))
