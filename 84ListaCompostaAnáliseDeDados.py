listan = []
listap = []
maior = menor = 0
while True:
    listan.append(str(input('Nome: ')))
    listan.append(float(input('Peso: ')))
    if len(listap) == 0:
        maior = menor = listan[1]
    else:
        if listan[1] > maior:
            maior = listan[1]
        if listan[1] < menor:
            menor = listan[1]
    listap.append(listan[:])
    listan.clear()
    r = ' '
    while r not in 'SN':
        r = (str(input('Deseja continuar? [S/N]'))).strip().upper()[0]
    if r == 'N':
        break

print(f'Ao todo voce encontrou {len(listap)} pessoas:')
print(f'O maior peso é: {maior} ', end='')
for p in listap:
    if p[1] == maior:
        print(f'[{p[0]}]', end= '')
print()
print(f'O menor peso é: {menor}')
for p in listap:
    if p[1] == menor:
        print(f'[{p[0]}]', end= '')
