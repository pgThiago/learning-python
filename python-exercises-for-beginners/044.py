# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros 

preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a sua opção de pagamento? '))
if opcao == 1:
    desconto = preco - (10 * preco / 100)
    print('Sua compra com desconto de 10% sairá por R$:{:.2f}'.format(desconto))
elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print('Sua compra com desconto de 5% sairá por R$:{:.2f}'.format(desconto))
elif opcao == 3:
    div = preco /  2
    print('Sua compra parcelada em 2x sairá por R${}, cada parcela'.format(div))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    n = preco / parcelas
    juros = 20 * n / 100
    vf = preco + (juros * parcelas)
    print('Sua compra será parcelada em {}x de {} COM JUROS!'.format(parcelas, n))
    print('Custará R$:{} NO FINAL'.format(vf))
else:
    print('Não existe essa opção!')
