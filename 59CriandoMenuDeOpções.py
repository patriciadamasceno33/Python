from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    1 - Somar
    2 - Multiplicar
    3 - Maior
    4 - Novos números
    5 = Sair ''')
    op = int(input('Escolha sua opcao: '))
    if op == 1:
        result = n1 + n2
        print('A soma entre {} + {} é: {}'.format(n1, n2, result))
    elif op == 2:
        result = n1 * n2
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, result))
    elif op == 3:
        if n1 > n2:
            result = n1
            print('O maior numero entre {} e {} é: {}'.format(n1, n2, result))
        else:
            result = n2
            print('O maior numero entre {} e {} é: {}'.format(n1, n2, result))
    elif op == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Saindo...')
    else:
        print('Opção inválida. Tente novamente!')
    print('-'*40)
    sleep(2)
print('Fim do programa')