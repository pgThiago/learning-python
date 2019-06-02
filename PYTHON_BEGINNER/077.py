# Faça um programa que tenha uma tupla com várias palavras (desconsiderar os acentos)
# depois disso você deve mostrar, para cada palavra quais são as suas vogais 

pala = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
       'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in pala:
    print(f'\nNa palavra {p.lower()} temos', end=' ')
    for v in 'a''e''i''o''u':
        if v.lower() in p.lower():
            print(v.lower(), end=' ')
