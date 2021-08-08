from random import randint
lista = list()
jogos = list()
qtd = int(input('Quantos jogos da Loto Mania você quer?'))
tot = 0
while tot < qtd:
    cont = 0
    while True:
        num = randint(1, 100)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 40:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')