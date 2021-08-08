n = int(input('Digite um número [para sair 999]'))
cont = n
totnum = 0
while n != 999:
    n = int(input('Digite um número [para sair 999]'))
    if n == 999:
        print('Voce digitou {} numeros e a soma entre eles foi {}'.format(totnum, cont))
    cont += n
    totnum += 1
print('FIM')
