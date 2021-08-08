lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        #print('Número cadastrado com Sucesso..')
    else:
        print('valor duplicado')
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print(f'Voce digitou os números: {sorted(lista)}')