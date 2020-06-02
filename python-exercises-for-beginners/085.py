# Faça um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final mostre os valores pares e ímpares em ordem crescente.

num = []
for t in range(1, 8):
    n = int(input('Digite um número: '))
    num.append([])
    num.append([])
    if n % 2 == 0:
        num[0].append(n)
        par = num[0]
    else:
        num[1].append(n)
        impar = num[1]
num[0].sort()
num[1].sort()
print('-' * 30)
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
