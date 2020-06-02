# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input('Qual é o salário do funcionário?'))
aumento = salario + (15 * salario / 100)
print("O salário do funcionário que era de R${salario:.2f} passará a ser de R${aumento:.2f}")
