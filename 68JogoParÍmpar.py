from random import randint
c = 0
print('=-=-=-= Jogo do Par ou Ímpar =-=-=-=')
while True:
    n = int(input('Forneça um número par ou ímpar:'))
    comp = randint(0,20)
    total = n + comp
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {comp}. Total {total} .', end='')
    print('Deu Par. ' if total % 2 == 0 else 'Deu Ímpar. ', end='')
    if pi == 'P':
        if total % 2 == 0:
            c+=1
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    if pi == 'I':
        if total % 2 == 1:
            c += 1
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    print('Tente Novamente...')
print(f'Game Over: você venceu {c} vezes!')

