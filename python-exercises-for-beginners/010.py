# Conversor de moedas
print('==' * 9)
print('\033[;33mCONVERSOR DE MOEDA\033[m')
print('==' * 9)
valor = float(input("Digite o valor que deseja converter R$: "))
conversão = valor / 4.15
print(f"Com R$:{valor:.2f} você pode comprar US$:{conversão:.2f}")
