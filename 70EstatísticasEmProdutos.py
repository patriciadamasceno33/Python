tot = prod = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço: '))
    tot += preço
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        prod += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total gasto {tot}.')
print(f'{prod} produtos custam mais de R$1.000,00.')
print(f'O produto mais barato foi {barato} que custa: {menor}.')
