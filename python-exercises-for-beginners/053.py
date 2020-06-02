# Faça um programa que leia uma frase qualquer e diga se ela é um palíndromo
# desconsidere os espaços 

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if junto == inverso:
    print('É palíndromo')
else:
    print('Não é palíndromo')
