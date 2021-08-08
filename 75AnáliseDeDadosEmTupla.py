num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Valores Digitados: {num}')
print(f'O valor 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado!')
print('Valores pares digitados: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


