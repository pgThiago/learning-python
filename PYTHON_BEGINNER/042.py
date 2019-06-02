# Refaça o desafio 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero
# Escaleno
# Isósceles 

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print('Essas medidas podem formar um triangulo', end=' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    
    if l1 != l2 != l3 != l1:
            print('ESCALENO')
    
    else:
         print('ISÓSCELES')
