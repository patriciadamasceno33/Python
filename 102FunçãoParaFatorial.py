def fatorial(n, show=False):
    ''' Calcula Fatorial de um número
    :param n: o numero a ser calculado.
    :param show: opcional. Mostrar ou não a conta.
    :return: o valor fatiorial de um número N.'''
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

print(fatorial(5, show=True))

