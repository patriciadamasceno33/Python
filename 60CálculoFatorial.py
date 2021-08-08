#While
'''n = int(input('Informe o numero do fatorial: '))
cont = n
f = 1
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))'''
#For
n = int(input('Digite o numero para o seu fatorial: '))
f = 1
cont = n
for i in range(n, 1, -1):
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))