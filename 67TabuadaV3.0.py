n = 0
c = 1
while n >= 0:
    n = int(input('Valor da Tabuada:'))
    print('-'*20)
    for c in range(11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 20)
print('Acabou!')