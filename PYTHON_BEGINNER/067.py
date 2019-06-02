# Faça um programa que leia a tabuada de vários números, um de cada vez, 
# para cada valor igitado pelo usuário.
# O programa será interrompido quando o valor digitado for negativo.

print('=' * 12)
while True:
    n = int(input('Tabuada do: '))
    if n < 0:
        break
    for t in range(0, 11):
        print(f'{n} X {t:2} = {n * t:2}')
    print('=' * 12)
print('\033[;32mEssa calculadora só aceita valores positivos\033[m')
