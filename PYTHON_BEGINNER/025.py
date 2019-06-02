# Crie um programa que leia o nome de uma pesoa e diga se ela possui "SILVA" no nome.
nome = str(input("Digite seu nome completo: ")).upper().strip().split()
print(f"Seu nome tem 'SILVA?' {'SILVA' in nome}")
