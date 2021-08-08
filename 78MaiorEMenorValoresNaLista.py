l = []
for i in range(0, 5):
    l.append(int(input(f'Digite um valor para a posição [{i}]: ')))
    if i == 0:
        maior = menor = l[i]
    else:
        if l[i] > maior:
            maior = l[i]
        if l[i] < menor:
            menor = l[i]
print(f'Voce digitou os valors {l}')
print(f'O maior valor foi: {maior} nas posições ', end='')
for i, v in enumerate(l):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi: {menor} nas posições ', end='')
for i, v in enumerate(l):
    if v == menor:
        print(f'{i}...', end='')



#print(f'O maior valor digitado foi {max(n)} na posicao {n.index(n)}')
