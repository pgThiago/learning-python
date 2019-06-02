# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar 
# A prestação mensal não poderá exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = valor / (anos * 12)
exced = 30 * salario / 100
if prestacao > exced:
    print(f'A sua parcela é igual a R$:{prestacao:.2f} e isso excede o valor de 30% do seu salário de {salario:.2f}')
    print('Empréstimo negado')
elif prestacao <= exced:
    print(f'Para pagar uma casa de R$:{valor} em {anos} anos a sua parcela será igual a R$:{prestacao:.2f}')
