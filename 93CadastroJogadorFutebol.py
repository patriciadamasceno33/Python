jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for i in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {i+1}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('='*30)
print(jogador)
print('='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('='*30)
print(f'O jogador {jogador["nome"]} jogou {total} partidas')
for i, j in enumerate(partidas):
    print(f'Na partida {i+1}, fez {j} gols')