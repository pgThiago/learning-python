# crie um programa que leia vários números e coloque-os em uma lista
# depois disso mostre:
# a) quantos números foram digitados
# b) a lista de valores ordenada de forma decrescente
# c) se o valor 5 foi digitado e está ou não na lista 

valor = []
while True:
    v = int(input('Digite um valor: '))
    valor.append(v)
    p = str(input('Quer continuar? [S / N]: ')).upper()
    if 'N' in p:
        break
valor.sort(reverse=True)
print('=' * 50)
print(f'Você digitou {len(valor)} elementos!')
print(f'Os valores em ordem decrescente: {valor}')
if 5 in valor:
    print('Valor 5 faz parte da lista!')
else:
    print('O 5 não está na lista!')
