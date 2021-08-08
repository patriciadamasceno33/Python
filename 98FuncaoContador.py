from time import sleep
def separador():
    print('='*30)

def contador(i, j, p):
    print(f'Contagem de {i} até {j} de {p} em {p}')
    sleep(1.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < j:
        cont = i
        while cont <= j:
            print(f' {cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= j:
            print(f' {cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


#main
contador(1, 10, 1)
separador()
contador(10, 0, 2)
separador()
print('Agora é sua vez de prosinalizar')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
