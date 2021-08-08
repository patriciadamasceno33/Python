primeiro = int(input('Informe o primeiro numero: '))
razao = int(input('Informe a razão: '))
decimo = primeiro + (10-1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{} -'.format(i), end='- ')
print('Acabou')
