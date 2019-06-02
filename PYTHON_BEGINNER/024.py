# Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO".

cidade = str(input("Qual o nome da sua cidade? ")).upper().strip().split()
print(f"A sua cidade começa com a palavra 'SANTO'? {'SANTO' in cidade[0:5]}")
