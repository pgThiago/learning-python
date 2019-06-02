# Tabuada com laço

numero = int(input('Digite um numero para saber sua tabuada: '))
limite = int(input('Digite até onde deseja ir a tabuada: '))
for multiplicador in range(0, limite):
   print(f"{numero:4} x {multiplicador + 1:4} = {numero * (multiplicador + 1):4}")
