time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for i in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {i+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Responsa S ou N: ')
    if resp == 'N':
        break

print('-'*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}!')
        for i, j in enumerate(time[busca]['gols']):
            print(f'Na partida {i+1} fez {j} gols')
    print('='*40)
print('Volte Sempre!!!')

