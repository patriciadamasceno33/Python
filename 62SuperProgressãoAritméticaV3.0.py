primeiro = int(input('Primeiro número: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        c += 1
    print('\npausa')
    mais = int(input('Quantos termos a mais voce quer adicionar? '))
print('Total de termos apresentados: {}'.format(total))
