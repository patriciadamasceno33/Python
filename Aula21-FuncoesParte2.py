'''def somar(a=0, b=0, c=0):
    """
    soma os parâmetros
    """
    s = a + b + c
    print(f'A soma vale: {s}')


somar(4,3)
help(somar)

def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale: {a}')
    print(f'B dentro vale: {b}')
    print(f'C dentro vale: {c}')


#main
a=5
teste(a)
print(f'A fora vale: {a}')'''

def par(n=0):
    if n%2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par')
else:
    print('Não é par')
