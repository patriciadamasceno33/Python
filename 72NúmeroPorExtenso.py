c = ('zero','um', 'dois', 'tres', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'quatorze',
     'quinze', 'dezesseis', 'dezesete', 'dezoito',
     'dezenove','vinte')

while True:
    num = int(input('Digite um número de 1 a 20: '))
    if 0 <= num <= 20:
        print(f'Você escolheu o número {c[num]}')
        #break
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Tentar novamente? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('cabo')

