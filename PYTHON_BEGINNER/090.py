# Faça um programa que leia o nome e a média de um aluno, guardando também a situação, em um dicionário.
# No final mostre o conteúdo da estrutura na tela.

aluno = {}
aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input("Média de {}: ".format(aluno['Nome'])))

if aluno["Média"] >= 7.0:
     aluno["Situação"] = "aprovado"
elif 5 <= aluno["Média"] < 7:
    aluno["Situação"] = "recuperação"
else:
    aluno["Situação"] = "reprovado"
for chave, valor in aluno.items():
    print(f"{chave} é igual a {valor}")
    print()
