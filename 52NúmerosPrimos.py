tot = 0
num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0:
        print('\33[33m', end='')
        tot +=1
    else:
        print('\33[31m', end='')
    print('{}'.format(i), end=' ')
print('\n\33[mO numero {} foi dividigo {} vezes'.format(num, tot))
if tot == 2:
    print('por isso ele é PRIMO')
else:
    print('e por isso ele não é PRIMO')
