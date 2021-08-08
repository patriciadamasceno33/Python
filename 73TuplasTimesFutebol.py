time = ('Santos', 'Palmeiras', 'flamengo', 'Atlético', 'São Paulo', 'Corinthians',
        'Botafogo', 'Internacional', 'Ceará', 'Bahia', 'Atlético-PR', 'Fortaleza',
        'Goiás', 'Grêmio', 'Vasco', 'Fluminense', 'Cruzeiro', 'Chapecoense', 'CSA', 'Avaí')
print(f'Cinco primeiros times{time[:5]}')
print(f'Quatro últimos colocados {time[16:]}')
print(f'Em ordem alfabética {sorted(time)}')
print(f'{time[17]} está na posicao {time.index("Chapecoense")+1}')
