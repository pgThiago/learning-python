# Faça um programa que leia dois valores e mostre um MENU, como o abaixo
# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] MAIOR 
# [ 4 ] NOVOS NÚMEROS
# [ 5 ] SAIR DO PROGRAMA
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep
o =''
while o != 5:
    v = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('[1] PARA SOMAR')
    print('[2] PARA MULTIPLICAR')
    print('[3] PARA DESCOBRIR QUAL O MAIOR')
    print('[4] PARA INSERIR NOVOS VALORES')
    print('[5] PARA FINALIZAR')
    o = int(input('Qual a sua opção? '))
    if o == 5:
        print('Finalizando...')
        sleep(3)
        print('Programa encerrado')

    if o == 4:
        while o == 4:
            v = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o segundo valor: '))
            o = int(input('Qual a sua opção? '))
            if o == 5:
                print('Finalizando...')
                sleep(3)
                print('Programa encerrado')

    if o == 3 and v > v2:
        while o == 3:
            print('{} é maior do que {}'.format(v, v2))
            print('[1] PARA SOMAR')
            print('[2] PARA MULTIPLICAR')
            print('[3] PARA DESCOBRIR QUAL O MAIOR')
            print('[4] PARA INSERIR NOVOS VALORES')
            print('[5] PARA FINALIZAR')
            o = int(input('Qual a sua opção? '))
            if o == 5:
                print('Finalizando...')
                sleep(3)
                print('Programa encerrado')

    if o == 3 and v2 > v:
        while o == 3:
            print('{} é maior do que {}'.format(v2, v))
            print('[1] PARA SOMAR')
            print('[2] PARA MULTIPLICAR')
            print('[3] PARA DESCOBRIR QUAL O MAIOR')
            print('[4] PARA INSERIR NOVOS VALORES')
            print('[5] PARA FINALIZAR')
            o = int(input('Qual a sua opção? '))
            if o == 5:
                print('Finalizando...')
                sleep(3)
                print('Programa encerrado')

    if o == 3 and v == v2:
        print('{} e {} são valores iguais'.format(v, v2))
        print('[1] PARA SOMAR')
        print('[2] PARA MULTIPLICAR')
        print('[3] PARA DESCOBRIR QUAL O MAIOR')
        print('[4] PARA INSERIR NOVOS VALORES')
        print('[5] PARA FINALIZAR')
        o = int(input('Qual a sua opção? '))
        if o == 5:
            print('Finalizando...')
            sleep(3)
            print('Programa encerrado')

    if o == 2:
        while o == 2:
            print('{} X {} = {}'.format(v, v2, v * v2))
            print('[1] PARA SOMAR')
            print('[2] PARA MULTIPLICAR')
            print('[3] PARA DESCOBRIR QUAL O MAIOR')
            print('[4] PARA INSERIR NOVOS VALORES')
            print('[5] PARA FINALIZAR')
            o = int(input('Qual a sua opção? '))
            if o == 5:
                print('Finalizando...')
                sleep(3)
                print('Programa encerrado')

    if o == 1:
        while o == 1:
            print('{} + {} = {}'.format(v, v2, v + v2))
            print('[1] PARA SOMAR')
            print('[2] PARA MULTIPLICAR')
            print('[3] PARA DESCOBRIR QUAL O MAIOR')
            print('[4] PARA INSERIR NOVOS VALORES')
            print('[5] PARA FINALIZAR')
            o = int(input('Qual a sua opção? '))
            if o == 5:
                print('Finalizando...')
                sleep(3)
                print('Programa encerrado')

    if o > 5 or o <= 0:
        print('Opção inválida')
