# Faça um programa que leia algo do teclado e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele.'''
algo = (input('Digite algo: '))
print(f"Só tem espaços? {algo.isspace()}")
print(f"É um número? {algo.isalnum()}")
print(f"É alfabético? {algo.isalpha()}")
print(f"Só tem maiúsculas? {algo.isupper()}")
print(f"Só tem minúsculs? {algo.islower()}")
print(f"Está capitalizada? {algo.istitle()}")
