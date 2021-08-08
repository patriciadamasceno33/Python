primeiro = int(input('Primeiro número: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
termo = primeiro
c = 1
while c <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    c += 1
print('\nacabou')