lista = [[],[]]
n = 0
for i in range(1, 8):
    n = int(input('Num: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Valores Pares: {lista[0]}')
print(f'Valores Impares: {lista[1]}')
