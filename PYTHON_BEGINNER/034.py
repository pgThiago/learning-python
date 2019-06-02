# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$> 1.250,00 calcule um aumento de 10%
# Para inferiores ou igual o aumento é de 15%

salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    aumento = salario + (10 * salario)/100
    print('Com o aumento de 10% o seu salário passará para R${}'.format(aumento))

else:
    if salario <= 1250:
        aumento = salario + (15 * salario) / 100
        print('Com o aumento de 15% o seu salário passará para R${}'.format(aumento))
