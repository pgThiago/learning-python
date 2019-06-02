# Faça um programa que leia um número inteiro e diga se ele é ou não um número ímpar

#n = int(input('Digite um número: '))
#total = 0
#for c in range(1, n+1):
    #if n % c == 0:
        #total += 1
        #print('\033[33m', end='')
    #else:
        #print('\033[31m', end='')
    #print('{}'.format(c), end=' ')
#print('\033[34mO número {} foi divisível {} vezes'.format(n, total))
#if total == 2:
    #print('É primo')
#else:
    #print('NÃO é primo')
n = int(input('Digite um número: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        div = div + 1
    print('{}'.format(c), end=' ')
print('O número {} foi divisível {} vezes'.format(n, div), end=' ')
if div == 2:
    print(',portanto, é primo')
else:
    print(',portanto, não é primo')
