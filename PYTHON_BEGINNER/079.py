# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# caso o número já exista lá dentro, ele não será adicionado. No final serão mostrados todos os
# valores únicos digitados em ordem crescente.

valores = []
resp = ' '
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado')
    else:
        print('Valor duplicado. Não vou adicionar')
    resp = str(input('Deseja continuar? [S / N] ')).upper()
    if 'N' in resp:
        break
print(sorted(valores))