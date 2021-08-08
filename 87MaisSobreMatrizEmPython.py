matriz = [[0,0,0], [0,0,0], [0,0,0]]
somap = somac = maiorl = 0
for i in range (0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para {[i,j]}:'))

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            somap += matriz[i][j]
    print()

print(f'Soma dos pares: {somap}')

for l in range(0,3):
    somac += matriz[l][2]
print(f'Soma da 3 coluna: {somac}')

for x in range(0,3):
    if x == 0:
        maiorl = matriz[1][x]
    elif matriz[1][x] > maiorl:
        maiorl = matriz[1][x]
print(f'Maior valor da segunda linha: {maiorl}')
