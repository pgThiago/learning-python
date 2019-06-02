# Crie um programa em que o usuário digite uma expressão qualquer que usa parênteses.
# Seu aplicativos deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

p = []
pa = []
a = '('
b = ')'
e = input('Digite a expressão: ')
for a in e:
    p.insert(0, a)
for b in e:
    pa.insert(0, b)
if p.count('(') == pa.count(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')
#válida ((a+b)*c)(x+y(3+2/3)*z)
#inválida ((((a+b)*c)+2)/4))
