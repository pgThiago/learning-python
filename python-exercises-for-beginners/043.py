# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
# de acordo com a tabela abaixo
# - Abaixo de 18,5: abaixo do peso
# - Entre 18,5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - Acima de 40: obesidade mórbida


peso = float(input('Qual o seu peso em Kg?'))
altura = float(input('Qual a sua altura? '))

imc = peso / altura ** 2

print('Seu IMC é igual a {:.2f} e'.format(imc), end=' ')

if imc < 18.5:
    print('você está abaixo do peso ideal')

elif imc <= 25:
    print('você está no seu peso ideal')

elif imc <= 30:
    print('você está com sobrepeso')

elif imc <= 40:
    print('você está com obesidade')

elif imc > 40:
    print('você está com obesidade mórbida')
