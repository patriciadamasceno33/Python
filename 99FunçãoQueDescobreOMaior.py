from time import sleep
def maior(*n):
    print('=' * 40)
    mn = 0
    print('Analisando os valores passados...')
    for i in n:
        print(f' {i} ', end='')
        sleep(0.5)
        if i > mn:
            mn = i;
    print(f'foram informados {len(n)} valores ao todo')
    print(f'O maior valor informado foi: {mn}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(7)
maior()