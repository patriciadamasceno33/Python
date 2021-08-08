def leiaInt(n):
    while True:
        try:
            n = int(input(n))
        except (TypeError, ValueError):
            print('Erro! por favor, digite um número inteiro válido.')
            continue
        else:
            return n

def leiaFloat(n):
    while True:
        try:
            n = float(input(n))
        except (TypeError, ValueError):
            print('Erro! por favor, digite um número real válido.')
            continue
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
