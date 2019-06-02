# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('VOU PENSAR EM UM NUMERO ENTRE 0 E 5. TENTE ADIVINHAR :)')
import random
chute = int(input('Em que número eu pensei?'))
computador = random.randint(0, 5)
if chute == computador:
    print("Parabéns. Você venceu :)")
else:
    print(f"GANHEI! Eu pensei no número {computador}, não no número {chute}")
