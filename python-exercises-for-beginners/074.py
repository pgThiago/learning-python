# Crie um program que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso 
# mostre a listagem de números gerados e também  maior e menor valores lidos.   

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os numeros sorteados foram: {n}')
print(max(n))
print(min(n))
