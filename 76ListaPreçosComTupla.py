l = ('sofá', 300.00, 'cama', 500.00, 'ventilador', 150.00,
     'geladeira', 700.00, 'fogão', 400.00, 'mesa', 250.00)
for i in range(0, len(l)):
    if i % 2 == 0:
        print(f'{l[i]:.<30}', end='')
    else:
        print((f'R${l[i]:.>3}'))
