soma = 0
for cont in range (1, 501, 2):
    if cont % 3 == 0:
        print(cont, end=' ')
        soma += cont
print('A soma de todos os valores e: {}'.format(soma))
