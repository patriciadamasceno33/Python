sn = ''
cont = tot = maior = menor = 0
while sn != 'N':
    n = float(input('Digite um numero: '))
    tot += n
    cont += 1
    media = tot/cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    sn = str(input('Quer continuar? [S/N]? ')).strip().upper()[0]
    if sn == 'N':
        print('Voce digitou {} numeros e a media foi: {}'.format(cont, media))
        print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('FIM')
