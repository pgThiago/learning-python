# Melhore o desafio 061 perguntando para o usuário se ele quer mostrar mais alguns termos.
# o programa encerra quando o usuário disser que quer mostrar mais 0 termos

print('=' * 22)
print('PROGRESSÃO ARITIMÉTICA')
print('=' * 22)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        a1 += r
        c += 1
        print(a1, end=' ')
    print('PAUSA')
    mais = int(input('Digite os termos a mais: '))
print('FIM')
print('{} total de termos'.format(total))
